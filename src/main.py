import json
import os
import sys
from ctypes import *
from ctypes.wintypes import *
from webview2 import *

########################################
# Additional WinAPI types
########################################
LONG_PTR = c_longlong
WNDPROC = WINFUNCTYPE(LONG_PTR, HWND, UINT, WPARAM, LPARAM)

class WNDCLASSEXW(Structure):
    def __init__(self, *args, **kwargs):
        super(WNDCLASSEXW, self).__init__(*args, **kwargs)
        self.cbSize = sizeof(self)
    _fields_ = [
        ("cbSize", c_uint),
        ("style", c_uint),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", c_int),
        ("cbWndExtra", c_int),
        ("hInstance", HANDLE),
        ("hIcon", HANDLE),
        ("hCursor", HANDLE),
        ("hbrBackground", HANDLE),
        ("lpszMenuName", LPCWSTR),
        ("lpszClassName", LPCWSTR),
        ("hIconSm", HANDLE)
    ]

########################################
# Used WinAPI functions
########################################
gdi32 = windll.gdi32
gdi32.GetStockObject.restype = HANDLE

kernel32 = windll.kernel32
kernel32.GetModuleHandleW.argtypes = (LPCWSTR,)
kernel32.GetModuleHandleW.restype = HMODULE

user32 = windll.user32
user32.CreateWindowExW.argtypes = (DWORD, LPCWSTR, LPCWSTR, DWORD, INT, INT, INT, INT, HWND, HMENU, HINSTANCE, LPVOID)
user32.DefWindowProcW.argtypes = (HWND, UINT, WPARAM, LPARAM)
user32.DispatchMessageW.argtypes = (LPMSG,)
user32.GetMessageW.argtypes = (LPMSG, HWND, UINT, UINT)
user32.LoadCursorW.argtypes = (HINSTANCE, LPVOID)
user32.LoadIconW.argtypes = (HINSTANCE, LPCWSTR)
user32.LoadIconW.restype = HICON
user32.RegisterClassExW.argytpes = (POINTER(WNDCLASSEXW),)
user32.TranslateMessage.argtypes = (LPMSG,)

########################################
# Used WinAPI constants
########################################
#WS_OVERLAPPED = 0
BLACK_BRUSH = 4
CW_USEDEFAULT = -2147483648
GWL_STYLE = -16
IDC_ARROW = 32512
SW_SHOWMAXIMIZED = 3
SW_SHOWNORMAL = 1
WM_CLOSE = 16
WM_SIZE = 5
WS_OVERLAPPEDWINDOW = 13565952

########################################
# App settings
########################################
APP_NAME = "vidfind"
APP_DIR = os.path.dirname(__file__)

IS_FROZEN = getattr(sys, 'frozen', False)

try:
    with open(os.path.join(APP_DIR, 'settings.json'), 'r') as f:
        APP_SETTINGS = json.loads(f.read())
except:
    APP_SETTINGS = {}

# Settings that can be overwritten by a JSON file called 'settings.json' in the 'data' folder
VIDSRC_HOST = APP_SETTINGS.get('VIDSRC_HOST', 'vidsrc.sh')
USER_AGENT = APP_SETTINGS.get('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0')
DARK_MODE = APP_SETTINGS.get('DARK_MODE', True)

########################################
# WebView settings
########################################
SETTINGS.USER_AGENT = USER_AGENT
SETTINGS.BROWSER_EXTENSIONS_ENABLED = True
if IS_FROZEN:
    SETTINGS.USER_DATA_FOLDER = os.path.join(APP_DIR, '..', 'profile')

ERROR_WRONG_INPUT = 1
ERROR_SERVER_NOT_REACHED = 2
ERROR_MOVIE_NOT_FOUND = 3
ERROR_VIDEO_NOT_FOUND = 4
ERROR_UNKNOWN_ERROR = 5


