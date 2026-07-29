from tkinter import *
win =Tk()
win.geometry("200x200")
s= Listbox(win , width=15)
s.pack()

s.insert(END,"hello world")

for i in ["cisco" ,'python' , 'programmer']:
    s.insert(END , i)
    
win.mainloop()