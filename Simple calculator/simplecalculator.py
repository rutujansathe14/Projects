from tkinter import*


root = Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.iconbitmap('E:/projects/Simple calculator/simple calculator.ico')

global svalue
svalue=StringVar()
svalue.set("")
screen=Entry(root,textvariable=svalue,font=('Verdana',25))
screen.pack(fill=X,padx=10,pady=10,ipadx=20)


#click 
def click(event):
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if svalue.get().isdigit():
            value=int(svalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="ERROR"
                

        svalue.set(value)
        screen.update()
    elif text=="C":
        svalue.set("")
        screen.update()
    elif text=="⌫":
        value=svalue.get()
        svalue.set(value[0:len(value)-1])
        screen.update()

    else:
        svalue.set(svalue.get()+text)
        screen.update()



#button frame
frame=Frame(root,bg="")
#creating buttons
button=Button(frame,text="C",font='Verdana',padx=20,pady=20,bg="light blue")
button.grid(row=1,column=1,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="⌫",font='Verdana',padx=20,pady=20)
button.grid(row=1,column=2,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="/",font='Verdana',padx=20,pady=20,bg="pale green")
button.grid(row=1,column=3,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="7",font='Verdana',padx=20,pady=20)
button.grid(row=2,column=0,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="8",font='Verdana',padx=20,pady=20)
button.grid(row=2,column=1,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="9",font='Verdana',padx=20,pady=20)
button.grid(row=2,column=2,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="*",font='Verdana',padx=20,pady=20,bg="pale green")
button.grid(row=2,column=3,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="4",font='Verdana',padx=20,pady=20)
button.grid(row=3,column=0,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="5",font='Verdana',padx=20,pady=20)
button.grid(row=3,column=1,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="6",font='Verdana',padx=20,pady=20)
button.grid(row=3,column=2,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="-",font='Verdana',padx=20,pady=20,bg="pale green")
button.grid(row=3,column=3,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="1",font='Verdana',padx=20,pady=20)
button.grid(row=4,column=0,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="2",font='Verdana',padx=20,pady=20)
button.grid(row=4,column=1,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="3",font='Verdana',padx=20,pady=20)
button.grid(row=4,column=2,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="+",font='Verdana',padx=20,pady=20,bg="pale green")
button.grid(row=4,column=3,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="%",font='Verdana',padx=20,pady=20)
button.grid(row=5,column=0,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="0",font='Verdana',padx=20,pady=20)
button.grid(row=5,column=1,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text=".",font='Verdana',padx=20,pady=20)
button.grid(row=5,column=2,padx=5,pady=10)
button.bind("<Button 1>",click)

button=Button(frame,text="=",font='Verdana',padx=20,pady=20,bg="red")
button.grid(row=5,column=3,padx=5,pady=10)
button.bind("<Button 1>",click)


frame.pack()



root.mainloop()