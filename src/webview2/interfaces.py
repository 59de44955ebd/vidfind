from ctypes import *
from ctypes.wintypes import *

from .comtypes import IUnknown, GUID, COMObject, COMMETHOD, HRESULT, IStream
from .comtypes.automation import VARIANT, IDispatch, VT_DISPATCH

INT64 = c_int64

UINT32 = c_uint32
UINT64 = c_uint64

########################################
# Structures
########################################

class EventRegistrationToken(Structure):
    _fields_ = [
        ('value', c_int64),
    ]

class COREWEBVIEW2_PHYSICAL_KEY_STATUS(Structure):
    _fields_ = [
        ('RepeatCount', UINT32),
        ('ScanCode', UINT32),
        ('IsExtendedKey', BOOL),
        ('IsMenuKeyDown', BOOL),
        ('WasKeyDown', BOOL),
        ('IsKeyReleased', BOOL),
    ]

########################################
# COM Classes
########################################

# Referenced but not implemented (yet)
ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler = LPVOID
ICoreWebView2FindActiveMatchIndexChangedEventHandler = LPVOID
ICoreWebView2FindMatchCountChangedEventHandler = LPVOID
ICoreWebView2FindStartCompletedHandler = LPVOID
ICoreWebView2FrameDestroyedEventHandler = LPVOID
ICoreWebView2IsDocumentPlayingAudioChangedEventHandler = LPVOID
ICoreWebView2IsMutedChangedEventHandler = LPVOID
ICoreWebView2MoveFocusRequestedEventHandler = LPVOID
ICoreWebView2NewBrowserVersionAvailableEventHandler = LPVOID
ICoreWebView2PrintToPdfStreamCompletedHandler = LPVOID
ICoreWebView2ProcessFailedEventHandler = LPVOID
ICoreWebView2SaveAsUIShowingEventHandler = LPVOID
ICoreWebView2ScriptDialogOpeningEventHandler = LPVOID
ICoreWebView2TrySuspendCompletedHandler = LPVOID
ICoreWebView2WindowFeatures = LPVOID
ICoreWebView2ZoomFactorChangedEventHandler = LPVOID

class ICoreWebView2(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{76eceacb-0462-4d94-ac83-423a6793775e}')
    _idlflags_ = []

class ICoreWebView2_2(ICoreWebView2):
    _case_insensitive_ = True
    _iid_ = GUID('{9E8F0CF8-E670-4B5E-B2BC-73E061E3184C}')
    _idlflags_ = []

class ICoreWebView2_3(ICoreWebView2_2):
    _case_insensitive_ = True
    _iid_ = GUID('{A0D6DF20-3B92-416D-AA0C-437A9C727857}')
    _idlflags_ = []

class ICoreWebView2_4(ICoreWebView2_3):
    _case_insensitive_ = True
    _iid_ = GUID('{20d02d59-6df2-42dc-bd06-f98a694b1302}')
    _idlflags_ = []

#class ICoreWebView2_5(ICoreWebView2_4):
#    _case_insensitive_ = True
#    _iid_ = GUID('{bedb11b8-d63c-11eb-b8bc-0242ac130003}')
#    _idlflags_ = []

class ICoreWebView2_6(ICoreWebView2_4):
    _case_insensitive_ = True
    _iid_ = GUID('{499aadac-d92c-4589-8a75-111bfc167795}')
    _idlflags_ = []

class ICoreWebView2_7(ICoreWebView2_6):
    _case_insensitive_ = True
    _iid_ = GUID('{79c24d83-09a3-45ae-9418-487f32a58740}')
    _idlflags_ = []

class ICoreWebView2_8(ICoreWebView2_7):
    _case_insensitive_ = True
    _iid_ = GUID('{E9632730-6E1E-43AB-B7B8-7B2C9E62E094}')
    _idlflags_ = []

#class ICoreWebView2_8(ICoreWebView2_7):
#    _case_insensitive_ = True
#    _iid_ = GUID('{E9632730-6E1E-43AB-B7B8-7B2C9E62E094}')
#    _idlflags_ = []
#
#class ICoreWebView2_9(ICoreWebView2_8):
#    _case_insensitive_ = True
#    _iid_ = GUID('{4d7b2eab-9fdc-468d-b998-a9260b5ed651}')
#    _idlflags_ = []
#
#class ICoreWebView2_10(ICoreWebView2_9):
#    _case_insensitive_ = True
#    _iid_ = GUID('{b1690564-6f5a-4983-8e48-31d1143fecdb}')
#    _idlflags_ = []

class ICoreWebView2_11(ICoreWebView2_8):
    _case_insensitive_ = True
    _iid_ = GUID('{0be78e56-c193-4051-b943-23b460c08bdb}')
    _idlflags_ = []

class ICoreWebView2_12(ICoreWebView2_11):
    _case_insensitive_ = True
    _iid_ = GUID('{35D69927-BCFA-4566-9349-6B3E0D154CAC}')
    _idlflags_ = []

class ICoreWebView2_13(ICoreWebView2_12):
    _case_insensitive_ = True
    _iid_ = GUID('{f75f09a8-667e-4983-88d6-c8773f315e84}')
    _idlflags_ = []

#class ICoreWebView2_14(ICoreWebView2_13):
#    _case_insensitive_ = True
#    _iid_ = GUID('{6daa4f10-4a90-4753-8898-77c5df534165}')
#    _idlflags_ = []

class ICoreWebView2_15(ICoreWebView2_13):
    _case_insensitive_ = True
    _iid_ = GUID('{517B2D1D-7DAE-4A66-A4F4-10352FFB9518}')
    _idlflags_ = []

class ICoreWebView2_16(ICoreWebView2_15):
    _case_insensitive_ = True
    _iid_ = GUID('{0EB34DC9-9F91-41E1-8639-95CD5943906B}')
    _idlflags_ = []

class ICoreWebView2_20(ICoreWebView2_16):
    _case_insensitive_ = True
    _iid_ = GUID('{b4bc1926-7305-11ee-b962-0242ac120002}')
    _idlflags_ = []

class ICoreWebView2_21(ICoreWebView2_20):
    _case_insensitive_ = True
    _iid_ = GUID('{c4980dea-587b-43b9-8143-3ef3bf552d95}')
    _idlflags_ = []

class ICoreWebView2_25(ICoreWebView2_21):
    _case_insensitive_ = True
    _iid_ = GUID('{b5a86092-df50-5b4f-a17b-6c8f8b40b771}')
    _idlflags_ = []


#    MIDL_INTERFACE("806268b8-f897-5685-88e5-c45fca0b1a48")
#    ICoreWebView2_26 : public ICoreWebView2_25
#    {
#    public:
#        virtual HRESULT STDMETHODCALLTYPE add_SaveFileSecurityCheckStarting(
#            /* [in] */ ICoreWebView2SaveFileSecurityCheckStartingEventHandler *eventHandler,
#            /* [out] */ EventRegistrationToken *token) = 0;
#
#        virtual HRESULT STDMETHODCALLTYPE remove_SaveFileSecurityCheckStarting(
#            /* [in] */ EventRegistrationToken token) = 0;
#
#    };


#    MIDL_INTERFACE("00fbe33b-8c07-517c-aa23-0ddd4b5f6fa0")
#    ICoreWebView2_27 : public ICoreWebView2_26
#    {
#    public:
#        virtual HRESULT STDMETHODCALLTYPE add_ScreenCaptureStarting(
#            /* [in] */ ICoreWebView2ScreenCaptureStartingEventHandler *eventHandler,
#            /* [out] */ EventRegistrationToken *token) = 0;
#
#        virtual HRESULT STDMETHODCALLTYPE remove_ScreenCaptureStarting(
#            /* [in] */ EventRegistrationToken token) = 0;
#
#    };


class ICoreWebView2_28(ICoreWebView2_25):
    _case_insensitive_ = True
    _iid_ = GUID('{62e50381-5bf5-51a8-aae0-f20a3a9c8a90}')
    _idlflags_ = []

class ICoreWebView2AcceleratorKeyPressedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9f760f8a-fb79-42be-9990-7b56900fa9c7}')
    _idlflags_ = []

class ICoreWebView2AcceleratorKeyPressedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{b29c7e28-fa79-41a8-8e44-65811c76dcb2}')
    _idlflags_ = []

class ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{b99369f3-9b11-47b5-bc6f-8e7895fcea17}')
    _idlflags_ = []

class ICoreWebView2BrowserExtension(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7EF7FFA0-FAC5-462C-B189-3D9EDBE575DA}')
    _idlflags_ = []

class ICoreWebView2BrowserExtensionEnableCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{30c186ce-7fad-421f-a3bc-a8eaf071ddb8}')
    _idlflags_ = []

class ICoreWebView2BrowserExtensionList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2ef3d2dc-bd5f-4f4d-90af-fd67798f0c2f}')
    _idlflags_ = []

class ICoreWebView2BrowserExtensionRemoveCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8e41909a-9b18-4bb1-8cdf-930f467a50be}')
    _idlflags_ = []

class ICoreWebView2BytesReceivedChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{828e8ab6-d94c-4264-9cef-5217170d6251}')
    _idlflags_ = []

class ICoreWebView2CallDevToolsProtocolMethodCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5c4889f0-5ef6-4c5a-952c-d8f1b92d0574}')
    _idlflags_ = []

class ICoreWebView2CapturePreviewCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{697e05e9-3d8f-45fa-96f4-8ffe1ededaf5}')
    _idlflags_ = []

class ICoreWebView2ClearBrowsingDataCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e9710a06-1d1d-49b2-8234-226f35846ae5}')
    _idlflags_ = []

class ICoreWebView2ContainsFullScreenElementChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e45d98b1-afef-45be-8baf-6c7728867f73}')
    _idlflags_ = []

class ICoreWebView2ContentLoadingEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0c8a1275-9b6b-4901-87ad-70df25bafa6e}')
    _idlflags_ = []

class ICoreWebView2ContentLoadingEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{364471e7-f2be-4910-bdba-d72077d51c4b}')
    _idlflags_ = []

class ICoreWebView2ContextMenuItem(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7aed49e3-a93f-497a-811c-749c6b6b6c65}')
    _idlflags_ = []

class ICoreWebView2ContextMenuItemCollection(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f562a2f5-c415-45cf-b909-d4b7c1e276d3}')
    _idlflags_ = []

