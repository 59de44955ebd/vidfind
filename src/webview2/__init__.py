import json
import os
import sys
from sysconfig import get_platform
import time

#from winapp.themes import *
#from winapp.const import *
#from winapp.dlls import *
TRUE = 1
FALSE = 0

from .interfaces import *
from .handlers import *

if getattr(sys, 'frozen', False):
    loader_dll = os.path.join(os.path.dirname(__file__), 'loader.dll')
else:
    loader_dll = os.path.join(os.path.dirname(__file__), 'native', get_platform(), 'loader.dll')

LOADER = CDLL(loader_dll)
LOADER.CreateEnvironmentWithOptions.argtypes = (LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, BOOL, POINTER(ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler))

class SETTINGS:
    # https://peter.sh/experiments/chromium-command-line-switches/
    # https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/webview-features-flags?tabs=dotnetcsharp
    ADDITIONAL_BROWSER_ARGUMENTS = None

    ALLOW_HOST_INPUT_PROCESSING = False
    ARE_HOST_OBJECTS_ALLOWED = True
    BROWSER_ACCELERATOR_KEYS_ENABLED = None
    BROWSER_EXECUTABLE_FOLDER = None
    BROWSER_EXTENSIONS_ENABLED = False
    COLOR_SCHEME = None
    DEFAULT_CONTEXT_MENUS_ENABLED = True
    DEFAULT_SCRIPT_DIALOGS_ENABLED = True
    DEV_TOOLS_ENABLED = True
    FILE_DROP_SELECTOR = 'html'
    GENERAL_AUTOFILL_ENABLED = None
    LANGUAGE = None
    PASSWORD_AUTOSAVE_ENABLED = None
    PINCH_ZOOM_ENABLED = None
    STATUS_BAR_ENABLED = True
    SWIPE_NAVIGATION_ENABLED = None
    USER_AGENT = None
    USER_DATA_FOLDER = None
    ZOOM_CONTROL_ENABLED = False

# Order:
# NavigationStarting
# ContentLoading -> Earliest moment when JS can be injected. Not raised if a same page navigation occurs.
# DOMContentLoaded
# NavigationCompleted

class EVENT:
    ACCELERATOR_KEY_PRESSED = 101
    CONTAINS_FULLSCREEN_ELEMENT_CHANGED = 102
    CONTENT_LOADING = 103
    CONTEXT_MENU_REQUESTED = 104
    DOCUMENT_TITLE_CHANGED = 105
    DOM_CONTENT_LOADED = 106
    DOWNLOAD_STARTING = 107
    FAVICON_CHANGED = 108
    FILES_DROPPED = 109
    FOCUS_LOST = 110
    FRAME_CREATED = 111
    HISTORY_CHANGED = 112
    MENU_COMMAND = 113
    NAVIGATION_COMPLETED = 114
    NAVIGATION_STARTING = 115
    NEW_WINDOW_REQUESTED = 116
    PERMISSION_REQUESTED = 117
    SOURCE_CHANGED = 118
    STATUS_BAR_TEXT_CHANGED = 119
    WEBVIEW_READY = 120
    WEB_MESSAGE_RECEIVED = 121
    WEB_RESOURCE_REQUESTED = 122
    WEB_RESOURCE_RESPONSE_RECEIVED = 123

# COREWEBVIEW2_BROWSING_DATA_KINDS
class BROWSING_DATA_KINDS:
    FILE_SYSTEMS = 0x1
    INDEXED_DB = 0x2
    LOCAL_STORAGE = 0x4
    WEB_SQL = 0x8
    CACHE_STORAGE = 0x10
    ALL_DOM_STORAGE = 0x20
    COOKIES = 0x40
    ALL_SITE = 0x80
    DISK_CACHE = 0x100
    DOWNLOAD_HISTORY = 0x200
    GENERAL_AUTOFILL = 0x400
    PASSWORD_AUTOSAVE = 0x800
    BROWSING_HISTORY = 0x1000
    SETTINGS = 0x2000
    ALL_PROFILE = 0x4000
    SERVICE_WORKERS = 0x8000

# COREWEBVIEW2_CONTEXT_MENU_ITEM_KIND
class CONTEXT_MENU_ITEM_KIND:
    COMMAND = 0
    CHECK_BOX = 1
    RADIO = 2
    SEPARATOR = 3
    SUBMENU = 4

# COREWEBVIEW2_CONTEXT_MENU_TARGET_KIND
class CONTEXT_MENU_TARGET_KIND:
    PAGE = 0
    IMAGE = 1
    SELECTED_TEXT = 2
    AUDIO = 3
    VIDEO = 4

# COREWEBVIEW2_COOKIE_SAME_SITE_KIND
class COOKIE_SAME_SITE_KIND:
    NONE = 0
    LAX = 1
    STRICT = 2

# COREWEBVIEW2_DOWNLOAD_STATE
class DOWNLOAD_STATE:
    IN_PROGRESS = 0
    INTERRUPTED = 1
    COMPLETED = 2

# COREWEBVIEW2_HOST_RESOURCE_ACCESS_KIND
class HOST_RESOURCE_ACCESS_KIND:
    DENY = 0
    ALLOW = 1
    DENY_CORS = 2

# COREWEBVIEW2_CAPTURE_PREVIEW_IMAGE_FORMAT
# COREWEBVIEW2_FAVICON_IMAGE_FORMAT
class IMAGE_FORMAT:
    PNG = 0
    JPEG = 1

# COREWEBVIEW2_KEY_EVENT_KIND
class KEY_EVENT_KIND:
    KEY_DOWN = 0
    KEY_UP = 1
    SYSTEM_KEY_DOWN = 2
    SYSTEM_KEY_UP = 3

# COREWEBVIEW2_PERMISSION_KIND
class PERMISSION_KIND:
    UNKNOWN_PERMISSION = 0
    MICROPHONE = 1
    CAMERA = 2
    GEOLOCATION = 3
    NOTIFICATIONS = 4
    OTHER_SENSORS = 5
    CLIPBOARD_READ = 6
    MULTIPLE_AUTOMATIC_DOWNLOADS = 7
    FILE_READ_WRITE = 8
    AUTOPLAY = 9
    LOCAL_FONTS = 10
    MIDI_SYSTEM_EXCLUSIVE_MESSAGES = 11
    WINDOW_MANAGEMENT = 12
    PERSISTENT_STORAGE = 13

# COREWEBVIEW2_PERMISSION_STATE
class PERMISSION_STATE:
    DEFAULT = 0
    ALLOW = 1
    DENY = 2

