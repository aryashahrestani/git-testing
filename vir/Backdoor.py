from winreg import *

def run_app():
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER,keyVal)
    SetValueEx(key,"notepad",0,REG_SZ,"C:\\Windows\\System32\\Notepad.exe")
    CloseKey(key) 
run_app()