class ICoreWebView2ContextMenuTarget(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{b8611d99-eed6-4f3f-902c-a198502ad472}')
    _idlflags_ = []

class ICoreWebView2ContextMenuRequestedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{a1d309ee-c03f-11eb-8529-0242ac130003}')
    _idlflags_ = []

class ICoreWebView2ContextMenuRequestedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{04d3fe1d-ab87-42fb-a898-da241d35b63c}')
    _idlflags_ = []

class ICoreWebView2Controller(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4d00c0d1-9434-4eb6-8078-8697a560334f}')
    _idlflags_ = []

class ICoreWebView2ControllerOptions(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{12aae616-8ccb-44ec-bcb3-eb1831881635}')
    _idlflags_ = []

class ICoreWebView2ControllerOptions4(ICoreWebView2ControllerOptions):
    _case_insensitive_ = True
    _iid_ = GUID('{21eb052f-ad39-555e-824a-c87b091d4d36}')
    _idlflags_ = []

class ICoreWebView2Cookie(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AD26D6BE-1486-43E6-BF87-A2034006CA21}')
    _idlflags_ = []

class ICoreWebView2CookieList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f7f6f714-5d2a-43c6-9503-346ece02d186}')
    _idlflags_ = []

class ICoreWebView2CookieManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{177CD9E7-B6F5-451A-94A0-5D7A3A4C4141}')
    _idlflags_ = []

class ICoreWebView2CreateCoreWebView2ControllerCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6c4819f3-c9b7-4260-8127-c9f5bde7f68c}')
    _idlflags_ = []

class ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4e8a3389-c9d8-4bd2-b6b5-124fee6cc14d}')
    _idlflags_ = []

class ICoreWebView2CustomItemSelectedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{49e1d0bc-fe9e-4481-b7c2-32324aa21998}')
    _idlflags_ = []

class ICoreWebView2Deferral(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{c10e7f7b-b585-46f0-a623-8befbf3e4ee0}')
    _idlflags_ = []

class ICoreWebView2DevToolsProtocolEventReceiver(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{b32ca51a-8371-45e9-9317-af021d080367}')
    _idlflags_ = []

class ICoreWebView2DevToolsProtocolEventReceivedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{653c2959-bb3a-4377-8632-b58ada4e66c4}')
    _idlflags_ = []

class ICoreWebView2DevToolsProtocolEventReceivedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e2fda4be-5456-406c-a261-3d452138362c}')
    _idlflags_ = []

class ICoreWebView2DocumentTitleChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f5f2b923-953e-4042-9f95-f3a118e1afd4}')
    _idlflags_ = []

class ICoreWebView2DOMContentLoadedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{16b1e21a-c503-44f2-84c9-70aba5031283}')
    _idlflags_ = []

class ICoreWebView2DOMContentLoadedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4bac7e9c-199e-49ed-87ed-249303acf019}')
    _idlflags_ = []

class ICoreWebView2DownloadOperation(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3d6b6cf2-afe1-44c7-a995-c65117714336}')
    _idlflags_ = []

class ICoreWebView2DownloadStartingEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e99bbe21-43e9-4544-a732-282764eafa60}')
    _idlflags_ = []

class ICoreWebView2DownloadStartingEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{efedc989-c396-41ca-83f7-07f845a55724}')
    _idlflags_ = []

class ICoreWebView2Environment(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{b96d755e-0319-4e92-a296-23436f46a1fc}')
    _idlflags_ = []

class ICoreWebView2Environment2(ICoreWebView2Environment):
    _case_insensitive_ = True
    _iid_ = GUID('{41f3632b-5ef4-404f-ad82-2d606c5a9a21}')
    _idlflags_ = []

class ICoreWebView2Environment6(ICoreWebView2Environment2):
    _case_insensitive_ = True
    _iid_ = GUID('{e59ee362-acbd-4857-9a8e-d3644d9459a9}')
    _idlflags_ = []

class ICoreWebView2Environment8(ICoreWebView2Environment6):
    _case_insensitive_ = True
    _iid_ = GUID('{d6eb91dd-c3d2-45e5-bd29-6dc2bc4de9cf}')
    _idlflags_ = []

class ICoreWebView2Environment9(ICoreWebView2Environment8):
    _case_insensitive_ = True
    _iid_ = GUID('{f06f41bf-4b5a-49d8-b9f6-fa16cd29f274}')
    _idlflags_ = []

class ICoreWebView2Environment10(ICoreWebView2Environment9):
    _case_insensitive_ = True
    _iid_ = GUID('{ee0eb9df-6f12-46ce-b53f-3f47b9c928e0}')
    _idlflags_ = []

class ICoreWebView2Environment15(ICoreWebView2Environment10):
    _case_insensitive_ = True
    _iid_ = GUID('{2ac5ebfb-e654-5961-a667-7971885c7b27}')
    _idlflags_ = []

class ICoreWebView2EstimatedEndTimeChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{28f0d425-93fe-4e63-9f8d-2aeec6d3ba1e}')
    _idlflags_ = []

class ICoreWebView2ExecuteScriptCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{49511172-cc67-4bca-9923-137112f4c4cc}')
    _idlflags_ = []

class ICoreWebView2ScriptException(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{054DAE00-84A3-49FF-BC17-4012A90BC9FD}')
    _idlflags_ = []

class ICoreWebView2ExecuteScriptResult(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0CE15963-3698-4DF7-9399-71ED6CDD8C9F}')
    _idlflags_ = []

class ICoreWebView2ExecuteScriptWithResultCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1bb5317b-8238-4c67-a7ff-baf6558f289d}')
    _idlflags_ = []

class ICoreWebView2FaviconChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2913da94-833d-4de0-8dca-900fc524a1a4}')
    _idlflags_ = []

class ICoreWebView2File(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f2c19559-6bc1-4583-a757-90021be9afec}')
    _idlflags_ = []

class ICoreWebView2Find(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{a3ec0f5f-ddbc-54ed-8546-af75a785b9a6}')
    _idlflags_ = []

class ICoreWebView2FindOptions(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e82e3b2b-a4af-5bc6-94c6-18b44157a16c}')
    _idlflags_ = []

class ICoreWebView2FocusChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{05ea24bd-6452-4926-9014-4b82b498135d}')
    _idlflags_ = []

class ICoreWebView2Frame(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f1131a5e-9ba9-11eb-a8b3-0242ac130003}')
    _idlflags_ = []

class ICoreWebView2Frame2(ICoreWebView2Frame):
    _case_insensitive_ = True
    _iid_ = GUID('{7a6a5834-d185-4dbf-b63f-4a9bc43107d4}')
    _idlflags_ = []

class ICoreWebView2Frame7(ICoreWebView2Frame2):
    _case_insensitive_ = True
    _iid_ = GUID('{3598cfa2-d85d-5a9f-9228-4dde1f59ec64}')
    _idlflags_ = []

class ICoreWebView2FrameChildFrameCreatedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{569e40e7-46b7-563d-83ae-1073155664d7}')
    _idlflags_ = []

class ICoreWebView2FrameContentLoadingEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0d6156f2-d332-49a7-9e03-7d8f2feeee54}')
    _idlflags_ = []

class ICoreWebView2FrameCreatedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4d6e7b5e-9baa-11eb-a8b3-0242ac130003}')
    _idlflags_ = []

class ICoreWebView2FrameCreatedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{38059770-9baa-11eb-a8b3-0242ac130003}')
    _idlflags_ = []

class ICoreWebView2FrameDOMContentLoadedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{38d9520d-340f-4d1e-a775-43fce9753683}')
    _idlflags_ = []

class ICoreWebView2FrameNameChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{435c7dc8-9baa-11eb-a8b3-0242ac130003}')
    _idlflags_ = []

class ICoreWebView2FrameNavigationCompletedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{609302ad-0e36-4f9a-a210-6a45272842a9}')
    _idlflags_ = []

class ICoreWebView2FrameNavigationStartingEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e79908bf-2d5d-4968-83db-263fea2c1da3}')
    _idlflags_ = []

class ICoreWebView2FrameWebMessageReceivedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e371e005-6d1d-4517-934b-a8f1629c62a5}')
    _idlflags_ = []

class ICoreWebView2GetCookiesCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5a4f5069-5c15-47c3-8646-f4de1c116670}')
    _idlflags_ = []

class ICoreWebView2GetFaviconCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{a2508329-7da8-49d7-8c05-fa125e4aee8d}')
    _idlflags_ = []

class ICoreWebView2HistoryChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{c79a420c-efd9-4058-9295-3e8b4bcab645}')
    _idlflags_ = []

class ICoreWebView2HttpHeadersCollectionIterator(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0702fc30-f43b-47bb-ab52-a42cb552ad9f}')
    _idlflags_ = []

class ICoreWebView2HttpRequestHeaders(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e86cac0e-5523-465c-b536-8fb9fc8c8c60}')
    _idlflags_ = []

class ICoreWebView2HttpResponseHeaders(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{03c5ff5a-9b45-4a88-881c-89a9f328619c}')
    _idlflags_ = []

class ICoreWebView2NavigationCompletedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{30d68b7d-20d9-4752-a9ca-ec8448fbb5c1}')
    _idlflags_ = []

class ICoreWebView2NavigationCompletedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{d33a35bf-1c49-4f98-93ab-006e0533fe1c}')
    _idlflags_ = []

class ICoreWebView2NavigationStartingEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5b495469-e119-438a-9b18-7604f25f2e49}')
    _idlflags_ = []

class ICoreWebView2NavigationStartingEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9adbe429-f36d-432b-9ddc-f8881fbd76e3}')
    _idlflags_ = []

class ICoreWebView2NewWindowRequestedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{34acb11c-fc37-4418-9132-f9c21d1eafb9}')
    _idlflags_ = []

class ICoreWebView2NewWindowRequestedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{d4c185fe-c81c-4989-97af-2d3fa7ab5651}')
    _idlflags_ = []

class ICoreWebView2ObjectCollectionView(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0f36fd87-4f69-4415-98da-888f89fb9a33}')
    _idlflags_ = []

class ICoreWebView2PermissionRequestedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{973ae2ef-ff18-4894-8fb2-3c758f046810}')
    _idlflags_ = []

class ICoreWebView2PermissionRequestedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{15e1c6a3-c72a-4df3-91d7-d097fbec6bfd}')
    _idlflags_ = []

class ICoreWebView2PrintCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8fd80075-ed08-42db-8570-f5d14977461e}')
    _idlflags_ = []

