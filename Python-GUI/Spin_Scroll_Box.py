from tkinter import scrolledtext
from tkinter import *

win =Tk()
win.geometry("300x300")

def insert():
    value = spin.get() 
    s.insert(INSERT , value+'\n')

spin = Spinbox(win , from_=0 , to=10 , bd=8 , width=15,command=insert)
spin.grid(column=2,row=3)

s= scrolledtext.ScrolledText (win, width=15,height=15,bg="black",fg="green")
s.grid(row=3)

win.mainloop()
