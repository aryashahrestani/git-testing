from winreg import *

#This is Function for Disable CDROM
def disable_cdrom():
    keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,4)
    CloseKey(key)
disable_cdrom()