class ICoreWebView2PrintSettings(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{377f3721-c74e-48ca-8db1-df68e51d60e2}')
    _idlflags_ = []

class ICoreWebView2PrintToPdfCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{ccf1ef04-fd8e-4d5f-b2de-0983e41b8c36}')
    _idlflags_ = []

class ICoreWebView2ProcessInfo(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{84FA7612-3F3D-4FBF-889D-FAD000492D72}')
    _idlflags_ = []

class ICoreWebView2ProcessInfoCollection(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{402b99cd-a0cc-4fa5-b7a5-51d86a1d2339}')
    _idlflags_ = []

class ICoreWebView2ProcessInfosChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{f4af0c39-44b9-40e9-8b11-0484cfb9e0a1}')
    _idlflags_ = []

class ICoreWebView2Profile(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{79110ad3-cd5d-4373-8bc3-c60658f17a5f}')
    _idlflags_ = []

class ICoreWebView2Profile2(ICoreWebView2Profile):
    _case_insensitive_ = True
    _iid_ = GUID('{fa740d4b-5eae-4344-a8ad-74be31925397}')
    _idlflags_ = []

class ICoreWebView2Profile7(ICoreWebView2Profile2):
    _case_insensitive_ = True
    _iid_ = GUID('{7b4c7906-a1aa-4cb4-b723-db09f813d541}')
    _idlflags_ = []

class ICoreWebView2ProfileAddBrowserExtensionCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{df1aab27-82b9-4ab6-aae8-017a49398c14}')
    _idlflags_ = []

class ICoreWebView2ProfileGetBrowserExtensionsCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{fce16a1c-f107-4601-8b75-fc4940ae25d0}')
    _idlflags_ = []

class ICoreWebView2Settings(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e562e4f0-d7fa-43ac-8d71-c05150499f00}')
    _idlflags_ = []

class ICoreWebView2Settings2(ICoreWebView2Settings):
    _case_insensitive_ = True
    _iid_ = GUID('{ee9a0f68-f46c-4e32-ac23-ef8cac224d2a}')
    _idlflags_ = []

class ICoreWebView2Settings3(ICoreWebView2Settings2):
    _case_insensitive_ = True
    _iid_ = GUID('{fdb5ab74-af33-4854-84f0-0a631deb5eba}')
    _idlflags_ = []

class ICoreWebView2Settings4(ICoreWebView2Settings3):
    _case_insensitive_ = True
    _iid_ = GUID('{cb56846c-4168-4d53-b04f-03b6d6796ff2}')
    _idlflags_ = []

class ICoreWebView2Settings5(ICoreWebView2Settings4):
    _case_insensitive_ = True
    _iid_ = GUID('{183e7052-1d03-43a0-ab99-98e043b66b39}')
    _idlflags_ = []

class ICoreWebView2Settings6(ICoreWebView2Settings5):
    _case_insensitive_ = True
    _iid_ = GUID('{11cb3acd-9bc8-43b8-83bf-f40753714f87}')
    _idlflags_ = []

class ICoreWebView2ShowSaveAsUICompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{e24b07e3-8169-5c34-994a-7f6478946a3c}')
    _idlflags_ = []

class ICoreWebView2SourceChangedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{31e0e545-1dba-4266-8914-f63848a1f7d7}')
    _idlflags_ = []

class ICoreWebView2SourceChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3c067f9f-5388-4772-8b48-79f7ef1ab37c}')
    _idlflags_ = []

class ICoreWebView2StateChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{81336594-7ede-4ba9-bf71-acf0a95b58dd}')
    _idlflags_ = []

class ICoreWebView2StatusBarTextChangedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{a5e3b0d0-10df-4156-bfad-3b43867acac6}')
    _idlflags_ = []

class ICoreWebView2WebMessageReceivedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0f99a40c-e962-4207-9e92-e3d542eff849}')
    _idlflags_ = []

class ICoreWebView2WebMessageReceivedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{57213f19-00e6-49fa-8e07-898ea01ecbd2}')
    _idlflags_ = []

class ICoreWebView2WebResourceRequest(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{97055cd4-512c-4264-8b5f-e3f446cea6a5}')
    _idlflags_ = []

class ICoreWebView2WebResourceRequestedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{453e667f-12c7-49d4-be6d-ddbe7956f57a}')
    _idlflags_ = []

class ICoreWebView2WebResourceRequestedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{ab00b74c-15f1-4646-80e8-e76341d25d71}')
    _idlflags_ = []

class ICoreWebView2WebResourceResponse(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{aafcc94f-fa27-48fd-97df-830ef75aaec9}')
    _idlflags_ = []

class ICoreWebView2WebResourceResponseReceivedEventArgs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{d1db483d-6796-4b8b-80fc-13712bb716f4}')
    _idlflags_ = []

class ICoreWebView2WebMessageReceivedEventArgs2(ICoreWebView2WebMessageReceivedEventArgs):
    _case_insensitive_ = True
    _iid_ = GUID('{06fc7ab7-c90c-4297-9389-33ca01cf6d5e}')
    _idlflags_ = []

class ICoreWebView2WebResourceResponseReceivedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7de9898a-24f5-40c3-a2de-d4f458e69828}')
    _idlflags_ = []

class ICoreWebView2WebResourceResponseView(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{79701053-7759-4162-8F7D-F1B3F084928D}')
    _idlflags_ = []

class ICoreWebView2WebResourceResponseViewGetContentCompletedHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{875738e1-9fa2-40e3-8b74-2e8972dd6fe7}')
    _idlflags_ = []

class ICoreWebView2WindowCloseRequestedEventHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5c19e9e0-092f-486b-affa-ca8231913039}')
    _idlflags_ = []

########################################
# COM Class methods
########################################

ICoreWebView2._methods_ = [
    COMMETHOD([], HRESULT, 'get_Settings',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Settings)), 'ICoreWebView2Settings' )),

    COMMETHOD([], HRESULT, 'get_Source',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'Navigate',
        ( ['in'], LPCWSTR, 'uri' )),

    COMMETHOD([], HRESULT, 'NavigateToString',
        ( ['in'], LPCWSTR, 'htmlContent' )),

    COMMETHOD([], HRESULT, 'add_NavigationStarting',
        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NavigationStarting',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_ContentLoading',
        ( ['in'], POINTER(ICoreWebView2ContentLoadingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ContentLoading',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_SourceChanged',
        ( ['in'], POINTER(ICoreWebView2SourceChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_SourceChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_HistoryChanged',
        ( ['in'], POINTER(ICoreWebView2HistoryChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_HistoryChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_NavigationCompleted',
        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NavigationCompleted',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_FrameNavigationStarting',
        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_FrameNavigationStarting',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_FrameNavigationCompleted',
        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_FrameNavigationCompleted',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_ScriptDialogOpening',
        ( ['in'], POINTER(ICoreWebView2ScriptDialogOpeningEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ScriptDialogOpening',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_PermissionRequested',
        ( ['in'], POINTER(ICoreWebView2PermissionRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_PermissionRequested',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_ProcessFailed',
        ( ['in'], POINTER(ICoreWebView2ProcessFailedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ProcessFailed',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'AddScriptToExecuteOnDocumentCreated',
        ( ['in'], LPCWSTR, 'javaScript' ),
        ( ['in'], POINTER(ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'RemoveScriptToExecuteOnDocumentCreated',
        ( ['in'], LPCWSTR, 'id' )),

    COMMETHOD([], HRESULT, 'ExecuteScript',
        ( ['in'], LPCWSTR, 'javaScript' ),
        ( ['in'], POINTER(ICoreWebView2ExecuteScriptCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'CapturePreview',
        ( ['in'], INT, 'imageFormat' ),  # COREWEBVIEW2_CAPTURE_PREVIEW_IMAGE_FORMAT
        ( ['in'], POINTER(IStream), 'imageStream' ),
        ( ['in'], POINTER(ICoreWebView2CapturePreviewCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'Reload'),

    COMMETHOD([], HRESULT, 'PostWebMessageAsJson',
        ( ['in'], LPCWSTR, 'webMessageAsJson' )),

    COMMETHOD([], HRESULT, 'PostWebMessageAsString',
        ( ['in'], LPCWSTR, 'webMessageAsString' )),

    COMMETHOD([], HRESULT, 'add_WebMessageReceived',
        ( ['in'], POINTER(ICoreWebView2WebMessageReceivedEventHandler), 'handler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_WebMessageReceived',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'CallDevToolsProtocolMethod',
        ( ['in'], LPCWSTR, 'methodName' ),
        ( ['in'], LPCWSTR, 'parametersAsJson' ),
        ( ['in'], POINTER(ICoreWebView2CallDevToolsProtocolMethodCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'get_BrowserProcessId',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'get_CanGoBack',
        ( ['retval', 'out'], LPBOOL, 'canGoBack' )),

    COMMETHOD([], HRESULT, 'get_CanGoForward',
        ( ['retval', 'out'], LPBOOL, 'canGoForward' )),

    COMMETHOD([], HRESULT, 'GoBack'),

    COMMETHOD([], HRESULT, 'GoForward'),

    COMMETHOD([], HRESULT, 'GetDevToolsProtocolEventReceiver',
        ( ['in'], LPCWSTR, 'eventName' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2DevToolsProtocolEventReceiver)), 'receiver' )),

    COMMETHOD([], HRESULT, 'Stop'),

    COMMETHOD([], HRESULT, 'add_NewWindowRequested',
        ( ['in'], POINTER(ICoreWebView2NewWindowRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NewWindowRequested',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_DocumentTitleChanged',
        ( ['in'], POINTER(ICoreWebView2DocumentTitleChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_DocumentTitleChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_DocumentTitle',
        ( ['retval', 'out'], POINTER(LPWSTR), 'title' )),

    COMMETHOD([], HRESULT, 'AddHostObjectToScript',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], POINTER(VARIANT), 'object' )),

    COMMETHOD([], HRESULT, 'RemoveHostObjectFromScript',
        ( ['in'], LPCWSTR, 'name' )),

    COMMETHOD([], HRESULT, 'OpenDevToolsWindow'),

    COMMETHOD([], HRESULT, 'add_ContainsFullScreenElementChanged',
        ( ['in'], POINTER(ICoreWebView2ContainsFullScreenElementChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ContainsFullScreenElementChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_ContainsFullScreenElement',
        ( ['retval', 'out'], LPBOOL, 'containsFullScreenElement' )),

    COMMETHOD([], HRESULT, 'add_WebResourceRequested',
        ( ['in'], POINTER(ICoreWebView2WebResourceRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_WebResourceRequested',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'AddWebResourceRequestedFilter',
        ( ['in'], LPCWSTR, 'uri' ),
        ( ['in'], INT, 'resourceContext' )),  # COREWEBVIEW2_WEB_RESOURCE_CONTEXT

    COMMETHOD([], HRESULT, 'RemoveWebResourceRequestedFilter',
        ( ['in'], LPCWSTR, 'uri' ),
        ( ['in'], INT, 'resourceContext' )),  # COREWEBVIEW2_WEB_RESOURCE_CONTEXT

    COMMETHOD([], HRESULT, 'add_WindowCloseRequested',
        ( ['in'], POINTER(ICoreWebView2WindowCloseRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_WindowCloseRequested',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2_2._methods_ = [
    COMMETHOD([], HRESULT, 'add_WebResourceResponseReceived',
        ( ['in'], POINTER(ICoreWebView2WebResourceResponseReceivedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_WebResourceResponseReceived',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'NavigateWithWebResourceRequest',
        ( ['in'], POINTER(ICoreWebView2WebResourceRequest), 'request' )),

    COMMETHOD([], HRESULT, 'add_DOMContentLoaded',
        ( ['in'], POINTER(ICoreWebView2DOMContentLoadedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_DOMContentLoaded',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_CookieManager',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2CookieManager)), 'cookieManager' )),

    COMMETHOD([], HRESULT, 'get_Environment',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Environment)), 'environment' )),
]

ICoreWebView2_3._methods_ = [
    COMMETHOD([], HRESULT, 'TrySuspend',
        ( ['in'], POINTER(ICoreWebView2TrySuspendCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'Resume'),

    COMMETHOD([], HRESULT, 'get_IsSuspended',
        ( ['retval', 'out'], LPBOOL, 'isSuspended' )),

    COMMETHOD([], HRESULT, 'SetVirtualHostNameToFolderMapping',
        ( ['in'], LPCWSTR, 'hostName' ),
        ( ['in'], LPCWSTR, 'folderPath' ),
        ( ['in'], INT, 'accessKind' )),  # COREWEBVIEW2_HOST_RESOURCE_ACCESS_KIND

    COMMETHOD([], HRESULT, 'ClearVirtualHostNameToFolderMapping',
        ( ['in'], LPCWSTR, 'hostName' )),
]

ICoreWebView2_4._methods_ = [
    COMMETHOD([], HRESULT, 'add_FrameCreated',
        ( ['in'], POINTER(ICoreWebView2FrameCreatedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_FrameCreated',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_DownloadStarting',
        ( ['in'], POINTER(ICoreWebView2DownloadStartingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_DownloadStarting',
        ( ['in'], EventRegistrationToken, 'token' )),
]

# ICoreWebView2_5

ICoreWebView2_6._methods_ = [COMMETHOD([], HRESULT, '_')] * 2 + [
    COMMETHOD([], HRESULT, 'OpenTaskManagerWindow'),
]

ICoreWebView2_7._methods_ = [
    COMMETHOD([], HRESULT, 'PrintToPdf',
        ( ['in'], LPCWSTR, 'ResultFilePath' ),
        ( ['in'], POINTER(ICoreWebView2PrintSettings), 'printSettings' ),
        ( ['in'], POINTER(ICoreWebView2PrintToPdfCompletedHandler), 'handler' )),
]

ICoreWebView2_8._methods_ = [
    COMMETHOD([], HRESULT, 'add_IsMutedChanged',
        ( ['in'], POINTER(ICoreWebView2IsMutedChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_IsMutedChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_IsMuted',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsMuted',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'add_IsDocumentPlayingAudioChanged',
        ( ['in'], POINTER(ICoreWebView2IsDocumentPlayingAudioChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_IsDocumentPlayingAudioChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_IsDocumentPlayingAudio',
        ( ['retval', 'out'], LPBOOL, 'value' )),
]

# ICoreWebView2_9 - ICoreWebView2_10

ICoreWebView2_11._methods_ = [COMMETHOD([], HRESULT, '_')] * 11 + [
    COMMETHOD([], HRESULT, 'CallDevToolsProtocolMethodForSession',
        ( ['in'], LPCWSTR, 'sessionId' ),
        ( ['in'], LPCWSTR, 'methodName' ),
        ( ['in'], LPCWSTR, 'parametersAsJson' ),
        ( ['in'], POINTER(ICoreWebView2CallDevToolsProtocolMethodCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'add_ContextMenuRequested',
        ( ['in'], POINTER(ICoreWebView2ContextMenuRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ContextMenuRequested',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2_12._methods_ = [
    COMMETHOD([], HRESULT, 'add_StatusBarTextChanged',
        ( ['in'], POINTER(ICoreWebView2StatusBarTextChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_StatusBarTextChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_StatusBarText',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2_13._methods_ = [
    COMMETHOD([], HRESULT, 'get_Profile',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Profile)), 'value' )),
]

# ICoreWebView2_14

ICoreWebView2_15._methods_ = [COMMETHOD([], HRESULT, '_')] * 3 + [
    COMMETHOD([], HRESULT, 'add_FaviconChanged',
        ( ['in'], POINTER(ICoreWebView2FaviconChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_FaviconChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_FaviconUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'GetFavicon',
        ( ['in'], INT, 'format' ),  # COREWEBVIEW2_FAVICON_IMAGE_FORMAT
        ( ['in'], POINTER(ICoreWebView2GetFaviconCompletedHandler), 'completedHandler' )),
]

ICoreWebView2_16._methods_ = [
    COMMETHOD([], HRESULT, 'Print',
        ( ['in'], POINTER(ICoreWebView2PrintSettings), 'printSettings' ),
        ( ['in'], POINTER(ICoreWebView2PrintCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'ShowPrintUI',
        ( ['in'], INT, 'printDialogKind' )),  # COREWEBVIEW2_PRINT_DIALOG_KIND

    COMMETHOD([], HRESULT, 'PrintToPdfStream',
        ( ['in'], POINTER(ICoreWebView2PrintSettings), 'printSettings' ),
        ( ['in'], POINTER(ICoreWebView2PrintToPdfStreamCompletedHandler), 'handler' )),
]

#ICoreWebView2_17    1
#ICoreWebView2_18    2
#ICoreWebView2_19    2

ICoreWebView2_20._methods_ = [COMMETHOD([], HRESULT, '_')] * 5 + [
    COMMETHOD([], HRESULT, 'get_FrameId',
        ( ['retval', 'out'], POINTER(UINT), 'value' )),
]

ICoreWebView2_21._methods_ = [
    COMMETHOD([], HRESULT, 'ExecuteScriptWithResult',
        ( ['in'], LPCWSTR, 'javaScript' ),
        ( ['in'], POINTER(ICoreWebView2ExecuteScriptWithResultCompletedHandler), 'handler' )),
]

#ICoreWebView2_22    2
#ICoreWebView2_23    1
#ICoreWebView2_24    2

ICoreWebView2_25._methods_ = [COMMETHOD([], HRESULT, '_')] * 5 + [
    COMMETHOD([], HRESULT, 'add_SaveAsUIShowing',
        ( ['in'], POINTER(ICoreWebView2SaveAsUIShowingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_SaveAsUIShowing',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'ShowSaveAsUI',
        ( ['in'], POINTER(ICoreWebView2ShowSaveAsUICompletedHandler), 'handler' )),
]

#ICoreWebView2_26   2
#ICoreWebView2_27   2

ICoreWebView2_28._methods_ = [COMMETHOD([], HRESULT, '_')] * 4 + [
    COMMETHOD([], HRESULT, 'get_Find',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Find)), 'value' )),
]

ICoreWebView2AcceleratorKeyPressedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_KeyEventKind',
        ( ['retval', 'out'], LPINT, 'keyEventKind' )),  # COREWEBVIEW2_KEY_EVENT_KIND

    COMMETHOD([], HRESULT, 'get_VirtualKey',
        ( ['retval', 'out'], POINTER(UINT), 'virtualKey' )),

    COMMETHOD([], HRESULT, 'get_KeyEventLParam',
        ( ['retval', 'out'], LPINT, 'lParam' )),

    COMMETHOD([], HRESULT, 'get_PhysicalKeyStatus',
        ( ['retval', 'out'], POINTER(COREWEBVIEW2_PHYSICAL_KEY_STATUS), 'physicalKeyStatus' )),

    COMMETHOD([], HRESULT, 'get_Handled',
        ( ['retval', 'out'], LPBOOL, 'handled' )),

    COMMETHOD([], HRESULT, 'put_Handled',
        ( ['in'], BOOL, 'enabled' )),
]

ICoreWebView2AcceleratorKeyPressedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Controller), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2AcceleratorKeyPressedEventArgs), 'args' )),
]

ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], LPCWSTR, 'result' )),
]

ICoreWebView2BrowserExtension._methods_ = [
    COMMETHOD([], HRESULT, 'get_Id',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_Name',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'Remove',
        ( ['in'], POINTER(ICoreWebView2BrowserExtensionRemoveCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'get_IsEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'Enable',
        ( ['in'], BOOL, 'isEnabled' ),
        ( ['in'], POINTER(ICoreWebView2BrowserExtensionEnableCompletedHandler), 'handler' )),
]

ICoreWebView2BrowserExtensionEnableCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' )),
]

ICoreWebView2BrowserExtensionList._methods_ = [
    COMMETHOD([], HRESULT, 'get_Count',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'GetValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2BrowserExtension)), 'value' )),
]

ICoreWebView2BrowserExtensionRemoveCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' )),
]

ICoreWebView2BytesReceivedChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2DownloadOperation), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2CallDevToolsProtocolMethodCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], LPCWSTR, 'result' )),
]

ICoreWebView2CapturePreviewCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' )),
]

ICoreWebView2ClearBrowsingDataCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' )),
]

ICoreWebView2ContainsFullScreenElementChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2ContentLoadingEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsErrorPage',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_NavigationId',
        ( ['retval', 'out'], POINTER(UINT64), 'value' )),
]

ICoreWebView2ContentLoadingEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2ContentLoadingEventArgs), 'args' )),
]

ICoreWebView2ContextMenuItem._methods_ = [
    COMMETHOD([], HRESULT, 'get_Name',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_Label',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_CommandId',
        ( ['retval', 'out'], POINTER(INT), 'value' )),  # INT32

    COMMETHOD([], HRESULT, 'get_ShortcutKeyDescription',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_Icon',
        ( ['retval', 'out'], POINTER(POINTER(IStream)), 'value' )),

    COMMETHOD([], HRESULT, 'get_Kind',
        ( ['retval', 'out'], LPINT, 'value' )),  # COREWEBVIEW2_CONTEXT_MENU_ITEM_KIND

    COMMETHOD([], HRESULT, 'put_IsEnabled',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsChecked',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsChecked',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_Children',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ContextMenuItemCollection)), 'value' )),

    COMMETHOD([], HRESULT, 'add_CustomItemSelected',
        ( ['in'], POINTER(ICoreWebView2CustomItemSelectedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_CustomItemSelected',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2ContextMenuItemCollection._methods_ = [
    COMMETHOD([], HRESULT, 'get_Count',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'GetValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ContextMenuItem)), 'value' )),

    COMMETHOD([], HRESULT, 'RemoveValueAtIndex',
        ( ['in'], UINT32, 'index' )),

    COMMETHOD([], HRESULT, 'InsertValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['in'], POINTER(ICoreWebView2ContextMenuItem), 'value' )),
]

ICoreWebView2ContextMenuTarget._methods_ = [
    COMMETHOD([], HRESULT, 'get_Kind',
        ( ['retval', 'out'], LPINT, 'value' )),  # COREWEBVIEW2_CONTEXT_MENU_TARGET_KIND

    COMMETHOD([], HRESULT, 'get_IsEditable',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsRequestedForMainFrame',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_PageUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_FrameUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_HasLinkUri',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_LinkUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_HasLinkText',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_LinkText',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_HasSourceUri',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_SourceUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_HasSelection',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_SelectionText',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2ContextMenuRequestedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_MenuItems',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ContextMenuItemCollection)), 'value' )),

    COMMETHOD([], HRESULT, 'get_ContextMenuTarget',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ContextMenuTarget)), 'value' )),

    COMMETHOD([], HRESULT, 'get_Location',
        ( ['retval', 'out'], LPPOINT, 'value' )),

    COMMETHOD([], HRESULT, 'put_SelectedCommandId',
        ( ['in'], INT, 'value' )),  # INT32

    COMMETHOD([], HRESULT, 'get_SelectedCommandId',
        ( ['retval', 'out'], POINTER(INT), 'value' )),  # INT32

    COMMETHOD([], HRESULT, 'put_Handled',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_Handled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'GetDeferral',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Deferral)), 'deferral' )),
]

ICoreWebView2ContextMenuRequestedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2ContextMenuRequestedEventArgs), 'args' )),
]

ICoreWebView2Controller._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsVisible',
        ( ['retval', 'out'], LPBOOL, 'isVisible' )),

    COMMETHOD([], HRESULT, 'put_IsVisible',
        ( ['in'], BOOL, 'isVisible' )),

    COMMETHOD([], HRESULT, 'get_Bounds',
        ( ['retval', 'out'], POINTER(RECT), 'bounds' )),

    COMMETHOD([], HRESULT, 'put_Bounds',
        ( ['in'], RECT, 'bounds' )),

    COMMETHOD([], HRESULT, 'get_ZoomFactor',
        ( ['retval', 'out'], POINTER(DOUBLE), 'zoomFactor' )),

    COMMETHOD([], HRESULT, 'put_ZoomFactor',
        ( ['in'], DOUBLE, 'zoomFactor' )),

    COMMETHOD([], HRESULT, 'add_ZoomFactorChanged',
        ( ['in'], POINTER(ICoreWebView2ZoomFactorChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ZoomFactorChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'SetBoundsAndZoomFactor',
        ( ['in'], RECT, 'bounds' ),
        ( ['in'], DOUBLE, 'zoomFactor' )),

    COMMETHOD([], HRESULT, 'MoveFocus',
        ( ['in'], INT, 'reason' )),  # COREWEBVIEW2_MOVE_FOCUS_REASON

    COMMETHOD([], HRESULT, 'add_MoveFocusRequested',
        ( ['in'], POINTER(ICoreWebView2MoveFocusRequestedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_MoveFocusRequested',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_GotFocus',
        ( ['in'], POINTER(ICoreWebView2FocusChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_GotFocus',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_LostFocus',
        ( ['in'], POINTER(ICoreWebView2FocusChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_LostFocus',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_AcceleratorKeyPressed',
        ( ['in'], POINTER(ICoreWebView2AcceleratorKeyPressedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_AcceleratorKeyPressed',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_ParentWindow',
        ( ['retval', 'out'], POINTER(HWND), 'parentWindow' )),

    COMMETHOD([], HRESULT, 'put_ParentWindow',
        ( ['in'], HWND, 'parentWindow' )),

    COMMETHOD([], HRESULT, 'NotifyParentWindowPositionChanged'),

    COMMETHOD([], HRESULT, 'Close'),

    COMMETHOD([], HRESULT, 'get_CoreWebView2',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2)), 'coreWebView2' )),
]

ICoreWebView2ControllerOptions._methods_ = [
    COMMETHOD([], HRESULT, 'get_ProfileName',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'put_ProfileName',
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsInPrivateModeEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsInPrivateModeEnabled',
        ( ['in'], BOOL, 'value' )),
]

#ICoreWebView2ControllerOptions2: 2
#ICoreWebView2ControllerOptions3: 2

ICoreWebView2ControllerOptions4._methods_ = [COMMETHOD([], HRESULT, '_')] * 4 + [
    COMMETHOD([], HRESULT, 'get_AllowHostInputProcessing',
        ( ['retval', 'out'], POINTER(BOOL), 'value' )),

    COMMETHOD([], HRESULT, 'put_AllowHostInputProcessing',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2Cookie._methods_ = [
    COMMETHOD([], HRESULT, 'get_Name',
        ( ['retval', 'out'], POINTER(LPWSTR), 'name' )),

    COMMETHOD([], HRESULT, 'get_Value',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'put_Value',
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'get_Domain',
        ( ['retval', 'out'], POINTER(LPWSTR), 'domain' )),

    COMMETHOD([], HRESULT, 'get_Path',
        ( ['retval', 'out'], POINTER(LPWSTR), 'path' )),

    COMMETHOD([], HRESULT, 'get_Expires',
        ( ['retval', 'out'], POINTER(DOUBLE), 'expires' )),

    COMMETHOD([], HRESULT, 'put_Expires',
        ( ['in'], DOUBLE, 'expires' )),

    COMMETHOD([], HRESULT, 'get_IsHttpOnly',
        ( ['retval', 'out'], LPBOOL, 'isHttpOnly' )),

    COMMETHOD([], HRESULT, 'put_IsHttpOnly',
        ( ['in'], BOOL, 'isHttpOnly' )),

    COMMETHOD([], HRESULT, 'get_SameSite',
        ( ['retval', 'out'], LPINT, 'sameSite' )),  # COREWEBVIEW2_COOKIE_SAME_SITE_KIND

    COMMETHOD([], HRESULT, 'put_SameSite',
        ( ['in'], INT, 'sameSite' )),  # COREWEBVIEW2_COOKIE_SAME_SITE_KIND

    COMMETHOD([], HRESULT, 'get_IsSecure',
        ( ['retval', 'out'], LPBOOL, 'isSecure' )),

    COMMETHOD([], HRESULT, 'put_IsSecure',
        ( ['in'], BOOL, 'isSecure' )),

    COMMETHOD([], HRESULT, 'get_IsSession',
        ( ['retval', 'out'], LPBOOL, 'isSession' )),
]

ICoreWebView2CookieList._methods_ = [
    COMMETHOD([], HRESULT, 'get_Count',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'GetValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Cookie)), 'value' )),
]

ICoreWebView2CookieManager._methods_ = [
    COMMETHOD([], HRESULT, 'CreateCookie',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], LPCWSTR, 'value' ),
        ( ['in'], LPCWSTR, 'domain' ),
        ( ['in'], LPCWSTR, 'path' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Cookie)), 'handler' )),

    COMMETHOD([], HRESULT, 'CopyCookie',
        ( ['in'], POINTER(ICoreWebView2Cookie), 'cookieParam' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Cookie)), 'cookie' )),

    COMMETHOD([], HRESULT, 'GetCookies',
        ( ['in'], LPCWSTR, 'uri' ),
        ( ['in'], POINTER(ICoreWebView2GetCookiesCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'AddOrUpdateCookie',
        ( ['in'], POINTER(ICoreWebView2Cookie), 'cookie' )),

    COMMETHOD([], HRESULT, 'DeleteCookie',
        ( ['in'], POINTER(ICoreWebView2Cookie), 'cookie' )),

    COMMETHOD([], HRESULT, 'DeleteCookies',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], LPCWSTR, 'uri' )),

    COMMETHOD([], HRESULT, 'DeleteCookiesWithDomainAndPath',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], LPCWSTR, 'domain' ),
        ( ['in'], LPCWSTR, 'path' )),

    COMMETHOD([], HRESULT, 'DeleteAllCookies'),
]

ICoreWebView2CreateCoreWebView2ControllerCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2Controller), 'result' )),
]

ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2Environment), 'result' )),
]

ICoreWebView2CustomItemSelectedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2ContextMenuItem), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2Deferral._methods_ = [
    COMMETHOD([], HRESULT, 'Complete'),
]

ICoreWebView2DevToolsProtocolEventReceivedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_ParameterObjectAsJson',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2DevToolsProtocolEventReceivedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2DevToolsProtocolEventReceivedEventArgs), 'args' )),
]

ICoreWebView2DevToolsProtocolEventReceiver._methods_ = [
    COMMETHOD([], HRESULT, 'add_DevToolsProtocolEventReceived',
        ( ['in'], POINTER(ICoreWebView2DevToolsProtocolEventReceivedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_DevToolsProtocolEventReceived',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2DocumentTitleChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2DOMContentLoadedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_NavigationId',
        ( ['retval', 'out'], POINTER(UINT64), 'value' )),
]

ICoreWebView2DOMContentLoadedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2DOMContentLoadedEventArgs), 'args' )),
]

ICoreWebView2DownloadOperation._methods_ = [
    COMMETHOD([], HRESULT, 'add_BytesReceivedChanged',
        ( ['in'], POINTER(ICoreWebView2BytesReceivedChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_BytesReceivedChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_EstimatedEndTimeChanged',
        ( ['in'], POINTER(ICoreWebView2EstimatedEndTimeChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_EstimatedEndTimeChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_StateChanged',
        ( ['in'], POINTER(ICoreWebView2StateChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_StateChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'get_Uri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'get_ContentDisposition',
        ( ['retval', 'out'], POINTER(LPWSTR), 'contentDisposition' )),

    COMMETHOD([], HRESULT, 'get_MimeType',
        ( ['retval', 'out'], POINTER(LPWSTR), 'mimeType' )),

    COMMETHOD([], HRESULT, 'get_TotalBytesToReceive',
        ( ['retval', 'out'], POINTER(INT64), 'totalBytesToReceive' )),

    COMMETHOD([], HRESULT, 'get_BytesReceived',
        ( ['retval', 'out'], POINTER(INT64), 'bytesReceived' )),

    COMMETHOD([], HRESULT, 'get_EstimatedEndTime',
        ( ['retval', 'out'], POINTER(LPWSTR), 'estimatedEndTime' )),

    COMMETHOD([], HRESULT, 'get_ResultFilePath',
        ( ['retval', 'out'], POINTER(LPWSTR), 'resultFilePath' )),

    COMMETHOD([], HRESULT, 'get_State',
        ( ['retval', 'out'], LPINT, 'downloadState' )), # COREWEBVIEW2_DOWNLOAD_STATE

    COMMETHOD([], HRESULT, 'get_InterruptReason',
        ( ['retval', 'out'], LPINT, 'interruptReason' )), # COREWEBVIEW2_DOWNLOAD_INTERRUPT_REASON

    COMMETHOD([], HRESULT, 'Cancel'),

    COMMETHOD([], HRESULT, 'Pause'),

    COMMETHOD([], HRESULT, 'Resume'),

    COMMETHOD([], HRESULT, 'get_CanResume',
        ( ['retval', 'out'], LPBOOL, 'canResume' )),
]

ICoreWebView2DownloadStartingEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_DownloadOperation',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2DownloadOperation)), 'downloadOperation' )),

    COMMETHOD([], HRESULT, 'get_Cancel',
        ( ['retval', 'out'], LPBOOL, 'cancel' )),

    COMMETHOD([], HRESULT, 'put_Cancel',
        ( ['in'], BOOL, 'cancel' )),

    COMMETHOD([], HRESULT, 'get_ResultFilePath',
        ( ['retval', 'out'], POINTER(LPWSTR), 'resultFilePath' )),

    COMMETHOD([], HRESULT, 'put_ResultFilePath',
        ( ['in'], LPCWSTR, 'resultFilePath' )),

    COMMETHOD([], HRESULT, 'get_Handled',
        ( ['retval', 'out'], LPBOOL, 'handled' )),

    COMMETHOD([], HRESULT, 'put_Handled',
        ( ['in'], BOOL, 'handled' )),

    COMMETHOD([], HRESULT, 'GetDeferral',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Deferral)), 'deferral' )),
]

ICoreWebView2DownloadStartingEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2DownloadStartingEventArgs), 'args' )),
]

