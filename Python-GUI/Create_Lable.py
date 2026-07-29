from tkinter import *

win = Tk()

lable1 = Label(win, text="Hello World!", fg="red", bg="yellow")
lable1.grid(ipadx="4", ipady="10")

lable2 = Label(win, text="Hello World!", fg="blue", bg="orange")
lable2.grid()

win.mainloop()