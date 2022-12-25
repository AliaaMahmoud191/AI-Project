from tkinter import*
from PIL import Image,ImageTk
from random import randint

myFont=("Calibri", 30, "bold")

window = Tk()
window.title("Stone, Paper and Scissors!")
window.configure(bg="#100f1f")

playerScore=0
computerScore=0
#
scissorswinImage=ImageTk.PhotoImage(Image.open("./images/scissorswin (2).jpg"))
StonewinImage=ImageTk.PhotoImage(Image.open("./images/stonewin (2).jpg"))
paperwinImage=ImageTk.PhotoImage(Image.open("./images/paperwin.jpg"))

scissorslostImage=ImageTk.PhotoImage(Image.open("./images/scissorslost.jpg"))
StonelostImage=ImageTk.PhotoImage(Image.open("./images/stonelost.jpg"))
paperlostImage=ImageTk.PhotoImage(Image.open("./images/paperlost.jpg"))

label_player=Label(window, image=scissorswinImage)
label_computer=Label(window,image=scissorslostImage)
label_computer.grid(row=1,column=0)
label_computer.grid(row=1,column=4)

computerScore=label(window,text=0,font=myFont,text="Computer",bg="#100f1f")
playerScore=label(window,text=0,font=myFont,text="Player",bg="#100f1f")

computerScore.grid(row=1,column=0)
playerScore.grid(row=1,column=3)



def updateImages_ShowScore():
    


#Creating Elements for Frame3
scissorsBtn= Button(window,width=16,height=3, text="Scissors", font=myFont, borderwidth = 0,bg="white" , command=lambda: StartGame("scissors")).grid(row=2,column=1)
stoneBtn= Button(window, width=16,height=3,text="Stone", font=myFont, borderwidth = 0, bg="white", command=lambda: StartGame("stone")).grid(row=2,column=2)
paperBtn= Button(window, width=16,height=3,text="Paper", font=myFont, borderwidth = 0,bg="white", command=lambda: StartGame("paper")).grid(row=2,column=3)

window.mainloop()