ICoreWebView2Environment._methods_ = [
    COMMETHOD([], HRESULT, 'CreateCoreWebView2Controller',
        ( ['in'], HWND, 'parentWindow' ),
        ( ['in'], POINTER(ICoreWebView2CreateCoreWebView2ControllerCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'CreateWebResourceResponse',
        ( ['in'], POINTER(IStream), 'content' ),
        ( ['in'], INT, 'statusCode' ),
        ( ['in'], LPCWSTR, 'reasonPhrase' ),
        ( ['in'], LPCWSTR, 'headers' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceResponse)), 'response' )),

    COMMETHOD([], HRESULT, 'get_BrowserVersionString',
        ( ['retval', 'out'], POINTER(LPWSTR), 'versionInfo' )),

    COMMETHOD([], HRESULT, 'add_NewBrowserVersionAvailable',
        ( ['in'], POINTER(ICoreWebView2NewBrowserVersionAvailableEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NewBrowserVersionAvailable',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2Environment2._methods_ = [
    COMMETHOD([], HRESULT, 'CreateWebResourceRequest',
        ( ['in'], LPCWSTR, 'uri' ),
        ( ['in'], LPCWSTR, 'Method' ),
        ( ['in'], POINTER(IStream), 'postData' ),
        ( ['in'], LPCWSTR, 'Headers' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceRequest)), 'value' )),
]

#ICoreWebView2Environment3   2
#ICoreWebView2Environment4   1
#ICoreWebView2Environment5   2

ICoreWebView2Environment6._methods_ = [COMMETHOD([], HRESULT, '_')] * 5 + [
    COMMETHOD([], HRESULT, 'CreatePrintSettings',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2PrintSettings)), 'value' )),
]

