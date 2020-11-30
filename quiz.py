import tkinter
from tkinter import *

def startIsPressed():
    labelimage.destroy()
    labelText.destroy()
    lblRules.destroy()
    lblInstruction.destroy()
    btnstart.destroy()

root = tkinter.Tk()
root.title("Quiz App")
root.geometry("700x600")
root.config(background="white")
root.resizable(0,0)

img1 = PhotoImage(file="hat.png")
labelimage = Label(
    root,
    image = img1,
    background = "white"
)
labelimage.pack(pady=(40,0))

labelText = Label(
    root,
    text = "QuizApp",
    font = ("comic sans MS" , 24 , "bold"),
    background = "white"
)
labelText.pack(pady=(0,50))

img2 = PhotoImage(file = "Frame.png")
btnstart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0.0,
    command = startIsPressed
)
btnstart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules \n Start The game Once you are Ready",
    background = "white",
    font = ("consolas",14),
    justify = "center"
)
lblInstruction.pack()

lblRules = Label(
    root,
    text = "° This quiz contains 10 questions\n° You will 20 seconds to solve a question\n° Once you select a choice that will be final choice\n° Think Before you select",
    width = 100, 
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack(pady = (110,0))
root.mainloop()