# COREWEBVIEW2_PREFERRED_COLOR_SCHEME
class PREFERRED_COLOR_SCHEME:
    AUTO = 0
    LIGHT = 1
    DARK = 2

# COREWEBVIEW2_PRINT_DIALOG_KIND
class PRINT_DIALOG_KIND:
    BROWSER = 0
    SYSTEM = 1

# COREWEBVIEW2_PRINT_ORIENTATION
class PRINT_ORIENTATION:
    PORTRAIT = 0
    LANDSCAPE = 1

# COREWEBVIEW2_WEB_RESOURCE_CONTEXT
class WEB_RESOURCE_CONTEXT:
    ALL = 0
    DOCUMENT = 1
    STYLESHEET = 2
    IMAGE = 3
    MEDIA = 4
    FONT = 5
    SCRIPT = 6
    XML_HTTP_REQUEST = 7
    FETCH = 8
    TEXT_TRACK = 9
    EVENT_SOURCE = 10
    WEBSOCKET = 11
    MANIFEST = 12
    SIGNED_EXCHANGE = 13
    PING = 14
    CSP_VIOLATION_REPORT = 15
    OTHER = 16

class WebviewNotReadyException(Exception):
    pass

DEFAULT_HTML = """
<!doctype html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=0">
        <meta name="color-scheme" content="dark">
        <title>about:blank</title>
    </head>
    <body></body>
</html>
"""

API_JS = """
if (!window.chrome.webview.api){
    window.chrome.webview.api = {
        _results: {},
        _js_return: (uid, timeout_ms) => {
            return new Promise(async (resolve) => {
                for (let i = 0; i < timeout_ms; i+=10){
                    if (uid in chrome.webview.api._results)
                        break;
                    await new Promise(r => setTimeout(r, 10));
                }
                const res = chrome.webview.api._results[uid];
                delete chrome.webview.api._results[uid];
                resolve(res);
            });
        },
        _expose: (func_name, path, timeout_ms, return_result) => {
            let obj = chrome.webview.api;
            for (let p of path){
                if (!(p in obj))
                    obj[p] = {};
                obj = obj[p];
            }
            obj[func_name] = function(){
                const uid = return_result ? 'id' + (new Date()).getTime() : -1;
                window.chrome.webview.postMessage([uid, func_name, Array.from(arguments)]);
                if (return_result)
                    return chrome.webview.api._js_return(uid, timeout_ms);
            }
        },
        _resolve: (func_name, func) => {
            func().then(res => window.chrome.webview.postMessage([-1, func_name, [res]]));
        },
    };
    window.chrome.webview.addEventListener('message', (msg) => {chrome.webview.api._results[msg.data[0]] = msg.data[1]});
    console.log('API_JS loaded');
};
"""

DROP_INIT_JS = """
function _init_drop_() {{
    window.chrome.webview._dragover = (evt) => {{
        if (evt.dataTransfer.files){{
            evt.stopPropagation();
            evt.preventDefault();
        }}
    }};
    window.chrome.webview._drop = (evt) => {{
        if (evt.dataTransfer.files.length){{
            evt.stopPropagation();
            evt.preventDefault();
            chrome.webview.postMessageWithAdditionalObjects(['files_dropped', evt.target.id], evt.dataTransfer.files);
        }}
    }};
    for (let el of document.querySelectorAll("{}")){{
        el.addEventListener('dragover', window.chrome.webview._dragover);
        el.addEventListener('drop', window.chrome.webview._drop);
    }}
}}
if (document && document.readyState === "complete")
    _init_drop_();
else
    window.addEventListener("DOMContentLoaded", () => _init_drop_());
"""

DROP_EXIT_JS = """
function _exit_drop_() {{
    for (let el of document.querySelectorAll("{}")){{
        el.removeEventListener('dragover', window.chrome.webview._dragover);
        el.removeEventListener('drop', window.chrome.webview._drop);
    }}
}}
if (document && document.readyState === "complete")
    _exit_drop_();
else
    window.addEventListener("DOMContentLoaded", () => _exit_drop_());
"""

########################################
# res = call_sync(self._active_webview.get_cookies)
########################################
def call_sync(func, **kwargs):
    h_event = kernel32.CreateEventW(0, TRUE, FALSE, None)

    class ctx():
        result = None

    def callback(*result, h_event=h_event):
        ctx.result = result
        kernel32.SetEvent(h_event)

    try:
        func(callback=callback, **kwargs)
    except Exception as e:
        print(e)
        kernel32.CloseHandle(h_event)
        return (-1, e)

    hr = ole32.CoWaitForMultipleHandles(
        COWAIT_DISPATCH_WINDOW_MESSAGES | COWAIT_DISPATCH_CALLS | COWAIT_INPUTAVAILABLE,
        0xFFFFFFFF,
        1,
        (HANDLE * 1)(h_event),
        byref(DWORD())
    )
    kernel32.CloseHandle(h_event)
    return ctx.result


########################################
# https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/
# But we only need to support __setitem__ and __delitem__, nothing else.
########################################
class Headers(dict):

    def __init__(self, d={}):
        super().__init__(**d)
        self._edited = []
        self._deleted = []

    def __setitem__(self, key, value):
        self._edited.append(key)
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self._deleted.append(key)
        super().__delitem__(key)


########################################
#
########################################
class Request:
    def __init__(self, url, method, headers):
        self.url = url
        self.method = method
        self.headers = headers

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return str(self.__dict__)


########################################
#
########################################
class Response:
    def __init__(self, url, status, headers):
        self.url = url
        self.status = status
        self.headers = headers

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return str(self.__dict__)


