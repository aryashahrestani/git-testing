from tkinter import *
import os

win = Tk()
win.geometry("200x50")
win.resizable(0,0)

def shut_down():
    os.system("shutdown /s /t 1")

def Restart():
    os.system("shutdown /r /t 1")

lable1 = Label(win, text="Click on button:  ")
lable1.grid()

button1 = Button(win,text="Shutdown",command=shut_down,bg="yellow")
button1.grid()

button2 = Button(win,text="Restart",command=shut_down,bg="red")
button2.grid(ipadx=10,column=2,row=1)

win.mainloop()
