import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry('400x300')
root.title('Clicker')
root.config(bg = 'grey')

count = 0

def colorCheck():
    if count == 0:
        root.config(bg = 'grey')
    elif count > 0:
        root.config(bg = 'green')
    elif count < 0:
        root.config(bg = 'red')

def up():
    global count
    count += 1
    numberCount.set(count)
    colorCheck()

def down():
    global count
    count -= 1
    numberCount.set(count)
    colorCheck()

def bgColor(event):
    root.config(bg = 'yellow')

def bgReset(event):
    colorCheck()

upButton = tk.Button(text= 'Up',font= ('Helvetica', 10),command= up).pack(ipadx=150,ipady=5, pady=30)
numberCount = IntVar(value= count)
numberLabel = Label(textvariable=numberCount,font= ('Helvetica', 10))
numberLabel.bind("<Enter>", bgColor)
numberLabel.bind("<Leave>", bgReset)
numberLabel.pack(ipadx=150,ipady=5)

downButton = tk.Button(text= 'Down',font= ('Helvetica', 10),command= down).pack(ipadx=140,ipady=5,pady=35)

root.mainloop()