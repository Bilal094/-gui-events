import tkinter as tk
from tkinter import *
from random import *
from tkinter import messagebox

# Variables
time20 = 20
score = 0
letters = ['w', 'a', 's', 'd', 'space']
mouse = {'Button-1' : 'Click', 'Double-Button' : 'Double click', 'Triple-Button' : 'Triple click'}
mouseOrKey = ['Mouse', 'Key']
# Root configuration
root = tk.Tk()
root.title("Simple FPS trainer")
root.geometry("1050x650")
root.resizable(False, False)

def scoreAdd(widget):
    global score
    if widget == 'button':
        score += 1
        scoreDisplay.config(text=f'Score: {score}')
    elif widget == 'label':
        score += 2
        scoreDisplay.config(text=f'Score: {score}')

def time():
    global time20, score
    if time20 == 0:
        gameEnd = messagebox.askyesno('Game ended', f'You scored {score} points. Do you want to play again?')
        if gameEnd == True:
            score = 0
            time20 = 20
        else:
            root.destroy()
    time20 -= 1
    timeVar.get()
    time20 = time20
    timeVar.set(f'Time remaining: {time20}')
    root.after(1000, time)

def keyLabel(letter,posX,posY):
    global randomButton, randomLabel, score
    if time20 == 20:
        time()
    if letter in letters:
        randomLabel = Label(root,text=f'Press {letter}', font=('Helvetica', 14), relief='ridge', borderwidth= '5')
        randomLabel.place(x=posX,y=posY)
        root.bind(f'<{letter}>', lambda event: [root.unbind(f'<{letter}>'), randomLabel.destroy(), scoreAdd('label'), keyBind()])
    elif letter in mouse:
        randomButton = Button(text=f'{mouse[letter]}', font=('Helvetica', 14))
        randomButton.place(x=posX,y=posY)
        randomButton.bind(f'<{letter}>', lambda event: [randomButton.unbind(f'{letter}'), randomButton.destroy(), scoreAdd('button'), keyBind()])

def keyBind():
    startBtn.destroy()
    mouseOrKeyChoice = choice(mouseOrKey)
    if mouseOrKeyChoice == 'Key':
        randomX = randrange(5,950)
        randomY = randrange(40,600)
        randomLetter = choice(letters)
        keyLabel(randomLetter,randomX,randomY)
    elif mouseOrKeyChoice == 'Mouse':
        randomX = randrange(5,950)
        randomY = randrange(40,600)
        randomMouse = choice(list(mouse))
        keyLabel(randomMouse,randomX,randomY)

# Labels, button and frame
blackFrame = Frame(bg='black')
timeVar = StringVar(value=f'Time remaining: {time20}')
scoreDisplay = tk.Label(blackFrame, text=f'Score: {score}',font= ('Helvetica', 15), bg = 'black', fg = 'white')
timeDisplay = tk.Label(blackFrame, textvariable=timeVar,font= ('Helvetica', 15), bg = 'black', fg = 'white')
startBtn = tk.Button(root, text='Press here to start', font=('Helvetica', 14), command= keyBind)

# Widget placement
startBtn.place(x=450,y=300)
scoreDisplay.place(x=10,y=5)
timeDisplay.place(x=450,y=5)
blackFrame.pack(fill ='x', ipady=20)

root.mainloop()