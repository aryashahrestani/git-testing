import subprocess as sub


def find_drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    sys_drive=[]
    cmd =sub.check_output("net share",shell=True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)

    return sys_drive


def find_files(drivers):

    for p in passwand:
            
            try:
                cmd = sub.check_output("cd / && dir /S /B *."+p,shell=True)
                f.write(cmd)
                print(p)
            except:
                pass

    for d in drivers:
        for p in passwand:

            try:
                cmd = sub.check_output(d+" && dir /S /B *."+p,shell=True)
                f.write(cmd)
                print(d+'-------'+p)
            except:
                pass
            
    
    
passwand=["txt"]

drivers = find_drive()

f = open("paths.txt","wb")

find_files(drivers)