########################################
#
########################################
class Frame:

    ########################################
    #
    ########################################
    def __init__(self, frame):
        self._frame = frame
        self._listeners = {}
        self._handlers = {}  # evt => handler
        self._tokens = {}  # evt => token
        self._expose_callbacks = {}  # evt => [callbacks...]

        frame.add_WebMessageReceived(
            FrameWebMessageReceivedEventHandler(self._on_web_message_received).interface()
        )

    ########################################
    #
    ########################################
    def connect(self, evt, func):
        if evt not in self._listeners:
            self._listeners[evt] = []
        elif func in self._listeners[evt]:
            return
        init_event = not self._listeners[evt]
        self._listeners[evt].append(func)
        if init_event:
            self._register_event(evt)

    ########################################
    #
    ########################################
    def disconnect(self, evt, func = None):
        if evt not in self._listeners:
            return
        if func is None:
            self._listeners[evt] = []
        elif func in self._listeners[evt]:
            self._listeners[evt].remove(func)
        else:
            return
        if not self._listeners[evt]:
            self._unregister_event(evt)

    ########################################
    #
    ########################################
    def emit(self, evt, *args):
        if evt not in self._listeners:
            return
        res = None
        # We use a copy, in case the callback alters the list by removing itself from it(single-shot)
        listeners = list(self._listeners[evt])
        for func in listeners:
            r = func(self, *args)
            res = res or r
        return res

    ########################################
    #
    ########################################
    def expose(self, function_name, callback, timeout_ms = 0xFFFFFFFF, return_result = True):
        self._expose_callbacks[function_name] = callback
        js = f'chrome.webview.api._expose("{function_name}", [], {timeout_ms}, {int(return_result)});'
        self._frame.ExecuteScript(js, None)

    ########################################
    #
    ########################################
    def execute_js(self, js, callback = None):
        self._frame.ExecuteScript(
            js,
            ExecuteScriptCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def _register_event(self, evt):
        if evt in self._handlers:
            return

        if evt == EVENT.CONTENT_LOADING:
            self._handlers[evt] = FrameContentLoadingEventHandler(self._on_content_loading)
            self._tokens[evt] = self._frame.add_NavigationCompleted(self._handlers[evt].interface())

        elif evt == EVENT.DOM_CONTENT_LOADED:
            self._handlers[EVENT.DOM_CONTENT_LOADED] = FrameDOMContentLoadedEventHandler(self._on_dom_content_loaded)
            self._tokens[EVENT.DOM_CONTENT_LOADED] = self._frame.add_DOMContentLoaded(self._handlers[EVENT.DOM_CONTENT_LOADED].interface())

        elif evt == EVENT.FRAME_CREATED:
            self._handlers[evt] = FrameChildFrameCreatedEventHandler(self._on_frame_created)
            self._tokens[evt] = self._frame.add_FrameCreated(self._handlers[evt].interface())

        elif evt == EVENT.NAVIGATION_COMPLETED:
            self._handlers[evt] = FrameNavigationCompletedHandler(self._on_navigation_completed)
            self._tokens[evt] = self._frame.add_NavigationCompleted(self._handlers[evt].interface())

        elif evt == EVENT.NAVIGATION_STARTING:
            self._handlers[evt] = FrameNavigationStartingHandler(self._on_navigation_starting)
            self._tokens[evt] = self._frame.add_NavigationStarting(self._handlers[evt].interface())

        elif evt == EVENT.WEB_MESSAGE_RECEIVED:
            self._handlers[evt] = FrameWebMessageReceivedEventHandler(self._on_web_message_received)
            self._tokens[evt] = self._frame.add_WebMessageReceived(self._handlers[evt].interface())

        elif evt == EVENT.DOCUMENT_TITLE_CHANGED:
            self._handlers[evt] = FrameNameChangedEventHandler(self._on_document_title_changed)
            self._tokens[evt] = self._frame.add_NameChanged(self._handlers[evt].interface())

    ########################################
    #
    ########################################
    def _unregister_event(self, evt):

        if evt not in self._tokens:
            return

        if evt == EVENT.CONTENT_LOADING:
            self._frame.remove_ContentLoading(self._tokens[evt])

        elif evt == EVENT.DOM_CONTENT_LOADED:
            self._frame.remove_DOMContentLoaded(self._tokens[evt])

        elif evt == EVENT.FRAME_CREATED:
            self._frame.remove_FrameCreated(self._tokens[evt])

        elif evt == EVENT.NAVIGATION_COMPLETED:
            self._frame.remove_NavigationCompleted(self._tokens[evt])

        elif evt == EVENT.NAVIGATION_STARTING:
            self._frame.remove_NavigationStarting(self._tokens[evt])

        elif evt == EVENT.WEB_MESSAGE_RECEIVED:
            self._frame.remove_WebMessageReceived(self._tokens[evt])

        elif evt == EVENT.DOCUMENT_TITLE_CHANGED:
            self._frame.remove_NameChanged(self._tokens[evt])

        del self._tokens[evt]
        del self._handlers[evt]

    ########################################
    # Earliest moment when JS can be injected
    ########################################
    def _on_content_loading(self, sender, args):
        self.emit(EVENT.CONTENT_LOADING, args)

    ########################################
    #
    ########################################
    def _on_document_title_changed(self, sender, args):
        self.emit(EVENT.DOCUMENT_TITLE_CHANGED)

    ########################################
    #
    ########################################
    def _on_dom_content_loaded(self, sender, args):
        self.emit(EVENT.DOM_CONTENT_LOADED)

    ########################################
    #
    ########################################
    def _on_navigation_completed(self, sender, args):
        self.emit(EVENT.NAVIGATION_COMPLETED, args)

    ########################################
    #
    ########################################
    def _on_navigation_starting(self, sender, args):
        self.emit(EVENT.NAVIGATION_STARTING, args)

    ########################################
    #
    ########################################
    def _on_frame_created(self, sender, args):
        self.emit(EVENT.FRAME_CREATED, Frame(args.get_Frame().QueryInterface(ICoreWebView2Frame7)))

    ########################################
    #
    ########################################
    def _on_web_message_received(self, sender, args):
        data = json.loads(args.get_WebMessageAsJson())
        uid, func, args = data
        if func in self._expose_callbacks:
            res = self._expose_callbacks[func](*args)
            if res is not None:
                self._frame.PostWebMessageAsJson(json.dumps([id, res]))
        self.emit(EVENT.WEB_MESSAGE_RECEIVED, data)

########################################
#
########################################
class WebView2:

    environment = None
    environment_private = None
    profile_initialized = False

    ########################################
    #
    ########################################
    def __init__(
        self,
        parent_hwnd = None,
        url = None,
        html = None,
        left = 0, top = 0, width = 0, height = 0,
        is_private = False,
        is_hidden = False,
    ):
        # public
        self.webview_ready = False
        self.hwnd = None
        self.is_private = is_private

        self._controller = None
        self._webview = None
        self._url = url
        self._html = html
        self._parent_hwnd = parent_hwnd
        self._listeners = {}
        self._handlers = {}  # evt => handler
        self._tokens = {}  # evt => token
        self._expose_callbacks = {}  # evt => [callbacks...]

        self._init_rect = RECT(left, top, left + width, top + height)
        self._init_hidden = is_hidden
        self._init_suspended = False
        self._init_js = API_JS
        self._init_events = []
        self._init_vhosts = []
        self._init_focus = False
        self._init_muted = False

        self._current_request_filter = ('*', WEB_RESOURCE_CONTEXT.ALL)

        if WebView2.environment is None:
            LOADER.CreateEnvironmentWithOptions(
                SETTINGS.BROWSER_EXECUTABLE_FOLDER,
                SETTINGS.USER_DATA_FOLDER,
                SETTINGS.ADDITIONAL_BROWSER_ARGUMENTS,
                SETTINGS.LANGUAGE,
                SETTINGS.BROWSER_EXTENSIONS_ENABLED,
                CreateCoreWebView2EnvironmentCompletedHandler(self._on_environment_created).interface()
            )
        else:
            options = WebView2.environment.CreateCoreWebView2ControllerOptions().QueryInterface(ICoreWebView2ControllerOptions4)
            if self.is_private:
                options.put_IsInPrivateModeEnabled(1)

            options.put_AllowHostInputProcessing(int(SETTINGS.ALLOW_HOST_INPUT_PROCESSING))

            WebView2.environment.CreateCoreWebView2ControllerWithOptions(
                self._parent_hwnd,
                options,
                CreateCoreWebView2ControllerCompletedHandler(self._on_webview_ready).interface()
            )

    ########################################
    #
    ########################################
    def close(self):
        events = list(self._handlers.keys())
        for evt in events:
            self.disconnect(evt)
        if self._controller:
            self._controller.Close()
            self._controller = None

    ########################################
    #
    ########################################
    def connect(self, evt, func):
        if evt not in self._listeners:
            self._listeners[evt] = []
        elif func in self._listeners[evt]:
            return
        init_event = not self._listeners[evt]
        self._listeners[evt].append(func)
        if init_event:
            if evt == EVENT.FILES_DROPPED:
                if self._webview:
                    self.execute_js(DROP_INIT_JS.format(SETTINGS.FILE_DROP_SELECTOR))
                else:
                    self.add_script_to_execute_on_document_created(DROP_INIT_JS.format(SETTINGS.FILE_DROP_SELECTOR))
            else:
                self._register_event(evt)

    ########################################
    #
    ########################################
    def disconnect(self, evt, func = None):
        if evt not in self._listeners:
            return
        if func is None:
            self._listeners[evt] = []
        elif func in self._listeners[evt]:
            self._listeners[evt].remove(func)
        else:
            return
        if not self._listeners[evt]:
            if evt == EVENT.FILES_DROPPED:
                if self._webview:
                    self.execute_js(DROP_EXIT_JS.format(SETTINGS.FILE_DROP_SELECTOR))
                else:
                    self.add_script_to_execute_on_document_created(DROP_EXIT_JS.format(SETTINGS.FILE_DROP_SELECTOR))
            else:
                if self._webview:
                    self._unregister_event(evt)
                else:
                    self._init_events.remove(evt)

    ########################################
    #
    ########################################
    def emit(self, evt, *args):
        if evt not in self._listeners:
            return
        res = None

        # We use a copy, in case the callback alters the list by removing itself from it(single-shot)
        listeners = list(self._listeners[evt])
        for func in listeners:
            r = func(self, *args)
            res = res or r
        return res

    ########################################
    #
    ########################################
    def _register_event(self, evt):

        if self._webview is None:
            self._init_events.append(evt)
            return

        if evt in self._handlers:
            return

        if evt == EVENT.ACCELERATOR_KEY_PRESSED:
            self._handlers[evt] = AcceleratorKeyPressedEventHandler(self._on_accelerator_key_pressed)
            self._tokens[evt] = self._controller.add_AcceleratorKeyPressed(self._handlers[evt].interface())

        elif evt == EVENT.CONTAINS_FULLSCREEN_ELEMENT_CHANGED:
            self._handlers[evt] = ContainsFullScreenElementChangedEventHandler(self._on_contains_fullscreen_element_changed)
            self._tokens[evt] = self._webview.add_ContainsFullScreenElementChanged(self._handlers[evt].interface())

        elif evt == EVENT.CONTENT_LOADING:
            self._handlers[evt] = ContentLoadingEventHandler(self._on_content_loading)
            self._tokens[evt] = self._webview.add_ContentLoading(self._handlers[evt].interface())

        elif evt == EVENT.CONTEXT_MENU_REQUESTED:
            self._handlers[evt] = ContextMenuRequestedEventHandler(self._on_context_menu_requested)
            self._tokens[evt] = self._webview.add_ContextMenuRequested(self._handlers[evt].interface())

        elif evt == EVENT.DOCUMENT_TITLE_CHANGED:
            self._handlers[evt] = DocumentTitleChangedEventHandler(self._on_document_title_changed)
            self._tokens[evt] = self._webview.add_DocumentTitleChanged(self._handlers[evt].interface())

        elif evt == EVENT.DOM_CONTENT_LOADED:
            self._handlers[evt] = DOMContentLoadedEventHandler(self._on_dom_content_loaded)
            self._tokens[evt] = self._webview.add_DOMContentLoaded(self._handlers[evt].interface())

        elif evt == EVENT.DOWNLOAD_STARTING:
            self._handlers[evt] = DownloadStartingEventHandler(self._on_download_starting)
            self._tokens[evt] = self._webview.add_DownloadStarting(self._handlers[evt].interface())

        elif evt == EVENT.FAVICON_CHANGED:
            self._handlers[evt] = FaviconChangedEventHandler(self._on_favicon_changed)
            self._tokens[evt] = self._webview.add_FaviconChanged(self._handlers[evt].interface())

        elif evt == EVENT.FOCUS_LOST:
            self._handlers[evt] = FocusChangedEventHandler(self._on_focus_lost)
            self._tokens[evt] = self._controller.add_LostFocus(self._handlers[evt].interface())

        elif evt == EVENT.FRAME_CREATED:
            self._handlers[evt] = FrameCreatedEventHandler(self._on_frame_created)
            self._tokens[evt] = self._webview.add_FrameCreated(self._handlers[evt].interface())

        elif evt == EVENT.HISTORY_CHANGED:
            self._handlers[evt] = HistoryChangedEventHandler(self._on_history_changed)
            self._tokens[evt] = self._webview.add_HistoryChanged(self._handlers[evt].interface())

        elif evt == EVENT.NAVIGATION_COMPLETED:
            self._handlers[evt] = NavigationCompletedEventHandler(self._on_navigation_completed)
            self._tokens[evt] = self._webview.add_NavigationCompleted(self._handlers[evt].interface())

        elif evt == EVENT.NAVIGATION_STARTING:
            self._handlers[evt] = NavigationStartingEventHandler(self._on_navigation_starting)
            self._tokens[evt] = self._webview.add_NavigationStarting(self._handlers[evt].interface())

        elif evt == EVENT.NEW_WINDOW_REQUESTED:
            self._handlers[evt] = NewWindowRequestedEventHandler(self._on_new_window_requested)
            self._tokens[evt] = self._webview.add_NewWindowRequested(self._handlers[evt].interface())

        elif evt == EVENT.PERMISSION_REQUESTED:
            self._handlers[evt] = PermissionRequestedEventHandler(self._on_permission_requested)
            self._tokens[evt] = self._webview.add_PermissionRequested(self._handlers[evt].interface())

        elif evt == EVENT.SOURCE_CHANGED:
            self._handlers[evt] = SourceChangedEventHandler(self._on_source_changed)
            self._tokens[evt] = self._webview.add_SourceChanged(self._handlers[evt].interface())

        elif evt == EVENT.STATUS_BAR_TEXT_CHANGED:
            self._handlers[evt] = StatusBarTextChangedEventHandler(self._on_status_bar_text_changed)
            self._tokens[evt] = self._webview.add_StatusBarTextChanged(self._handlers[evt].interface())

        elif evt == EVENT.WEB_MESSAGE_RECEIVED:
            self._handlers[evt] = WebMessageReceivedEventHandler(self._on_web_message_received)
            self._tokens[evt] = self._webview.add_WebMessageReceived(self._handlers[evt].interface())

        elif evt == EVENT.WEB_RESOURCE_REQUESTED:
            self._webview.AddWebResourceRequestedFilter(*self._current_request_filter)
            self._handlers[evt] = WebResourceRequestedEventHandler(self._on_web_resource_requested)
            self._tokens[evt] = self._webview.add_WebResourceRequested(self._handlers[evt].interface())

        elif evt == EVENT.WEB_RESOURCE_RESPONSE_RECEIVED:
            self._handlers[evt] = WebResourceResponseReceivedEventHandler(self._on_web_resource_response_received)
            self._tokens[evt] = self._webview.add_WebResourceResponseReceived(self._handlers[evt].interface())

    ########################################
    #
    ########################################
    def _unregister_event(self, evt):

        if evt not in self._tokens:
            return

        if evt == EVENT.ACCELERATOR_KEY_PRESSED:
             self._controller.remove_AcceleratorKeyPressed(self._tokens[evt])

        elif evt == EVENT.CONTAINS_FULLSCREEN_ELEMENT_CHANGED:
           self._webview.remove_ContainsFullScreenElementChanged(self._tokens[evt])

        elif evt == EVENT.CONTENT_LOADING:
            self._webview.remove_ContentLoading(self._tokens[evt])

        elif evt == EVENT.CONTEXT_MENU_REQUESTED:
            self._webview.remove_ContextMenuRequested(self._tokens[evt])

        elif evt == EVENT.DOCUMENT_TITLE_CHANGED:
            self._webview.remove_DocumentTitleChanged(self._tokens[evt])

        elif evt == EVENT.DOM_CONTENT_LOADED:
            self._webview.remove_DOMContentLoaded(self._tokens[evt])

        elif evt == EVENT.DOWNLOAD_STARTING:
            self._webview.remove_DownloadStarting(self._tokens[evt])

        elif evt == EVENT.FAVICON_CHANGED:
            self._webview.remove_FaviconChanged(self._tokens[evt])

        elif evt == EVENT.FOCUS_LOST:
            self._controller.remove_LostFocus(self._tokens[evt])

        elif evt == EVENT.FRAME_CREATED:
            self._webview.remove_FrameCreated(self._tokens[evt])

        elif evt == EVENT.HISTORY_CHANGED:
            self._webview.remove_HistoryChanged(self._tokens[evt])

        elif evt == EVENT.NAVIGATION_COMPLETED:
            self._webview.remove_NavigationCompleted(self._tokens[evt])

        elif evt == EVENT.NAVIGATION_STARTING:
            self._webview.remove_FrameNavigationStarting(self._tokens[evt])

        elif evt == EVENT.NEW_WINDOW_REQUESTED:
            self._webview.remove_NewWindowRequested(self._tokens[evt])

        elif evt == EVENT.PERMISSION_REQUESTED:
            self._webview.remove_PermissionRequested(self._tokens[evt])

        elif evt == EVENT.SOURCE_CHANGED:
            self._webview.remove_SourceChanged(self._tokens[evt])

        elif evt == EVENT.STATUS_BAR_TEXT_CHANGED:
            self._webview.remove_StatusBarTextChanged(self._tokens[evt])

        elif evt == EVENT.WEB_MESSAGE_RECEIVED:
            self._webview.remove_WebMessageReceived(self._tokens[evt])

        elif evt == EVENT.WEB_RESOURCE_REQUESTED:
            self._webview.remove_WebResourceRequested(self._tokens[evt])

        elif evt == EVENT.WEB_RESOURCE_RESPONSE_RECEIVED:
            self._webview.remove_WebResourceResponseReceived(self._tokens[evt])

        del self._tokens[evt]
        del self._handlers[evt]

    ########################################
    #
    ########################################
    def _on_environment_created(self, error_code, environment):

        WebView2.environment = environment.QueryInterface(ICoreWebView2Environment15)

        options = WebView2.environment.CreateCoreWebView2ControllerOptions().QueryInterface(ICoreWebView2ControllerOptions4)
        if self.is_private:
            options.put_IsInPrivateModeEnabled(1)

        options.put_AllowHostInputProcessing(int(SETTINGS.ALLOW_HOST_INPUT_PROCESSING))

        WebView2.environment.CreateCoreWebView2ControllerWithOptions(
            self._parent_hwnd,
            options,
            CreateCoreWebView2ControllerCompletedHandler(self._on_webview_ready).interface()
        )

    ########################################
    #
    ########################################
    def _on_webview_ready(self, sender, args):
        self._controller = args

        webview = self._controller.get_CoreWebView2().QueryInterface(ICoreWebView2_28)  # ICoreWebView2_25
        self._webview = webview

#        if not WebView2.profile_initialized and SETTINGS.COLOR_SCHEME is not None:
#            webview_profile = self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7)
#            webview_profile.put_PreferredColorScheme(SETTINGS.COLOR_SCHEME)
#            WebView2.profile_initialized = True
#
#        self.hwnd = user32.FindWindowExW(self._parent_hwnd, None, 'Chrome_WidgetWin_0', None)

        if self._init_hidden:
            self._controller.put_IsVisible(0)

        self._controller.put_Bounds(self._init_rect)

        settings = webview.get_Settings().QueryInterface(ICoreWebView2Settings6)

        settings.put_IsScriptEnabled(TRUE)
        settings.put_IsWebMessageEnabled(TRUE)

        if SETTINGS.DEFAULT_CONTEXT_MENUS_ENABLED is not None:
            settings.put_AreDefaultContextMenusEnabled(int(SETTINGS.DEFAULT_CONTEXT_MENUS_ENABLED))
        if SETTINGS.DEFAULT_SCRIPT_DIALOGS_ENABLED is not None:
            settings.put_AreDefaultScriptDialogsEnabled(int(SETTINGS.DEFAULT_SCRIPT_DIALOGS_ENABLED))
        if SETTINGS.DEV_TOOLS_ENABLED is not None:
            settings.put_AreDevToolsEnabled(int(SETTINGS.DEV_TOOLS_ENABLED))
        if SETTINGS.ARE_HOST_OBJECTS_ALLOWED is not None:
            settings.put_AreHostObjectsAllowed(int(SETTINGS.ARE_HOST_OBJECTS_ALLOWED))
        if SETTINGS.STATUS_BAR_ENABLED is not None:
            settings.put_IsStatusBarEnabled(int(SETTINGS.STATUS_BAR_ENABLED))
        if SETTINGS.ZOOM_CONTROL_ENABLED is not None:
            settings.put_IsZoomControlEnabled(int(SETTINGS.ZOOM_CONTROL_ENABLED))
        if SETTINGS.USER_AGENT is not None:
            settings.put_UserAgent(SETTINGS.USER_AGENT)  # ICoreWebView2Settings2
        if SETTINGS.BROWSER_ACCELERATOR_KEYS_ENABLED is not None:
            settings.put_AreBrowserAcceleratorKeysEnabled(SETTINGS.BROWSER_ACCELERATOR_KEYS_ENABLED)  # ICoreWebView2Settings3
        if SETTINGS.PASSWORD_AUTOSAVE_ENABLED is not None:
            settings.put_IsPasswordAutosaveEnabled(SETTINGS.PASSWORD_AUTOSAVE_ENABLED)  # ICoreWebView2Settings4
        if SETTINGS.GENERAL_AUTOFILL_ENABLED is not None:
            settings.put_IsGeneralAutofillEnabled(SETTINGS.GENERAL_AUTOFILL_ENABLED)  # ICoreWebView2Settings4
        if SETTINGS.PINCH_ZOOM_ENABLED is not None:
            settings.put_IsPinchZoomEnabled(SETTINGS.PINCH_ZOOM_ENABLED)  # ICoreWebView2Settings5
        if SETTINGS.SWIPE_NAVIGATION_ENABLED is not None:
            settings.put_IsSwipeNavigationEnabled(SETTINGS.SWIPE_NAVIGATION_ENABLED)  # ICoreWebView2Settings6

        webview.add_WebMessageReceived(
            WebMessageReceivedEventHandler(self._on_web_message_received).interface()
        )

        if self._init_js:
            # The script will be executed after the global object has been created but
            # before the HTML has been parsed and scripts included from the HTML will run.
            # THIS IS EXECUTED ALSO IN EVERY (I)FRAME
            webview.AddScriptToExecuteOnDocumentCreated(self._init_js, None)

        for evt in self._init_events:
            self._register_event(evt)

        for vhost in self._init_vhosts:
            self._webview.SetVirtualHostNameToFolderMapping(*vhost)

        if self._init_muted:
            self._webview.put_IsMuted(TRUE)

        if self._init_focus:
            self._controller.MoveFocus(0)

        self.webview_ready = True
        self.emit(EVENT.WEBVIEW_READY)

        # If both URL and HTML are specified, HTML takes precedence
        if self._html:
            webview.NavigateToString(self._html)
        elif self._url:
            webview.Navigate(self._url)
        else:
            webview.NavigateToString(DEFAULT_HTML)

        if self._init_suspended:
            self._webview.TrySuspend(None)

    ########################################
    #
    ########################################
    def _on_web_message_received(self, sender, args):
        data = json.loads(args.get_WebMessageAsJson())

        if data[0] == 'files_dropped':
            additionalObjects = args.get_AdditionalObjects()
            files = [additionalObjects.GetValueAtIndex(i).get_Path() for i in range(additionalObjects.get_Count())]
            self._on_files_dropped(files, data[1])
        else:
            uid, func, args = data
            if func in self._expose_callbacks:
                res = self._expose_callbacks[func](*args)
                if res is not None:
                    self._webview.PostWebMessageAsJson(json.dumps([id, res]))

        self.emit(EVENT.WEB_MESSAGE_RECEIVED, data)

    ########################################
    #
    ########################################
    def _on_accelerator_key_pressed(self, sender, args):
        self.emit(EVENT.ACCELERATOR_KEY_PRESSED, args)

    ########################################
    #
    ########################################
    def _on_contains_fullscreen_element_changed(self, sender, args):
        self.emit(EVENT.CONTAINS_FULLSCREEN_ELEMENT_CHANGED, args)

    ########################################
    # Earliest moment when JS can be injected
    ########################################
    def _on_content_loading(self, sender, args):
        self.emit(EVENT.CONTENT_LOADING, args)

    ########################################
    #
    ########################################
    def _on_context_menu_requested(self, sender, args):
        self.emit(EVENT.CONTEXT_MENU_REQUESTED, args)

    ########################################
    #
    ########################################
    def _on_document_title_changed(self, sender, args):
        self.emit(EVENT.DOCUMENT_TITLE_CHANGED)

    ########################################
    #
    ########################################
    def _on_dom_content_loaded(self, sender, args):
        self.emit(EVENT.DOM_CONTENT_LOADED)

    ########################################
    # args: ICoreWebView2DownloadStartingEventArgs
    ########################################
    def _on_download_starting(self, sender, args):
        self.emit(EVENT.DOWNLOAD_STARTING, args)

    ########################################
    #
    ########################################
    def _on_favicon_changed(self, sender, args):
        self.emit(EVENT.FAVICON_CHANGED)

    ########################################
    #
    ########################################
    def _on_files_dropped(self, files, target_id):
        self.emit(EVENT.FILES_DROPPED, files, target_id)

    ########################################
    #
    ########################################
    def _on_focus_lost(self, sender, args):
        self.emit(EVENT.FOCUS_LOST)

    ########################################
    #
    ########################################
    def _on_frame_created(self, sender, args):
        self.emit(EVENT.FRAME_CREATED, Frame(args.get_Frame().QueryInterface(ICoreWebView2Frame7)))

    ########################################
    #
    ########################################
#    def _on_frame_navigation_completed(self, sender, args):
#        self.emit(EVENT.FRAME_NAVIGATION_COMPLETED, args)

    ########################################
    #
    ########################################
#    def _on_frame_navigation_starting(self, sender, args):
#        self.emit(EVENT.FRAME_NAVIGATION_STARTING, args)

    ########################################
    #
    ########################################
    def _on_history_changed(self,  sender, args):
        self.emit(EVENT.HISTORY_CHANGED)

    ########################################
    #
    ########################################
    def _on_navigation_completed(self, sender, args):
        self.emit(EVENT.NAVIGATION_COMPLETED, args)

    ########################################
    #
    ########################################
    def _on_navigation_starting(self, sender, args):
        self.emit(EVENT.NAVIGATION_STARTING, args)

    ########################################
    #
    ########################################
    def _on_new_window_requested(self, sender, args):
        self.emit(EVENT.NEW_WINDOW_REQUESTED, args)

    ########################################
    #
    ########################################
    def _on_permission_requested(self, sender, args):
        self.emit(EVENT.PERMISSION_REQUESTED, args)

    ########################################
    #
    ########################################
    def _on_source_changed(self, sender, args):
        self.emit(EVENT.SOURCE_CHANGED, args.get_IsNewDocument())

    ########################################
    #
    ########################################
    def _on_status_bar_text_changed(self, sender, args):
        self.emit(EVENT.STATUS_BAR_TEXT_CHANGED)

    ########################################
    #
    ########################################
    def _on_web_resource_requested(self, sender, args):
        request = args.get_Request()
        headers = request.get_Headers()

        headers_dict = Headers()
        it = headers.GetIterator()
        while it.get_HasCurrentHeader():
            k, v = it.GetCurrentHeader()
            headers_dict[k] = v
            it.MoveNext()

        url = request.get_Uri()
        method = request.get_Method()

        request_obj = Request(url, method, Headers(headers_dict))

        self.emit(EVENT.WEB_RESOURCE_REQUESTED, request_obj)

        if request_obj.url != url:
            request.put_Uri(request_obj.url)

        if request_obj.method != method:
            request.put_Method(request_obj.method)

        for k in request_obj.headers._edited:
            headers.SetHeader(k, request_obj.headers[k])

        for k in request_obj.headers._deleted:
            headers.RemoveHeader(k)

    ########################################
    #
    ########################################
    def _on_web_resource_response_received(self, sender, args):
        response_view = args.get_Response()
        headers = {}
        it = response_view.get_Headers().GetIterator()
        while it.get_HasCurrentHeader():
            k, v = it.GetCurrentHeader()
            headers[k] = v
            it.MoveNext()

        self.emit(EVENT.WEB_RESOURCE_RESPONSE_RECEIVED, Response(
            args.get_Request().get_Uri(),
            response_view.get_StatusCode(),
            headers
        ))

    ########################################
    #
    ########################################
    def add_script_to_execute_on_document_created(self, js, callback = None):
        if self._webview:
            self._webview.AddScriptToExecuteOnDocumentCreated(
                js,
                AddScriptToExecuteOnDocumentCreatedCompletedHandler(callback).interface() if callback else None
            )
        else:
            if not js.endswith(';'):
                js += ';'
            self._init_js += js

    ########################################
    #
    ########################################
    def remove_script_to_execute_on_document_created(self, script_id):
        if self._webview:
            self._webview.RemoveScriptToExecuteOnDocumentCreated(script_id)

    ########################################
    #
    ########################################
    def profile_apply_theme(self, preferred_color_scheme):
        if self._webview is None:
            raise WebviewNotReadyException()

        webview_profile = self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7)
        webview_profile.put_PreferredColorScheme(preferred_color_scheme)

    ########################################
    #
    ########################################
    def capture(self, image_format, istream, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.CapturePreview(
            image_format,
            istream,
            CapturePreviewCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def execute_js(self, js, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.ExecuteScript(
            js,
            ExecuteScriptCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def execute_js_with_result(self, js, callback):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.ExecuteScriptWithResult(
            js,
            ExecuteScriptWithResultCompletedHandler(callback).interface()
        )

    ########################################
    #
    ########################################
    def resolve_js(self, js, callback):
        if self._webview is None:
            raise WebviewNotReadyException()

        func_name = f'cb{time.time_ns()}'

        ########################################
        #
        ########################################
        def _on_resolve(res):
            callback(res)
            del self._expose_callbacks[func_name]

        self._expose_callbacks[func_name] = _on_resolve
        self._webview.ExecuteScript(f'chrome.webview.api._resolve("{func_name}", function(){{return {js}}});', None)

    ########################################
    #
    ########################################
    def expose(self, function_name, callback, timeout_ms = 0xFFFFFFFF, return_result = True):
        self._expose_callbacks[function_name] = callback
        js = f'chrome.webview.api._expose("{function_name}", [], {timeout_ms}, {int(return_result)});'
        if self._webview:
            self._webview.ExecuteScript(js, None)
        else:
            self._init_js += js

    ########################################
    #
    ########################################
    def unexpose(self, function_name):
        del self._expose_callbacks[function_name]
        self._webview.ExecuteScript(f'delete chrome.webview.api.{function_name}', None)

    ########################################
    #
    ########################################
    def delete_all_cookies(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_CookieManager().DeleteAllCookies()

    ########################################
    #
    ########################################
    def get_can_go_back(self):
        return bool(self._webview.get_CanGoBack()) if self._webview else False

    ########################################
    #
    ########################################
    def get_can_go_forward(self):
        return bool(self._webview.get_CanGoForward()) if self._webview else False

    ########################################
    # Return a list of all the cookies set for the current website
    ########################################
    def get_cookies(self, callback):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_CookieManager().GetCookies(
            self._webview.get_Source(),
            GetCookiesCompletedHandler(callback).interface()
        )

    ########################################
    #
    ########################################
    def get_document_title(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return self._webview.get_DocumentTitle()

    ########################################
    #
    ########################################
    def get_favicon_stream(self, image_format, callback):
        if self._webview is None:
            raise WebviewNotReadyException()

        handler = GetFaviconCompletedHandler(callback)
        self._webview.GetFavicon(
            image_format,
            handler.interface()
        )

    ########################################
    #
    ########################################
    def get_favicon_url(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return self._webview.get_FaviconUri()

    ########################################
    #
    ########################################
    def get_find(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return self._webview.get_Find()

    ########################################
    #
    ########################################
    def get_settings(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return self._webview.get_Settings().QueryInterface(ICoreWebView2Settings6)

    ########################################
    #
    ########################################
    def get_status_bar_text(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return self._webview.get_StatusBarText()

    ########################################
    #
    ########################################
    def get_url(self):
        if self._webview:
            return self._webview.get_Source()
        else:
            return self._url

    ########################################
    #
    ########################################
    def get_is_playing_audio(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return bool(self._webview.get_IsDocumentPlayingAudio())

    ########################################
    #
    ########################################
    def get_is_muted(self):
        if self._webview:
            return bool(self._webview.get_IsMuted())
        else:
            return self._init_muted

    ########################################
    #
    ########################################
    def put_is_muted(self, value):
        if self._webview:
            self._webview.put_IsMuted(int(value))
        else:
            self._init_muted = value

    ########################################
    #
    ########################################
    def get_is_suspended(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        return bool(self._webview.get_IsSuspended())

    ########################################
    #
    ########################################
    def go_back(self, num_pages = 1):
        if self._webview is None:
            raise WebviewNotReadyException()

        for i in range(num_pages):
            self._webview.GoBack()

    ########################################
    #
    ########################################
    def go_forward(self, num_pages = 1):
        if self._webview is None:
            raise WebviewNotReadyException()

        for i in range(num_pages):
            self._webview.GoForward()

    ########################################
    #
    ########################################
    def load_html(self, html):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.NavigateToString(html)

    ########################################
    #
    ########################################
    def load_url(self, url):
        if self._webview is None:
            self._url = url
            return

        self._webview.Navigate(url)

    ########################################
    #
    ########################################
    def open_dev_tools(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.OpenDevToolsWindow()

    ########################################
    #
    ########################################
    def open_task_manager(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.OpenTaskManagerWindow()

    ########################################
    #
    ########################################
    def print(self, printSettings = None, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.Print(
            printSettings,
            PrintCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def print_to_pdf(self, pdf_file, printSettings = None, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.PrintToPdf(
            pdf_file,
            printSettings,
            PrintToPdfCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def show_print_ui(self, dialog_kind = PRINT_DIALOG_KIND.BROWSER):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.ShowPrintUI(dialog_kind)

    ########################################
    #
    ########################################
    def profile_add_browser_extension(self, extension_folder, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7).AddBrowserExtension(
            extension_folder,
            AddBrowserExtensionCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def profile_clear_browsing_data(self, kinds, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile2).ClearBrowsingData(
            kinds,
            ClearBrowsingDataCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def profile_clear_browsing_data_all(self, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile2).ClearBrowsingDataAll(
            ClearBrowsingDataCompletedHandler(callback).interface() if callback else None
        )

    ########################################
    #
    ########################################
    def profile_enable_browser_extension(self, extension_id, is_enabled, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        ########################################
        #
        ########################################
        def _on_browser_extensions_received(error_code, args):
            found = False
            if error_code == 0:
                for i in range(args.get_Count()):
                    ex = args.GetValueAtIndex(i)
                    if ex.get_Id() == extension_id:
                        ex.Enable(int(is_enabled), BrowserExtensionEnableCompletedHandler(callback).interface() if callback else None)
                        found = True
                        break
            if callback and not found:
                callback(-1)

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7).GetBrowserExtensions(
            GetBrowserExtensionsCompletedHandler(_on_browser_extensions_received).interface()
        )

    ########################################
    #
    ########################################
    def profile_get_browser_extensions(self, callback):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7).GetBrowserExtensions(
            GetBrowserExtensionsCompletedHandler(callback).interface()
        )

    ########################################
    #
    ########################################
    def profile_remove_browser_extension(self, extension_id, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        ########################################
        #
        ########################################
        def _on_browser_extensions_received(error_code, args):
            found = False
            if error_code == 0:
                for i in range(args.get_Count()):
                    ex = args.GetValueAtIndex(i)
                    if ex.get_Id() == extension_id:
                        ex.Remove(BrowserExtensionRemoveCompletedHandler(callback).interface() if callback else None)
                        found = True
                        break

            if callback and not found:
                callback(-1)

        self._webview.get_Profile().QueryInterface(ICoreWebView2Profile7).GetBrowserExtensions(
             GetBrowserExtensionsCompletedHandler(_on_browser_extensions_received).interface()
        )

    ########################################
    #
    ########################################
    def reload(self):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.Reload()

    ########################################
    #
    ########################################
    def set_focus(self):
        if self._controller:
            self._controller.MoveFocus(0)
        else:
            self._init_focus = True

    ########################################
    #
    ########################################
    def set_virtual_host_name_to_folder_mapping(self, host_name, folder_path, access_kind = HOST_RESOURCE_ACCESS_KIND.ALLOW):
        if self._webview:
            self._webview.SetVirtualHostNameToFolderMapping(host_name, folder_path, access_kind)
        else:
            self._init_vhosts.append((host_name, folder_path, access_kind))

    ########################################
    #
    ########################################
    def set_visible(self, is_visible, suspend = False):
        if self._controller:

            self._controller.put_IsVisible(int(is_visible))

            if not is_visible and suspend:
                self._webview.TrySuspend(None)

        else:
            self._init_hidden = not is_visible
            if not is_visible and suspend:
                self._init_suspended = True

    ########################################
    #
    ########################################
    def set_web_resource_requested_filter(self, uri: str, context: int) -> None:
        if EVENT.WEB_RESOURCE_REQUESTED in self._tokens:
            self._webview.RemoveWebResourceRequestedFilter(*self._current_request_filter)
        self._current_request_filter = (uri, context)
        if EVENT.WEB_RESOURCE_REQUESTED in self._tokens:
            self._webview.AddWebResourceRequestedFilter(*self._current_request_filter)

    ########################################
    #
    ########################################
    def put_bounds(self, rc):
        if self._controller:
            self._controller.put_Bounds(rc)
        else:
            self._init_rect = rc

    ########################################
    #
    ########################################
    def get_bounds(self):
        if self._controller:
            return self._controller.get_Bounds()
        else:
            return self._init_rect

    ########################################
    #
    ########################################
    def put_zoom_factor(self, zoom):
        if self._controller:
            self._controller.put_ZoomFactor(zoom)

    ########################################
    #
    ########################################
    def show_save_as_ui(self, callback = None):
        if self._webview is None:
            raise WebviewNotReadyException()

        self._webview.ShowSaveAsUI(
            ShowSaveAsUICompletedHandler(callback).interface() if callback else None
        )
