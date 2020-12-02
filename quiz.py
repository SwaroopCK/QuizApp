import tkinter
from tkinter import *
import random

questions = [
    "The series Friends is set in which city?",
    "What pet did Ross own?",
    "Monica briefly dates billionaire Pete Becker. Which country does he take her for their first date?",
    "Rachel was popular in high school. Her prom date Chip ditched her for which girl at school?",
    "Which cartoon character was on Phoebe’s thermos that Ursula threw under a bus?",
    " What song is Phoebe best known for?",
    "Which Friends character plays Dr. Drake Ramoray on the show Days Of Our Lives?",
    " Who was Chandler’s TV magazine always addressed to?",
    "Who sang the Friends theme?",
    "What kind of uniform does Joey wear to Monica and Chandler’s wedding?",
]

answers_ch = [
    ["1","2","3","4",],
    ["1","2","3","4",],
    ["1","2","3","4",],
    ["1","2","3","4",],
    ["Pebbles Flintstone","Yogi Bear","Judy Jetson","Bullwinkle",],
    ["Smelly Cat","Smelly Dog","Smelly Rabbit","Smelly Worm",],
    ["Ross Geller","Pete Becker","Eddie Menuek","Joey Tribbiani",],
    ["Chanandler Bong","Chanandler Bang","Chanandler Bing","Chanandler Beng",],
    ["The Banksys","The Rembrandts","The Constables","The Da Vinci Band",],
    ["Chef","Soldier","Fire fighter","A baseball player",],
]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

ques = 1
def selected():
    global radiovar,user_answer
    global lblq,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    #print(x)
    user_answer.append(x)
    if ques < 5:
        lblq.config(text = questions[indexes[ques]])
        r1['text'] = answers_ch[indexes[ques]][0]
        r2['text'] = answers_ch[indexes[ques]][1]
        r3['text'] = answers_ch[indexes[ques]][2]
        r4['text'] = answers_ch[indexes[ques]][3]
        ques += 1 
    else:
        pass

def startquiz():
    global lblq,r1,r2,r3,r4
    lblq = Label(
        root,
        text = questions[indexes[0]],
        font = ("consolas",16),
        width = 500,
        justify = "center",
        wraplength = 400,
    )
    lblq.pack()

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_ch[indexes[0]][0],
        font = ("Times" , 12),
        value = 0,
        variable = radiovar,
        command = selected,
    )
    r1.pack(pady = (40,0))

    r2 = Radiobutton(
        root,
        text = answers_ch[indexes[0]][1],
        font = ("Times" , 12),
        value = 1,
        variable = radiovar,
        command = selected,
    )
    r2.pack(pady = (40,0))

    r3 = Radiobutton(
        root,
        text = answers_ch[indexes[0]][2],
        font = ("Times" , 12),
        value = 2,
        variable = radiovar,
        command = selected,
    )
    r3.pack(pady = (40,0))

    r4 = Radiobutton(
        root,
        text = answers_ch[indexes[0]][3],
        font = ("Times" , 12),
        value = 3,
        variable = radiovar,
        command = selected,
    )
    r4.pack(pady = (40,0))



def startIsPressed():
    labelimage.destroy()
    labelText.destroy()
    lblRules.destroy()
    lblInstruction.destroy()
    btnstart.destroy()
    gen()
    startquiz()

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