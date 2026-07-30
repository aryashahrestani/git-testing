from cryptography.fernet import Fernet

key = b'ypNVkNRZrgrXcoRToB4OWDVxasbYxk0BvxGYTsQK0qE='

#this section related Cipher-Text
c = b'gAAAAABg3cxLy2SmqreRjjjxjxAuVnETTZoD05lMnV4qXL4gxirrwBefCPSvLc4T9vCZZsYJl5VLp2gW9MI7x5MAQK1kik4nCA=='

f = Fernet(key)

dec = f.decrypt(c)

print(dec)
