from tkinter import *

win = Tk()

button1 = Button(win, text="Start", fg="blue",bg="yellow").pack(ipadx=5,ipady=5,padx="10cm",pady="30px")
button2 = Button(win, text="Start", fg="blue",bg="gray").pack(side="right")

win.mainloop()