from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

file = open(b'hacker.jpg','rb')

data=file.read()

file.close()

file_2 = open(b'hacker_enc.jpg','wb')

f= Fernet(key)

enc = f.encrypt(data)

file_2.write(enc)

file_2.close()
