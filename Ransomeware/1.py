import cryptography.fernet

key = cryptography.fernet.Fernet.generate_key()

print(key,'\n')

s = b'hello world'

f = cryptography.fernet.Fernet(key)

enc = f.encrypt(s)

print(enc)
