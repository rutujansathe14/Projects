from tkinter import *
import random


#Main Screen
root=Tk()
root.title('Rock Paper Scissors')
root.iconbitmap('images/rps icon.ico')
#root.geometry("903x200")
root.resizable(width=False,height=False)

global click
click=True

#player
rock_img=PhotoImage(file='images/rock1.png')
paper_img=PhotoImage(file='images/paper1.png')
scissors_img=PhotoImage(file='images/scissors1.png')

#opposite
rock_comp=PhotoImage(file='images/rock2.png')
paper_comp=PhotoImage(file='images/paper2.png')
scissors_comp=PhotoImage(file='images/scissors2.png')

#win lose
win_img=PhotoImage(file='images/win.png')
lose_img=PhotoImage(file='images/lose.png')
tie_img=PhotoImage(file='images/tie.png')



def reset():
    #if my_choice=='rock' or my_choice=='paper' or my_choice=='scissors':
        rock_btn.configure(image=rock_img)
        paper_btn.configure(image=paper_img)
        scissors_btn.configure(image=scissors_img)
        global click
        click=True
    
reset_btn=Button(root,text='Reset Game',command=reset)
reset_btn.grid(row=1,column=0,pady=10)

def play():
    global rock_btn , paper_btn , scissors_btn
    rock_btn=Button(root,image=rock_img,command=lambda:you_pick('rock'))
    paper_btn=Button(root,image=paper_img,command=lambda:you_pick('paper'))
    scissors_btn=Button(root,image=scissors_img,command=lambda:you_pick('scissors'))

    rock_btn.grid(row=0,column=0)
    paper_btn.grid(row=0,column=1)
    scissors_btn.grid(row=0,column=2)
    


def computer_pick():
    choice= random.choice(['rock','paper','scissors'])
    return choice

def you_pick(my_choice):
    global click

    comp_pick=computer_pick()

    if click==True:
        if my_choice=='rock':
            rock_btn.configure(image=rock_img)
            if comp_pick=='rock':
                paper_btn.configure(image=rock_comp)
                scissors_btn.configure(image=tie_img)
                click=False
            elif comp_pick=='paper':
                paper_btn.configure(image=paper_comp)
                scissors_btn.configure(image=lose_img)
                click=False
            elif comp_pick=='scissors':
                paper_btn.configure(image=scissors_comp)
                scissors_btn.configure(image=win_img)
                click=False
        elif my_choice=='paper':
            rock_btn.configure(image=paper_img)
            if comp_pick=='rock':
                paper_btn.configure(image=rock_comp)
                scissors_btn.configure(image=win_img)
                click=False
            elif comp_pick=='paper':
                paper_btn.configure(image=paper_comp)
                scissors_btn.configure(image=tie_img)
                click=False
            elif comp_pick=='scissors':
                paper_btn.configure(image=scissors_comp)
                scissors_btn.configure(image=lose_img)
                click=False
        elif my_choice=='scissors':
            rock_btn.configure(image=scissors_img)
            if comp_pick=='rock':
                paper_btn.configure(image=rock_comp)
                scissors_btn.configure(image=lose_img)
                click=False
            elif comp_pick=='paper':
                paper_btn.configure(image=paper_comp)
                scissors_btn.configure(image=win_img)
                click=False
            elif comp_pick=='scissors':
                paper_btn.configure(image=scissors_comp)
                scissors_btn.configure(image=tie_img)
                click=False
    else:
        reset()

play()



root.mainloop()