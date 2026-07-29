from tkinter import *

win =Tk()
win.geometry("300x300")

def insert_m():
    value = message.get()
    t.insert(INSERT , value)
    
message=StringVar()
e = Entry(win , width=14,textvariable=message)
e.grid(column=0,row=0)

b= Button(win , text="insert" , command=insert_m)
b.grid(column=1,row=0)

t= Text(win , width=25, height=10,bg="black",fg="green")
t.grid()

win.mainloop()
 
