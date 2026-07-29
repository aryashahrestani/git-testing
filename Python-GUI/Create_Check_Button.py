from tkinter import *
win =Tk()
win.geometry("200x200")
ch=IntVar()
c= Checkbutton(win, text="test", state="disable",variable=ch) # disable
c.select()
c.grid()

ch1 =IntVar()
c = Checkbutton(win, text="test1", state="active",variable=ch1)
c.deselect()
c.grid()

ch2 = IntVar()
c = Checkbutton(win, text="test2", variable=ch2)
c.grid()

win.mainloop()
