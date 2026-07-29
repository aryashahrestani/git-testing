from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

win = Tk()
win.geometry("500x500")

def open_file():
    
    file = tkFileDialog.askopenfile(parent=win , mode="r",title="select my file")
    data=file.read()
    s.insert(INSERT,data)
    file.close()

def save_file():
    
    data = s.get("1.0".END)
    file = tkFileDialog.asksavefile(mode="w")
    file.write(data)
    file.close()
    
s=ScrolledText(win, width=40)
s.grid()

b=Button(win,text="open",command=open_file)
b.grid()

b2=Button(win,text="save" , command=save_file)
b2.grid()

win.mainloop()

