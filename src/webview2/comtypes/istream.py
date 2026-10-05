from ctypes import *
from ctypes.wintypes import FILETIME, LARGE_INTEGER, ULARGE_INTEGER
from . import IUnknown, COMMETHOD
from .GUID import GUID

class STATSTG(Structure):
    _fields_ = [
        ('pwcsName', c_wchar_p),
        ('type', c_ulong),
        ('cbSize', ULARGE_INTEGER),
        ('mtime', FILETIME),
        ('ctime', FILETIME),
        ('atime', FILETIME),
        ('grfMode', c_ulong),
        ('grfLocksSupported', c_ulong),
        ('clsid', GUID),
        ('grfStateBits', c_ulong),
        ('reserved', c_ulong),
    ]

class ISequentialStream(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []

class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []

ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'Read',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'Write',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]

IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(STATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
