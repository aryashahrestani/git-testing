from tkinter import *

win = Tk()
win.geometry("700x800")

photo = PhotoImage(file='banana.png')

lable1 = Label(win, text="Hello World!", fg="red", bg="yellow")
lable1.grid(ipadx="4", ipady="10")

lable2 = Label(win, text="Hello World!", fg="blue", bg="orange")
lable2.grid()

win.mainloop()