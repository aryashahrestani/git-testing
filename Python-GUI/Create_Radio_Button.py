from tkinter import *

win = Tk()
win.geometry("300x300")
def color():
    color = rad1.get()
    if color ==1:
        win.configure(background="red")
        r.configure(bg="red")
        r1.configure(bg="red")
        r2.configure(bg="red")
    elif color ==2:
        win.configure(background="blue")
        r.configure(bg="blue")
        r1.configure(bg="blue")
        r2.configure(bg="blue")
    elif color ==3:
        win.configure(background="yellow")
        r.configure(bg="yellow")
        r1.configure(bg="yellow")
        r2.configure(bg="yellow")
        
rad1=IntVar()
r= Radiobutton(win , text="red",variable=rad1,value=1,command=color)
r.grid(column=0,row=0)

r1=Radiobutton(win,text="blue",variable=rad1,value=2,command=color)
r1.grid(column=1,row=2)

r2 = Radiobutton(win,text="yellow",variable=rad1,value=3,command=color)
r2.grid(column=2,row=0)

win.mainloop()
