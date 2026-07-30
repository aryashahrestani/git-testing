from winreg import *

def enable_cdrom():
    keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,1)
    CloseKey(key)
enable_cdrom()