#ICoreWebView2Environment7   1

ICoreWebView2Environment8._methods_ = [COMMETHOD([], HRESULT, '_')] + [
    COMMETHOD([], HRESULT, 'add_ProcessInfosChanged',
        ( ['in'], POINTER(ICoreWebView2ProcessInfosChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ProcessInfosChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'GetProcessInfos',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ProcessInfoCollection)), 'value' )),
]

ICoreWebView2Environment9._methods_ = [
    COMMETHOD([], HRESULT, 'CreateContextMenuItem',
        ( ['in'], LPCWSTR, 'Label' ),
        ( ['in'], POINTER(IStream), 'iconStream' ),
        ( ['in'], INT, 'Kind' ),  # COREWEBVIEW2_CONTEXT_MENU_ITEM_KIND
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ContextMenuItem)), 'value' )),
]

ICoreWebView2Environment10._methods_ = [
    COMMETHOD([], HRESULT, 'CreateCoreWebView2ControllerOptions',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ControllerOptions)), 'value' )),

    COMMETHOD([], HRESULT, 'CreateCoreWebView2ControllerWithOptions',
        ( ['in'], HWND, 'ParentWindow' ),
        ( ['in'], POINTER(ICoreWebView2ControllerOptions), 'options' ),
        ( ['in'], POINTER(ICoreWebView2CreateCoreWebView2ControllerCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'CreateCoreWebView2CompositionControllerWithOptions',
        ( ['in'], HWND, 'ParentWindow' ),
        ( ['in'], POINTER(ICoreWebView2ControllerOptions), 'options' ),
        ( ['in'], POINTER(ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler), 'handler' )),
]

#ICoreWebView2Environment11: 1
#ICoreWebView2Environment12: 1
#ICoreWebView2Environment13: 1
#ICoreWebView2Environment14: 3

ICoreWebView2Environment15._methods_ = [COMMETHOD([], HRESULT, '_')] * 6 + [
    COMMETHOD([], HRESULT, 'CreateFindOptions',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2FindOptions)), 'value' )),
]

