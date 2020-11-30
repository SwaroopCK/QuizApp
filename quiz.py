import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Quiz App")
root.geometry("700x600")
root.config(background="white")

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
    border = 0.0
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

root.mainloop()