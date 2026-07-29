from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x300")
def check():

         e_name = ename.get()
         c_name = cname.get()
    
         if c_name == "male":
        
                l2=Label(win,text="Hello MR."+e_name).grid()
         elif c_name == "famel":
                l2=Label(win,text="Hello MS."+e_name).grid()
        
l=Label(win, text="enter name:")
l.grid()
ename=StringVar()
e = Entry (win, width=10 , textvariable=ename)
e.grid(column=1)
cname=StringVar()
c = ttk.Combobox(win,width=15,values=("male","female"),textvariable=cname)
c.grid(column=1,row=5)
b=Button(win,text="hello",command=check)
b.grid()
win.mainloop()
