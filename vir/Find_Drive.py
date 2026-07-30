from subprocess import check_output

def system_drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    sys_drive=[]
    #cmd = check_output("net share",shell=True)
    cmd = check_output("wmic logicaldisk get name", shell=True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)
    return(sys_drive)

drive=system_drive()
print (drive)
