from tkinter import *
from socket import *

win = Tk()
win.geometry("200x200")
win.resizable(0,0)
win.configure(background="black")

def ip():
    ip = n.get()
    try:
        l2.configure(text=gethostbyname(ip),fg="green")
    except:
        l2.configure(text="Name of Website is false",fg="yellow")

l = Label(win, text="Enter Wbsite: ", fg ="red",bg="black")
l.grid()

n = StringVar()

e = Entry(win, width=32, textvariable=n)
e.grid()

b = Button(win, text="Ckeck",bg="orange",command=ip)
b.grid()

l2 = Label(win, text="",fg="green",bg="black")
l2.grid()


win.mainloop()
