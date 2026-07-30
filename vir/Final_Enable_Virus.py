from winreg import *


#This is Fuction for Disable Usb Storage
def enable_usb_ports():
    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,3)
    CloseKey(key)

#This is Function for Disable CDROM
def enable_cdrom():
    keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,1)
    CloseKey(key)

    
enable_usb_ports()
enable_cdrom()