ICoreWebView2EstimatedEndTimeChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2DownloadOperation), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2ExecuteScriptCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], LPCWSTR, 'result' )),
]

ICoreWebView2ScriptException._methods_ = [
    COMMETHOD([], HRESULT, 'get_LineNumber',
        ( ['retval', 'out'], POINTER(UINT), 'value' )),

    COMMETHOD([], HRESULT, 'get_ColumnNumber',
        ( ['retval', 'out'], POINTER(UINT), 'value' )),

    COMMETHOD([], HRESULT, 'get_Name',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_Message',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_ToJson',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2ExecuteScriptResult._methods_ = [
    COMMETHOD([], HRESULT, 'get_Succeeded',
        ( ['retval', 'out'], POINTER(BOOL), 'value' )),

    COMMETHOD([], HRESULT, 'get_ResultAsJson',
        ( ['retval', 'out'], POINTER(LPWSTR), 'jsonResult' )),

    COMMETHOD([], HRESULT, 'TryGetResultAsString',
        ( ['out'], POINTER(LPWSTR), 'stringResult' ),
        ( ['out'], POINTER(BOOL), 'value' )),

    COMMETHOD([], HRESULT, 'get_Exception',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ScriptException)), 'exception' )),
]

ICoreWebView2ExecuteScriptWithResultCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2ExecuteScriptResult), 'result' )),
]

ICoreWebView2FaviconChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2File._methods_ = [
    COMMETHOD([], HRESULT, 'get_Path',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2Find._methods_ = [
    COMMETHOD([], HRESULT, 'get_ActiveMatchIndex',
        ( ['retval', 'out'], POINTER(INT), 'value' )),

    COMMETHOD([], HRESULT, 'get_MatchCount',
        ( ['retval', 'out'], POINTER(INT), 'value' )),

    COMMETHOD([], HRESULT, 'add_ActiveMatchIndexChanged',
        ( ['in'], POINTER(ICoreWebView2FindActiveMatchIndexChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ActiveMatchIndexChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_MatchCountChanged',
        ( ['in'], POINTER(ICoreWebView2FindMatchCountChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_MatchCountChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'Start',
        ( ['in'], POINTER(ICoreWebView2FindOptions), 'options' ),
        ( ['in'], POINTER(ICoreWebView2FindStartCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'FindNext'),

    COMMETHOD([], HRESULT, 'FindPrevious'),

    COMMETHOD([], HRESULT, 'Stop'),
]

ICoreWebView2FindOptions._methods_ = [
    COMMETHOD([], HRESULT, 'get_FindTerm',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'put_FindTerm',
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsCaseSensitive',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsCaseSensitive',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_ShouldHighlightAllMatches',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_ShouldHighlightAllMatches',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_ShouldMatchWord',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_ShouldMatchWord',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_SuppressDefaultFindDialog',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_SuppressDefaultFindDialog',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2FocusChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Controller), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2GetCookiesCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2CookieList), 'result' )),
]

ICoreWebView2GetFaviconCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(IStream), 'result' )),
]

ICoreWebView2HistoryChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2HttpHeadersCollectionIterator._methods_ = [
    COMMETHOD([], HRESULT, 'GetCurrentHeader',
        ( ['out'], POINTER(LPWSTR), 'name' ),
        ( ['out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_HasCurrentHeader',
        ( ['retval', 'out'], LPBOOL, 'hasCurrent' )),

    COMMETHOD([], HRESULT, 'MoveNext',
        ( ['retval', 'out'], LPBOOL, 'hasNext' )),
]

ICoreWebView2HttpRequestHeaders._methods_ = [
    COMMETHOD([], HRESULT, 'GetHeader',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'GetHeaders',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpHeadersCollectionIterator)), 'value' )),

    COMMETHOD([], HRESULT, 'Contains',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'SetHeader',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'RemoveHeader',
        ( ['in'], LPCWSTR, 'name' )),

    COMMETHOD([], HRESULT, 'GetIterator',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpHeadersCollectionIterator)), 'value' )),
]

ICoreWebView2HttpResponseHeaders._methods_ = [
    COMMETHOD([], HRESULT, 'AppendHeader',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'Contains',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'GetHeader',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'GetHeaders',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpHeadersCollectionIterator)), 'value' )),

    COMMETHOD([], HRESULT, 'GetIterator',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpHeadersCollectionIterator)), 'value' )),
]

ICoreWebView2NavigationCompletedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsSuccess',
        ( ['retval', 'out'], LPBOOL, 'isSuccess' )),

    COMMETHOD([], HRESULT, 'get_WebErrorStatus',
        ( ['retval', 'out'], LPINT, 'webErrorStatus' )),  # COREWEBVIEW2_WEB_ERROR_STATUS

    COMMETHOD([], HRESULT, 'get_NavigationId',
        ( ['retval', 'out'], POINTER(UINT64), 'navigationId' )),
]

ICoreWebView2NavigationCompletedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventArgs), 'args' )),
]

ICoreWebView2NavigationStartingEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Uri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'get_IsUserInitiated',
        ( ['retval', 'out'], LPBOOL, 'isUserInitiated' )),

    COMMETHOD([], HRESULT, 'get_IsRedirected',
        ( ['retval', 'out'], LPBOOL, 'isRedirected' )),

    COMMETHOD([], HRESULT, 'get_RequestHeaders',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpRequestHeaders)), 'requestHeaders' )),

    COMMETHOD([], HRESULT, 'get_Cancel',
        ( ['retval', 'out'], LPBOOL, 'cancel' )),

    COMMETHOD([], HRESULT, 'put_Cancel',
        ( ['in'], BOOL, 'cancel' )),

    COMMETHOD([], HRESULT, 'get_NavigationId',
        ( ['retval', 'out'], POINTER(UINT64), 'navigationId' )),
]

ICoreWebView2NavigationStartingEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventArgs), 'args' )),
]

ICoreWebView2NewWindowRequestedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Uri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'put_NewWindow',
        ( ['in'], POINTER(ICoreWebView2), 'newWindow' )),

    COMMETHOD([], HRESULT, 'get_NewWindow',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2)), 'newWindow' )),

    COMMETHOD([], HRESULT, 'put_Handled',
        ( ['in'], BOOL, 'handled' )),

    COMMETHOD([], HRESULT, 'get_Handled',
        ( ['retval', 'out'], LPBOOL, 'handled' )),

    COMMETHOD([], HRESULT, 'get_IsUserInitiated',
        ( ['retval', 'out'], LPBOOL, 'isUserInitiated' )),

    COMMETHOD([], HRESULT, 'GetDeferral',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Deferral)), 'deferral' )),

    COMMETHOD([], HRESULT, 'get_WindowFeatures',
        ( ['retval', 'out'], POINTER(ICoreWebView2WindowFeatures), 'value' )),
]

