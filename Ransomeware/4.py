from cryptography.fernet import Fernet

key = b'IxYtzXqKFFiqbCcDmjmp4ZpEPWemkKjV0VNQBvgAcVI='

file = open(b'hacker_enc.jpg','rb')

data = file.read()

file.close()

file_2 = open(b'hacker.jpg','wb')

f = Fernet(key)

dec = f.decrypt(data)

file_2.write(dec)

file_2.close()

