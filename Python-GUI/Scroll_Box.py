from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

win =Tk()
win.geometry("500x400")
win.resizable(0,0)

s = ScrolledText(win , width=70, height=27)
s.grid()

def open_file(): 
    file = tkFileDialog.askopenfile(parent=win,mode="r",title="select file")
    data = file.read()
    s.insert(INSERT,data)
    file.close()
    
def red():
    s.configure(bg="red")
def green():
    s.configure(bg="green")
def black():
    s.configure(bg="black",fg="green")

menu = Menu(win)
win.configure(menu=menu)

file = Menu(menu)
menu.add_cascade(label="file",menu=file)
file.add_command(label="new")
file.add_command(label="open",command=open_file)
file.add_command(label="exit")

color = Menu(menu)
menu.add_cascade(label="color",menu=color)
color.add_command(label="red",command=red)
color.add_command(label="green",command=green)
color.add_command(label="black",command=black)

win.mainloop()





