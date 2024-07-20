from tkinter import *
from tkinter.messagebox import showinfo, showerror
import random

win = Tk()
win.title("ROCK PAPER SCISSOR")
win.geometry("800x800")

dic = {1: "rock", 2: "paper", 3: "scissor"}
userscore = 0
cmpscore = 0
userchoice = 0
cmpchoice = 0
userwin = 1

def winner(userwin):
    if userwin == 1:
        showinfo(title="Winner", message="You are the winner!")
    elif userwin == 0:
        showinfo(title="Winner", message="Computer is the winner!")
    else:
        showinfo(title="Winner", message="It's a draw!")

def getchoice(userchoice):
    global dic
    global userscore
    global cmpscore
    global userwin
    cmpchoice = random.randint(1, 3)
    
    if dic[userchoice] == "rock":
        if dic[cmpchoice] == "scissor":
            userscore += 1
            userwin = 1
        elif dic[cmpchoice] == "paper":
            cmpscore += 1
            userwin = 0
        else:
            userwin = 2
    elif dic[userchoice] == "paper":
        if dic[cmpchoice] == "rock":
            userscore += 1
            userwin = 1
        elif dic[cmpchoice] == "scissor":
            cmpscore += 1
            userwin = 0
        else:
            userwin = 2
    else:  # scissor
        if dic[cmpchoice] == "rock":
            cmpscore += 1
            userwin = 0
        elif dic[cmpchoice] == "paper":
            userscore += 1
            userwin = 1
        else:
            userwin = 2
    
    yp.config(text=str(userscore))
    cp.config(text=str(cmpscore))
    winner(userwin)

img1 = PhotoImage(file="C:\\Users\\91939\\Downloads\\rockn.png")
im1 = Button(image=img1, command=lambda: getchoice(1))
im1.place(x=35, y=10, height=300, width=300)

img2 = PhotoImage(file="C:\\Users\\91939\\Downloads\\papern.png")
im2 = Button(image=img2, command=lambda: getchoice(2))
im2.place(x=450, y=10, height=300, width=300)

img3 = PhotoImage(file="C:\\Users\\91939\\Downloads\\ssc.png")
im3 = Button(image=img3, command=lambda: getchoice(3))
im3.place(x=250, y=340, height=300, width=300)

y = Label(win, text="You", font=(40))
y.place(x=20, y=360)
yp = Label(win, text="", font=(40))
yp.place(x=200, y=360)

c = Label(win, text="Computer", font=(40))
c.place(x=20, y=400)
cp = Label(win, text="", font=(40))
cp.place(x=200, y=400)

win.mainloop()
