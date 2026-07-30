import smtplib

USER="noone@gmail.com"
PASS="12345"

FROM = USER
TO = ["any@gmail.com"]

message = "this is a code for send gmail"


server = smtplib.SMTP()
server.connect("smtp.gmail.com",587)
server.starttls()
server.login(USER,PASS)
server.sendmail(FROM, TO, message)
server.quit()
