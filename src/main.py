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
WS_OVERLAPPEDWINDOW = 13565952
CW_USEDEFAULT = -2147483648
IDC_ARROW = 32512
BLACK_BRUSH = 4
WM_CLOSE = 16
WM_SIZE = 5

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

VIDSRC_HOST = APP_SETTINGS.get('VIDSRC_HOST', 'vidsrc.sh')
USER_AGENT = APP_SETTINGS.get('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0')
DARK_MODE = APP_SETTINGS.get('DARK_MODE', True)

########################################
# WebView settings
########################################
SETTINGS.USER_AGENT = USER_AGENT
SETTINGS.BROWSER_EXTENSIONS_ENABLED = True
if IS_FROZEN:
    SETTINGS.USER_DATA_FOLDER = os.path.join(APP_DIR, '..', 'profile')  # Use a local profile folder
#SETTINGS.ADDITIONAL_BROWSER_ARGUMENTS = '--disable-web-security'

########################################
#
########################################
def usage():
    print(f'\nUsage:\n\n{APP_NAME} imdb-id [--play]\n{APP_NAME} --query "some movie title"', file=sys.stderr)
    sys.exit(1)

########################################
#
########################################
def main():
    if len(sys.argv) < 2:
        usage()

    play = False
    is_query = False

    if sys.argv[1] == '--query':
        if len(sys.argv) < 3:
            usage()
        is_query = True
        query = sys.argv[2]

    else:
        imdb_id = sys.argv[1]
        if not sys.argv[1].startswith('tt'):
            print(f"Error: imdb-id invalid. A valid id starts with 'tt' followed by digits.", file=sys.stderr)
            sys.exit(2)
        play = len(sys.argv) > 2 and sys.argv[2] == '--play'

    ########################################
    #
    ########################################
    def _window_proc_callback(hwnd, msg, wparam, lparam):
        if msg == WM_CLOSE:
            user32.PostQuitMessage(0)

        elif msg == WM_SIZE:
            width, height = lparam & 0xFFFF, (lparam >> 16) & 0xFFFF
            webview.put_bounds(RECT(0, 0, width, height))

        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

    newclass = WNDCLASSEXW()
    newclass.lpfnWndProc = WNDPROC(_window_proc_callback if play else user32.DefWindowProcW)
    newclass.lpszClassName = APP_NAME
    newclass.hbrBackground = gdi32.GetStockObject(BLACK_BRUSH)
    newclass.hCursor = user32.LoadCursorW(None, IDC_ARROW)
    newclass.hIcon = user32.LoadIconW(kernel32.GetModuleHandleW(None), LPCWSTR(1))
    user32.RegisterClassExW(byref(newclass))

    hwnd = user32.CreateWindowExW(
        0,
        APP_NAME,
        APP_NAME,
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
        None, None, None, 0
    )
    if DARK_MODE:
        windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, byref(c_int(1)), sizeof(c_int))

    if is_query:
        query = query.lower().replace(' ', '_')
        url = 'https://v2.sg.media-imdb.com/suggestion/' + ('x' if query[0] == '%' else query[0]) + '/' + query + '.json'
    else:
        url = f'https://data.{VIDSRC_HOST}/api.php?type=movie&imdb={imdb_id}'

    webview = WebView2(parent_hwnd = hwnd, url = url)

    ########################################
    #
    ########################################
    def on_WEBVIEW_READY(*args):
        # Install our tiny extension in the local profile
        extension_folder = os.path.join(APP_DIR, 'sniffer')
        webview.profile_add_browser_extension(extension_folder, lambda err, ex: None)

    webview.connect(EVENT.WEBVIEW_READY, on_WEBVIEW_READY)

    ########################################
    #
    ########################################
    def on_json_loaded(sender):
        webview.disconnect(EVENT.DOM_CONTENT_LOADED, on_json_loaded)

        ########################################
        #
        ########################################
        def on_json_data(err, data):
            data = json.loads(data)

            if is_query:
                for row in data['d']:
                    try:
                        if row['q'] == 'feature':
                            print(f"{row['id']}\t\"{row['l']}\"\t{row['y']}")
                    except:
                        pass
                webview.close()
                user32.PostQuitMessage(3)
                return

            if err != 0 or int(data['status_code']) != 200:
                print(f'Movie with ID {imdb_id} was not found.', file=sys.stderr)
                webview.close()
                user32.PostQuitMessage(3)
                return

            ########################################
            # Block all popup windows.
            # We also use this to pass the found master.m3u8 URL from our extension to the application.
            ########################################
            def on_new_window_requested(webview, args):
                args.put_Handled(1)
                uri = args.get_Uri()
                if '/master.m3u8' in uri:
                    if play:
                        user32.SetWindowTextW(hwnd, data['data']['title'])
                        user32.ShowWindow(hwnd, 1)
                        webview.set_visible(True)
                    else:
                        print(uri)
                        webview.close()
                        user32.PostQuitMessage(0)

            webview.connect(EVENT.NEW_WINDOW_REQUESTED, on_new_window_requested)

            ########################################
            #
            ########################################
            def on_frame_created(sender, frame):
                frame.connect(EVENT.DOM_CONTENT_LOADED, on_frame_dom_content_loaded)
                frame.connect(EVENT.FRAME_CREATED, on_frame_created)

            ########################################
            #
            ########################################
            def on_frame_dom_content_loaded(sender):
                # This button must be clicked, otherwise the actual video stream is not loaded.
                sender.execute_js("if (document.querySelector('#bigPlay')) document.querySelector('#bigPlay').click()")

            webview.connect(EVENT.DOM_CONTENT_LOADED, on_frame_dom_content_loaded)
            webview.connect(EVENT.FRAME_CREATED, on_frame_created)

            # Load the vidsrc iframe
            webview.execute_js(f'''
document.body.style.overflow='hidden';
document.body.style.background='black';
document.body.innerHTML='<iframe src="https://{VIDSRC_HOST}/embed/{imdb_id}" style="width:100vw;height:100vh;border:none;"></iframe>';'''
            )

        webview.execute_js('JSON.parse(document.body.textContent)', on_json_data)

    webview.connect(EVENT.DOM_CONTENT_LOADED, on_json_loaded)

    msg = MSG()
    while user32.GetMessageW(byref(msg), None, 0, 0):
        user32.TranslateMessage(byref(msg))
        user32.DispatchMessageW(byref(msg))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