ICoreWebView2NewWindowRequestedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2NewWindowRequestedEventArgs), 'args' )),
]

ICoreWebView2ObjectCollectionView._methods_ = [
    COMMETHOD([], HRESULT, 'get_Count',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'GetValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2File)), 'value' )),
]

ICoreWebView2PermissionRequestedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Uri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'get_PermissionKind',
        ( ['retval', 'out'], LPINT, 'permissionKind' )),  # COREWEBVIEW2_PERMISSION_KIND

    COMMETHOD([], HRESULT, 'get_IsUserInitiated',
        ( ['retval', 'out'], LPBOOL, 'isUserInitiated' )),

    COMMETHOD([], HRESULT, 'get_State',
        ( ['retval', 'out'], LPINT, 'state' )),  # COREWEBVIEW2_PERMISSION_STATE

    COMMETHOD([], HRESULT, 'put_State',
        ( ['in'], INT, 'state' )),  # COREWEBVIEW2_PERMISSION_STATE

    COMMETHOD([], HRESULT, 'GetDeferral',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Deferral)), 'deferral' )),
]

ICoreWebView2PermissionRequestedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2PermissionRequestedEventArgs), 'args' )),
]

ICoreWebView2PrintCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], INT, 'result' )),  # COREWEBVIEW2_PRINT_STATUS
]

ICoreWebView2PrintSettings._methods_ = [
    COMMETHOD([], HRESULT, 'get_Orientation',
        ( ['retval', 'out'], LPINT, 'orientation' )),  # COREWEBVIEW2_PRINT_ORIENTATION

    COMMETHOD([], HRESULT, 'put_Orientation',
        ( ['in'], INT, 'orientation' )),  # COREWEBVIEW2_PRINT_ORIENTATION

    COMMETHOD([], HRESULT, 'get_ScaleFactor',
        ( ['retval', 'out'], POINTER(DOUBLE), 'scaleFactor' )),

    COMMETHOD([], HRESULT, 'put_ScaleFactor',
        ( ['in'], DOUBLE, 'scaleFactor' )),

    COMMETHOD([], HRESULT, 'get_PageWidth',
        ( ['retval', 'out'], POINTER(DOUBLE), 'pageWidth' )),

    COMMETHOD([], HRESULT, 'put_PageWidth',
        ( ['in'], DOUBLE, 'pageWidth' )),

    COMMETHOD([], HRESULT, 'get_PageHeight',
        ( ['retval', 'out'], POINTER(DOUBLE), 'pageHeight' )),

    COMMETHOD([], HRESULT, 'put_PageHeight',
        ( ['in'], DOUBLE, 'pageHeight' )),

    COMMETHOD([], HRESULT, 'get_MarginTop',
        ( ['retval', 'out'], POINTER(DOUBLE), 'marginTop' )),

    COMMETHOD([], HRESULT, 'put_MarginTop',
        ( ['in'], DOUBLE, 'marginTop' )),

    COMMETHOD([], HRESULT, 'get_MarginBottom',
        ( ['retval', 'out'], POINTER(DOUBLE), 'marginBottom' )),

    COMMETHOD([], HRESULT, 'put_MarginBottom',
        ( ['in'], DOUBLE, 'marginBottom' )),

    COMMETHOD([], HRESULT, 'get_MarginLeft',
        ( ['retval', 'out'], POINTER(DOUBLE), 'marginLeft' )),

    COMMETHOD([], HRESULT, 'put_MarginLeft',
        ( ['in'], DOUBLE, 'marginLeft' )),

    COMMETHOD([], HRESULT, 'get_MarginRight',
        ( ['retval', 'out'], POINTER(DOUBLE), 'marginRight' )),

    COMMETHOD([], HRESULT, 'put_MarginRight',
        ( ['in'], DOUBLE, 'marginRight' )),

    COMMETHOD([], HRESULT, 'get_ShouldPrintBackgrounds',
        ( ['retval', 'out'], LPBOOL, 'shouldPrintBackgrounds' )),

    COMMETHOD([], HRESULT, 'put_ShouldPrintBackgrounds',
        ( ['in'], BOOL, 'shouldPrintBackgrounds' )),

    COMMETHOD([], HRESULT, 'get_ShouldPrintSelectionOnly',
        ( ['retval', 'out'], LPBOOL, 'shouldPrintSelectionOnly' )),

    COMMETHOD([], HRESULT, 'put_ShouldPrintSelectionOnly',
        ( ['in'], BOOL, 'shouldPrintSelectionOnly' )),

    COMMETHOD([], HRESULT, 'get_ShouldPrintHeaderAndFooter',
        ( ['retval', 'out'], LPBOOL, 'shouldPrintHeaderAndFooter' )),

    COMMETHOD([], HRESULT, 'put_ShouldPrintHeaderAndFooter',
        ( ['in'], BOOL, 'shouldPrintHeaderAndFooter' )),

    COMMETHOD([], HRESULT, 'get_HeaderTitle',
        ( ['retval', 'out'], POINTER(LPWSTR), 'headerTitle' )),

    COMMETHOD([], HRESULT, 'put_HeaderTitle',
        ( ['in'], LPCWSTR, 'headerTitle' )),

    COMMETHOD([], HRESULT, 'get_FooterUri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'footerUri' )),

    COMMETHOD([], HRESULT, 'put_FooterUri',
        ( ['in'], LPCWSTR, 'footerUri' )),
]

ICoreWebView2PrintToPdfCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], LPBOOL, 'result' )),
]

ICoreWebView2ProcessInfo._methods_ = [
    COMMETHOD([], HRESULT, 'get_ProcessId',
        ( ['retval', 'out'], POINTER(INT), 'value' )),

    COMMETHOD([], HRESULT, 'get_Kind',
        ( ['retval', 'out'], POINTER(INT), 'kind' )),  # COREWEBVIEW2_PROCESS_KIND
]

ICoreWebView2ProcessInfoCollection._methods_ = [
    COMMETHOD([], HRESULT, 'get_Count',
        ( ['retval', 'out'], POINTER(UINT32), 'value' )),

    COMMETHOD([], HRESULT, 'GetValueAtIndex',
        ( ['in'], UINT32, 'index' ),
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ProcessInfo)), 'value' )),
]

ICoreWebView2ProcessInfosChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Environment), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2Profile._methods_ = [
    COMMETHOD([], HRESULT, 'get_ProfileName',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_IsInPrivateModeEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_ProfilePath',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_DefaultDownloadFolderPath',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'put_DefaultDownloadFolderPath',
        ( ['in'], LPCWSTR, 'value' )),

    COMMETHOD([], HRESULT, 'get_PreferredColorScheme',
        ( ['retval', 'out'], LPINT, 'value' )),  # COREWEBVIEW2_PREFERRED_COLOR_SCHEME

    COMMETHOD([], HRESULT, 'put_PreferredColorScheme',
        ( ['in'], INT, 'value' )),  # COREWEBVIEW2_PREFERRED_COLOR_SCHEME
]

ICoreWebView2Profile2._methods_ = [
    COMMETHOD([], HRESULT, 'ClearBrowsingData',
        ( ['in'], INT, 'dataKinds' ),  # COREWEBVIEW2_BROWSING_DATA_KINDS
        ( ['in'], POINTER(ICoreWebView2ClearBrowsingDataCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'ClearBrowsingDataInTimeRange',
        ( ['in'], INT, 'dataKinds' ),  # COREWEBVIEW2_BROWSING_DATA_KINDS
        ( ['in'], DOUBLE, 'startTime' ),
        ( ['in'], DOUBLE, 'endTime' ),
        ( ['in'], POINTER(ICoreWebView2ClearBrowsingDataCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'ClearBrowsingDataAll',
        ( ['in'], POINTER(ICoreWebView2ClearBrowsingDataCompletedHandler), 'handler' )),
]

ICoreWebView2Profile7._methods_ = [COMMETHOD([], HRESULT, '_')] * 9 + [
    COMMETHOD([], HRESULT, 'AddBrowserExtension',
        ( ['in'], LPCWSTR, 'extensionFolderPath' ),
        ( ['in'], POINTER(ICoreWebView2ProfileAddBrowserExtensionCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'GetBrowserExtensions',
        ( ['in'], POINTER(ICoreWebView2ProfileGetBrowserExtensionsCompletedHandler), 'handler' )),
]

ICoreWebView2ProfileAddBrowserExtensionCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2BrowserExtension), 'result' )),
]

ICoreWebView2ProfileGetBrowserExtensionsCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(ICoreWebView2BrowserExtensionList), 'result' )),
]

ICoreWebView2Settings._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsScriptEnabled',
        ( ['retval', 'out'], LPBOOL, 'isScriptEnabled' )),

    COMMETHOD([], HRESULT, 'put_IsScriptEnabled',
        ( ['in'], BOOL, 'isScriptEnabled' )),

    COMMETHOD([], HRESULT, 'get_IsWebMessageEnabled',
        ( ['retval', 'out'], LPBOOL, 'isWebMessageEnabled' )),

    COMMETHOD([], HRESULT, 'put_IsWebMessageEnabled',
        ( ['in'], BOOL, 'isWebMessageEnabled' )),

    COMMETHOD([], HRESULT, 'get_AreDefaultScriptDialogsEnabled',
        ( ['retval', 'out'], LPBOOL, 'areDefaultScriptDialogsEnabled' )),

    COMMETHOD([], HRESULT, 'put_AreDefaultScriptDialogsEnabled',
        ( ['in'], BOOL, 'areDefaultScriptDialogsEnabled' )),

    COMMETHOD([], HRESULT, 'get_IsStatusBarEnabled',
        ( ['retval', 'out'], LPBOOL, 'uri' )),

    COMMETHOD([], HRESULT, 'put_IsStatusBarEnabled',
        ( ['in'], BOOL, 'isStatusBarEnabled' )),

    COMMETHOD([], HRESULT, 'get_AreDevToolsEnabled',
        ( ['retval', 'out'], LPBOOL, 'areDevToolsEnabled' )),

    COMMETHOD([], HRESULT, 'put_AreDevToolsEnabled',
        ( ['in'], BOOL, 'areDevToolsEnabled' )),

    COMMETHOD([], HRESULT, 'get_AreDefaultContextMenusEnabled',
        ( ['retval', 'out'], LPBOOL, 'enabled' )),

    COMMETHOD([], HRESULT, 'put_AreDefaultContextMenusEnabled',
        ( ['in'], BOOL, 'enabled' )),

    COMMETHOD([], HRESULT, 'get_AreHostObjectsAllowed',
        ( ['retval', 'out'], LPBOOL, 'allowed' )),

    COMMETHOD([], HRESULT, 'put_AreHostObjectsAllowed',
        ( ['in'], BOOL, 'allowed' )),

    COMMETHOD([], HRESULT, 'get_IsZoomControlEnabled',
        ( ['retval', 'out'], LPBOOL, 'enabled' )),

    COMMETHOD([], HRESULT, 'put_IsZoomControlEnabled',
        ( ['in'], BOOL, 'enabled' )),

    COMMETHOD([], HRESULT, 'get_IsBuiltInErrorPageEnabled',
        ( ['retval', 'out'], LPBOOL, 'enabled' )),

    COMMETHOD([], HRESULT, 'put_IsBuiltInErrorPageEnabled',
        ( ['in'], BOOL, 'enabled' )),
]

