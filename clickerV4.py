import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry('400x300')
root.title('Clicker')
root.config(bg = 'grey')

count = 0
labelClicked = 0
downButtonStatus = False
upButtonStatus = False

def colorCheck():
    if count == 0:
        root.config(bg = 'grey')
    elif count > 0:
        root.config(bg = 'green')
    elif count < 0:
        root.config(bg = 'red')

def up(event = None):
    global count, upButtonStatus, downButtonStatus
    upButtonStatus = True
    downButtonStatus = False
    count += 1
    numberCount.set(count)
    colorCheck()

def down(event = None):
    global count, downButtonStatus, upButtonStatus
    downButtonStatus = True
    upButtonStatus = False
    count -= 1
    numberCount.set(count)
    colorCheck()

def bgColor(event):
    root.config(bg = 'yellow')

def bgReset(event):
    colorCheck()


def labelTriple(event):
    global count, labelClicked, upButtonStatus, downButtonStatus
    labelClicked += 1
    if labelClicked == 1:
        labelClicked -= labelClicked
        if upButtonStatus == True:
            count *= 3
            numberCount.set(count)
        elif downButtonStatus == True:
            count /= 3
            numberCount.set(count)

# Up button
upButton = tk.Button(text= 'Up',font= ('Helvetica', 10),command= up)
root.bind("+", up)
upButton.pack(ipadx=150,ipady=5, pady=30)

# Number label
numberCount = IntVar(value= count)
numberLabel = Label(textvariable=numberCount,font= ('Helvetica', 10))
numberLabel.bind("<Enter>", bgColor)
numberLabel.bind("<Leave>", bgReset)
numberLabel.bind("<Double-Button-1>", labelTriple)
root.bind("<space>", labelTriple)
numberLabel.pack(ipadx=150,ipady=5)

# Down button
downButton = tk.Button(text= 'Down',font= ('Helvetica', 10),command= down)
root.bind("-", down)
downButton.pack(ipadx=140,ipady=5,pady=35)

root.mainloop()