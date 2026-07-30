from winreg import *
from os import system

def show_reg_backdoor():
    aKey = OpenKey(HKEY_LOCAL_MACHINE,r"Software\Microsoft\Windows\CurrentVersion\Run", 0,KEY_READ)
    for i in range(2000):
        try:
            Name,Value,Code = EnumValue(aKey,i)
            print("Num=%d\tName=\'%s\'\tPath=\'%s\'" % (i, Name, Value))
        except:
            pass
show_reg_backdoor()
system("PAUSE")
