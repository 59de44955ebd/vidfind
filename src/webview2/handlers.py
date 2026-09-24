import traceback
from .interfaces import *


########################################
#
########################################
class _Handler(object):

    def __init__(self, callback):
        self.callback = callback

    def __del__(self):
        self.IUnknown_Release(self)

    def Invoke(self, this, sender, args = None):
        try:
            self.callback(sender, args)
        except:
            traceback.print_exc()

    def interface(self):
        obj = cast(self._com_pointers_[self._com_interfaces_[0]._iid_], POINTER(self._com_interfaces_[0]))
        obj.AddRef()
        return obj


########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(ICoreWebView2Environment), 'result' )),
########################################
class CreateCoreWebView2EnvironmentCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(ICoreWebView2Controller), 'result' )),
########################################
class CreateCoreWebView2ControllerCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2CreateCoreWebView2ControllerCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Controller), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2AcceleratorKeyPressedEventArgs), 'args' )),
########################################
class AcceleratorKeyPressedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2AcceleratorKeyPressedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(ICoreWebView2BrowserExtension), 'result' )),
########################################
class AddBrowserExtensionCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ProfileAddBrowserExtensionCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], LPCWSTR, 'result' )),
########################################
class AddScriptToExecuteOnDocumentCreatedCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' )),
########################################
class BrowserExtensionEnableCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2BrowserExtensionEnableCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' )),
########################################
class BrowserExtensionRemoveCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2BrowserExtensionRemoveCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], LPCWSTR, 'result' )),
########################################
class CallDevToolsProtocolMethodCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2CallDevToolsProtocolMethodCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' )),
########################################
class CapturePreviewCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2CapturePreviewCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class ContainsFullScreenElementChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ContainsFullScreenElementChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2ContentLoadingEventArgs), 'args' )),
########################################
class ContentLoadingEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ContentLoadingEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2ContextMenuRequestedEventArgs), 'args' )),
########################################
class ContextMenuRequestedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ContextMenuRequestedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2ContextMenuItem), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class CustomItemSelectedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2CustomItemSelectedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class DocumentTitleChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2DocumentTitleChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2DOMContentLoadedEventArgs), 'args' )),
########################################
class DOMContentLoadedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2DOMContentLoadedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2DownloadStartingEventArgs), 'args' )),
########################################
class DownloadStartingEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2DownloadStartingEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2DownloadOperation), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class BytesReceivedChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2BytesReceivedChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' )),
########################################
class ClearBrowsingDataCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ClearBrowsingDataCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], LPCWSTR, 'result' )),
########################################
class ExecuteScriptCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ExecuteScriptCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(ICoreWebView2ExecuteScriptResult), 'result' )),
########################################
class ExecuteScriptWithResultCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ExecuteScriptWithResultCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class FaviconChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FaviconChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Controller), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class FocusChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FocusChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2FrameCreatedEventArgs), 'args' )),
########################################
class FrameChildFrameCreatedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameChildFrameCreatedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2ContentLoadingEventArgs), 'args' )),
########################################
class FrameContentLoadingEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameContentLoadingEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2FrameCreatedEventArgs), 'args' )),
########################################
class FrameCreatedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameCreatedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2DOMContentLoadedEventArgs), 'args' )),
########################################
class FrameDOMContentLoadedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameDOMContentLoadedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class FrameNameChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameNameChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventArgs), 'args' )),
########################################
class FrameNavigationCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameNavigationCompletedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventArgs), 'args' )),
########################################
class FrameNavigationStartingHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameNavigationStartingEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2WebMessageReceivedEventArgs), 'args' )),
########################################
class FrameWebMessageReceivedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2FrameWebMessageReceivedEventHandler]

########################################
#
########################################
class GetBrowserExtensionsCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ProfileGetBrowserExtensionsCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(ICoreWebView2CookieList), 'result' )),
########################################
class GetCookiesCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2GetCookiesCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], POINTER(IStream), 'result' )),
########################################
class GetFaviconCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2GetFaviconCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class HistoryChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2HistoryChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventArgs), 'args' )),
########################################
class NavigationCompletedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2NavigationCompletedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventArgs), 'args' )),
########################################
class NavigationStartingEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2NavigationStartingEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2NewWindowRequestedEventArgs), 'args' )),
########################################
class NewWindowRequestedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2NewWindowRequestedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2PermissionRequestedEventArgs), 'args' )),
########################################
class PermissionRequestedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2PermissionRequestedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], INT, 'result' )),  # COREWEBVIEW2_PRINT_STATUS
########################################
class PrintCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2PrintCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], LPBOOL, 'result' )),
########################################
class PrintToPdfCompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2PrintToPdfCompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2Environment), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class ProcessInfosChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ProcessInfosChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], HRESULT, 'errorCode' ),
#        ( ['in'], COREWEBVIEW2_SAVE_AS_UI_RESULT, 'result' )),
########################################
class ShowSaveAsUICompletedHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2ShowSaveAsUICompletedHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2SourceChangedEventArgs), 'args' )),
########################################
class SourceChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2SourceChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2DownloadOperation), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class StateChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2StateChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(IUnknown), 'args' )),
########################################
class StatusBarTextChangedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2StatusBarTextChangedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2WebMessageReceivedEventArgs2), 'args' )),
########################################
class WebMessageReceivedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2WebMessageReceivedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2WebResourceRequestedEventArgs), 'args' )),
########################################
class WebResourceRequestedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2WebResourceRequestedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2WebResourceResponseReceivedEventArgs), 'args' )),
########################################
class WebResourceResponseReceivedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2WebResourceResponseReceivedEventHandler]

########################################
#    COMMETHOD([], HRESULT, 'Invoke',
#        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
#        ( ['in'], POINTER(ICoreWebView2DevToolsProtocolEventReceivedEventArgs), 'args' )),
########################################
class DevToolsProtocolEventReceivedEventHandler(COMObject, _Handler):
    _com_interfaces_ = [ICoreWebView2DevToolsProtocolEventReceivedEventHandler]
