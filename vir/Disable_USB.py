from winreg import *

def disable_usb_ports():
    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,4)
    CloseKey(key)
disable_usb_ports()