########################################
#
########################################
class Main():

    ########################################
    #
    ########################################
    def __init__(self):

        self.imdb_id = None
        self.is_query = False
        self.is_query_and_load = False
        self.is_play = False
        self.query_str = None
        self.fullscreen = False
        self.exit_code = 0

        if sys.argv[1] == '--query':
            self.is_query = True
            self.query_str = sys.argv[2]

        elif sys.argv[1].startswith('tt'):
            self.imdb_id = sys.argv[1]
            self.is_play = len(sys.argv) > 2 and sys.argv[2] == '--play'

        else:
            self.is_query_and_load = True
            self.query_str = sys.argv[1]
            self.is_play = len(sys.argv) > 2 and sys.argv[2] == '--play'

        ########################################
        #
        ########################################
        def _window_proc_callback(hwnd, msg, wparam, lparam):
            if msg == WM_CLOSE:
                user32.PostQuitMessage(0)

            elif msg == WM_SIZE:
                width, height = lparam & 0xFFFF, (lparam >> 16) & 0xFFFF
                self.webview.put_bounds(RECT(0, 0, width, height))

            return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

        newclass = WNDCLASSEXW()
        newclass.lpfnWndProc = WNDPROC(_window_proc_callback if self.is_play else user32.DefWindowProcW)
        newclass.lpszClassName = APP_NAME
        newclass.hbrBackground = gdi32.GetStockObject(BLACK_BRUSH)
        newclass.hCursor = user32.LoadCursorW(None, IDC_ARROW)
        newclass.hIcon = user32.LoadIconW(kernel32.GetModuleHandleW(None), LPCWSTR(1))
        user32.RegisterClassExW(byref(newclass))

        self.hwnd = user32.CreateWindowExW(
            0,
            APP_NAME,
            APP_NAME,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
            None, None, None, 0
        )
        if DARK_MODE:
            windll.dwmapi.DwmSetWindowAttribute(self.hwnd, 20, byref(c_int(1)), sizeof(c_int))

        if self.is_query or self.is_query_and_load:
            q = self.query_str.lower().replace(' ', '_')
            url = 'https://v2.sg.media-imdb.com/suggestion/' + ('x' if q[0] == '%' else q[0]) + '/' + q + '.json'
        else:
            url = f'https://data.{VIDSRC_HOST}/api.php?type=movie&imdb={self.imdb_id}'

        self.webview = WebView2(parent_hwnd = self.hwnd, url = url)

        if not self.is_query:
            ########################################
            #
            ########################################
            def on_WEBVIEW_READY(*args):
                # Install our tiny extension in the local profile
                extension_folder = os.path.join(APP_DIR, 'sniffer')
                self.webview.profile_add_browser_extension(extension_folder, lambda err, ex: None)

            self.webview.connect(EVENT.WEBVIEW_READY, on_WEBVIEW_READY)

        if self.is_query or self.is_query_and_load:
            self.webview.connect(EVENT.DOM_CONTENT_LOADED, self.on_imdb_json_loaded)
        else:
            self.webview.connect(EVENT.DOM_CONTENT_LOADED, self.on_vidsrc_json_loaded)

        msg = MSG()
        while user32.GetMessageW(byref(msg), None, 0, 0) != 0:
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageW(byref(msg))
        sys.exit(self.exit_code)

    ########################################
    #
    ########################################
    def exit(self, exit_code = 0):
        self.exit_code = exit_code
        self.webview.close()
        user32.PostQuitMessage(0)

    ########################################
    #
    ########################################
    def on_imdb_json_loaded(self, sender):
        self.webview.disconnect(EVENT.DOM_CONTENT_LOADED, self.on_imdb_json_loaded)

        def on_json_data(err, data):
            data = json.loads(data)

            if type(data) != dict:
                print('Error: Server not reached.', file=sys.stderr)
                self.exit(ERROR_SERVER_NOT_REACHED)

            elif self.is_query:
                if 'd' in data:
                    for row in data['d']:
                        try:
                            if row['q'] == 'feature':
                                print(f"{row['id']}\t\"{row['l']}\"\t{row['y']}")
                        except:
                            pass
                    self.exit()
                else:
                    print(f'Error: Unknown error.', file=sys.stderr)
                    self.exit(ERROR_UNKNOWN_ERROR)

            elif self.is_query_and_load:
                if 'd' in data:
                    for row in data['d']:
                        try:
                            if row['q'] == 'feature':
                                self.imdb_id = row['id']
                                self.webview.connect(EVENT.DOM_CONTENT_LOADED, self.on_vidsrc_json_loaded)
                                self.webview.load_url(f'https://data.{VIDSRC_HOST}/api.php?type=movie&imdb={self.imdb_id}')
                                return
                        except:
                            pass

                    print('Error: Movie not found.', file=sys.stderr)
                    self.exit(ERROR_MOVIE_NOT_FOUND)
                else:
                    print('Error: Unknown error.', file=sys.stderr)
                    self.exit(ERROR_UNKNOWN_ERROR)

        self.webview.execute_js('JSON.parse(document.body.textContent)', on_json_data)

    ########################################
    #
    ########################################
    def on_vidsrc_json_loaded(self, sender):
        self.webview.disconnect(EVENT.DOM_CONTENT_LOADED, self.on_vidsrc_json_loaded)

        def on_json_data(err, data):
            data = json.loads(data)

            if type(data) != dict:
                print('Error: Server not reached.', file=sys.stderr)
                self.exit(ERROR_SERVER_NOT_REACHED)

            elif int(data['status_code']) != 200:
                print('Error: Video not found.', file=sys.stderr)
                self.exit(ERROR_VIDEO_NOT_FOUND)

            else:
               self.load_vidsrc(data['data']['title'])

        self.webview.execute_js('JSON.parse(document.body.textContent)', on_json_data)

    ########################################
    #
    ########################################
    def load_vidsrc(self, movie_title):

        ########################################
        # Block all popup windows.
        # We also use this to pass the found master.m3u8 URL from our extension to the application.
        ########################################
        def on_new_window_requested(sender, args):
            args.put_Handled(1)
            uri = args.get_Uri()
            if '/master.m3u8' in uri:
                if self.is_play:
                    user32.SetWindowTextW(self.hwnd, movie_title)
                    user32.ShowWindow(self.hwnd, 1)
                    self.webview.set_visible(True)
                else:
                    print(uri)
                    self.exit()

        self.webview.connect(EVENT.NEW_WINDOW_REQUESTED, on_new_window_requested)

        ########################################
        #
        ########################################
        def on_frame_dom_content_loaded(sender):
            # This button must be clicked, otherwise the actual video stream is not loaded.
            sender.execute_js("if (document.querySelector('#bigPlay')) document.querySelector('#bigPlay').click()")

            # Make the fullscreen button (and fullscreen by double-click) work
            if self.is_play:
                ########################################
                #
                ########################################
                def toggle_fullscreen():
                    self.fullscreen = not self.fullscreen
                    style = user32.GetWindowLongA(self.hwnd, GWL_STYLE)
                    user32.SetWindowLongA(self.hwnd, GWL_STYLE, style & ~13565952 if self.fullscreen else style | 13565952)
                    user32.ShowWindow(self.hwnd, SW_SHOWMAXIMIZED if self.fullscreen else SW_SHOWNORMAL)

                sender.expose('toggle_fullscreen', toggle_fullscreen)

                sender.execute_js(
"""const video = document.querySelector('video');
if (video)
{
    document.addEventListener("dblclick", () => chrome.webview.api.toggle_fullscreen());
    video.parentNode.requestFullscreen = () => chrome.webview.api.toggle_fullscreen();
}"""
                )

        ########################################
        #
        ########################################
        def on_frame_created(sender, frame):
            frame.connect(EVENT.DOM_CONTENT_LOADED, on_frame_dom_content_loaded)
            frame.connect(EVENT.FRAME_CREATED, on_frame_created)

        self.webview.connect(EVENT.DOM_CONTENT_LOADED, on_frame_dom_content_loaded)
        self.webview.connect(EVENT.FRAME_CREATED, on_frame_created)
        self.webview.load_url(f"https://{VIDSRC_HOST}/embed/{self.imdb_id}")


if __name__ == '__main__':
    if len(sys.argv) < 2 or (sys.argv[1] == '--query' and len(sys.argv) < 3):
        print(
            (
                '\nUsage:\n\n'
                f'{APP_NAME} imdb-id [--play]\n'
                f'{APP_NAME} "some movie title" [--play]\n'
                f'{APP_NAME} --query "some movie title"'
            ),
            file=sys.stderr
        )
        sys.exit(ERROR_WRONG_INPUT)
    Main()