ICoreWebView2Settings2._methods_ = [
    COMMETHOD([], HRESULT, 'get_UserAgent',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'put_UserAgent',
        ( ['in'], LPCWSTR, 'value' )),
]

ICoreWebView2Settings3._methods_ = [
    COMMETHOD([], HRESULT, 'get_AreBrowserAcceleratorKeysEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_AreBrowserAcceleratorKeysEnabled',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2Settings4._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsPasswordAutosaveEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsPasswordAutosaveEnabled',
        ( ['in'], BOOL, 'value' )),

    COMMETHOD([], HRESULT, 'get_IsGeneralAutofillEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsGeneralAutofillEnabled',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2Settings5._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsPinchZoomEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsPinchZoomEnabled',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2Settings6._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsSwipeNavigationEnabled',
        ( ['retval', 'out'], LPBOOL, 'value' )),

    COMMETHOD([], HRESULT, 'put_IsSwipeNavigationEnabled',
        ( ['in'], BOOL, 'value' )),
]

ICoreWebView2ShowSaveAsUICompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], INT, 'result' )),  # COREWEBVIEW2_SAVE_AS_UI_RESULT
]

ICoreWebView2SourceChangedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_IsNewDocument',
        ( ['retval', 'out'], LPBOOL, 'value' )),
]

ICoreWebView2SourceChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2SourceChangedEventArgs), 'args' )),
]

ICoreWebView2StateChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2DownloadOperation), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2StatusBarTextChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2WebMessageReceivedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Source',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'get_WebMessageAsJson',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),

    COMMETHOD([], HRESULT, 'TryGetWebMessageAsString',
        ( ['retval', 'out'], POINTER(LPWSTR), 'value' )),
]

ICoreWebView2WebMessageReceivedEventArgs2._methods_ = [
    COMMETHOD([], HRESULT, 'get_AdditionalObjects',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2ObjectCollectionView)), 'value' )),
]

ICoreWebView2WebMessageReceivedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2WebMessageReceivedEventArgs2), 'args' )),
]

ICoreWebView2WebResourceRequest._methods_ = [
    COMMETHOD([], HRESULT, 'get_Uri',
        ( ['retval', 'out'], POINTER(LPWSTR), 'uri' )),

    COMMETHOD([], HRESULT, 'put_Uri',
        ( ['in'], LPCWSTR, 'uri' )),

    COMMETHOD([], HRESULT, 'get_Method',
        ( ['retval', 'out'], POINTER(LPWSTR), 'method' )),

    COMMETHOD([], HRESULT, 'put_Method',
        ( ['in'], LPCWSTR, 'method' )),

    COMMETHOD([], HRESULT, 'get_Content',
        ( ['retval', 'out'], POINTER(POINTER(IStream)), 'content' )),

    COMMETHOD([], HRESULT, 'put_Content',
        ( ['in'], POINTER(IStream), 'content' )),

    COMMETHOD([], HRESULT, 'get_Headers',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpRequestHeaders)), 'headers' )),
]

ICoreWebView2WebResourceRequestedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Request',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceRequest)), 'request' )),

    COMMETHOD([], HRESULT, 'get_Response',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceResponse)), 'response' )),

    COMMETHOD([], HRESULT, 'put_Response',
        ( ['in'], POINTER(ICoreWebView2WebResourceResponse), 'response' )),

    COMMETHOD([], HRESULT, 'GetDeferral',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Deferral)), 'deferral' )),

    COMMETHOD([], HRESULT, 'get_ResourceContext',
        ( ['retval', 'out'], LPINT, 'context' )),  # COREWEBVIEW2_WEB_RESOURCE_CONTEXT
]

ICoreWebView2WebResourceRequestedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2WebResourceRequestedEventArgs), 'args' )),
]

ICoreWebView2WebResourceResponse._methods_ = [
    COMMETHOD([], HRESULT, 'get_Content',
        ( ['retval', 'out'], POINTER(POINTER(IStream)), 'content' )),

    COMMETHOD([], HRESULT, 'put_Content',
        ( ['in'], POINTER(IStream), 'content' )),

    COMMETHOD([], HRESULT, 'get_Headers',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpResponseHeaders)), 'headers' )),

    COMMETHOD([], HRESULT, 'get_StatusCode',
        ( ['retval', 'out'], LPINT, 'statusCode' )),

    COMMETHOD([], HRESULT, 'put_StatusCode',
        ( ['in'], INT, 'statusCode' )),

    COMMETHOD([], HRESULT, 'get_ReasonPhrase',
        ( ['retval', 'out'], POINTER(LPWSTR), 'reasonPhrase' )),

    COMMETHOD([], HRESULT, 'put_ReasonPhrase',
        ( ['in'], LPCWSTR, 'reasonPhrase' )),
]

ICoreWebView2WebResourceResponseReceivedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Request',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceRequest)), 'value' )),

    COMMETHOD([], HRESULT, 'get_Response',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2WebResourceResponseView)), 'value' )),
]

ICoreWebView2WebResourceResponseReceivedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2WebResourceResponseReceivedEventArgs), 'args' )),
]

ICoreWebView2WebResourceResponseView._methods_ = [
    COMMETHOD([], HRESULT, 'get_Headers',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2HttpResponseHeaders)), 'headers' )),

    COMMETHOD([], HRESULT, 'get_StatusCode',
        ( ['retval', 'out'], LPINT, 'statusCode' )),

    COMMETHOD([], HRESULT, 'get_ReasonPhrase',
        ( ['retval', 'out'], POINTER(LPWSTR), 'reasonPhrase' )),

    COMMETHOD([], HRESULT, 'GetContent',
        ( ['in'], POINTER(ICoreWebView2WebResourceResponseViewGetContentCompletedHandler), 'handler' )),
]

ICoreWebView2WebResourceResponseViewGetContentCompletedHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], HRESULT, 'errorCode' ),
        ( ['in'], POINTER(IStream), 'result' )),
]

ICoreWebView2WindowCloseRequestedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]

ICoreWebView2Frame._methods_ = [
    COMMETHOD([], HRESULT, 'get_Name',
        ( ['retval', 'out'], POINTER(LPWSTR), 'title' )),

    COMMETHOD([], HRESULT, 'add_NameChanged',
        ( ['in'], POINTER(ICoreWebView2FrameNameChangedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NameChanged',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'AddHostObjectToScriptWithOrigins',
        ( ['in'], LPCWSTR, 'name' ),
        ( ['in'], POINTER(VARIANT), 'object' ),
        ( ['in'], UINT32, 'originsCount' ),
        ( ['in'], POINTER(LPCWSTR), 'origins' )),

    COMMETHOD([], HRESULT, 'RemoveHostObjectFromScript',
        ( ['in'], LPCWSTR, 'name' )),

    COMMETHOD([], HRESULT, 'add_Destroyed',
        ( ['in'], POINTER(ICoreWebView2FrameDestroyedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_Destroyed',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'IsDestroyed',
        ( ['retval', 'out'], POINTER(BOOL), 'destroyed' )),
]

ICoreWebView2FrameContentLoadingEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2ContentLoadingEventArgs), 'args' )),
]

ICoreWebView2FrameDOMContentLoadedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2DOMContentLoadedEventArgs), 'args' )),
]

ICoreWebView2FrameNavigationCompletedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2NavigationCompletedEventArgs), 'args' )),
]

ICoreWebView2FrameNavigationStartingEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2NavigationStartingEventArgs), 'args' )),
]

ICoreWebView2FrameWebMessageReceivedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2WebMessageReceivedEventArgs), 'args' )),
]

ICoreWebView2Frame2._methods_ = [
    COMMETHOD([], HRESULT, 'add_NavigationStarting',
        ( ['in'], POINTER(ICoreWebView2FrameNavigationStartingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NavigationStarting',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_ContentLoading',
        ( ['in'], POINTER(ICoreWebView2FrameContentLoadingEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_ContentLoading',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_NavigationCompleted',
        ( ['in'], POINTER(ICoreWebView2FrameNavigationCompletedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_NavigationCompleted',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'add_DOMContentLoaded',
        ( ['in'], POINTER(ICoreWebView2FrameDOMContentLoadedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_DOMContentLoaded',
        ( ['in'], EventRegistrationToken, 'token' )),

    COMMETHOD([], HRESULT, 'ExecuteScript',
        ( ['in'], LPCWSTR, 'javaScript' ),
        ( ['in'], POINTER(ICoreWebView2ExecuteScriptCompletedHandler), 'handler' )),

    COMMETHOD([], HRESULT, 'PostWebMessageAsJson',
        ( ['in'], LPCWSTR, 'webMessageAsJson' )),

    COMMETHOD([], HRESULT, 'PostWebMessageAsString',
        ( ['in'], LPCWSTR, 'webMessageAsString' )),

    COMMETHOD([], HRESULT, 'add_WebMessageReceived',
        ( ['in'], POINTER(ICoreWebView2FrameWebMessageReceivedEventHandler), 'handler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_WebMessageReceived',
        ( ['in'], EventRegistrationToken, 'token' )),
]

# 3: 2
# 4: 1
# 5: 1
# 6: 2

ICoreWebView2FrameChildFrameCreatedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2FrameCreatedEventArgs), 'args' )),
]

ICoreWebView2Frame7._methods_ = [COMMETHOD([], HRESULT, '_')] * 6 + [
    COMMETHOD([], HRESULT, 'add_FrameCreated',
        ( ['in'], POINTER(ICoreWebView2FrameChildFrameCreatedEventHandler), 'eventHandler' ),
        ( ['out'], POINTER(EventRegistrationToken), 'token' )),

    COMMETHOD([], HRESULT, 'remove_FrameCreated',
        ( ['in'], EventRegistrationToken, 'token' )),
]

ICoreWebView2FrameCreatedEventArgs._methods_ = [
    COMMETHOD([], HRESULT, 'get_Frame',
        ( ['retval', 'out'], POINTER(POINTER(ICoreWebView2Frame)), 'value' )),
]

ICoreWebView2FrameCreatedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2), 'sender' ),
        ( ['in'], POINTER(ICoreWebView2FrameCreatedEventArgs), 'args' )),
]

ICoreWebView2FrameNameChangedEventHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
        ( ['in'], POINTER(ICoreWebView2Frame), 'sender' ),
        ( ['in'], POINTER(IUnknown), 'args' )),
]
