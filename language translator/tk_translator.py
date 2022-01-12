from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import googletrans
import textblob


root=Tk()
root.title("Language Translator")
#root.geometry("1100x700")
root.resizable(False,False)
root.iconbitmap('icon.ico')

#translate function
def translate_text():
    global language
    try:
        text1=text_box1.get(1.0,END)
        L1=combo1.get()
        L2=combo2.get()
        if text1:
            text2=textblob.TextBlob(text1)
            lan=text2.detect_language()
            for i,j in language.items():
                if j==L2:
                    lan2=i
            text2=text2.translate(from_lang=lan,to=lan2)
            text_box2.delete(1.0,END)
            text_box2.insert(END,text2)
    except Exception as e:
        messagebox.showerror("Language Translator","ERROR!\nPlease try again")



#language list
language=googletrans.LANGUAGES
lang_list=list(language.values())
lang=language.keys

#combo box 1
combo1=ttk.Combobox(root,values=lang_list,font=("Century",25),state="r")
combo1.grid(row=0,column=0,padx=20,pady=20)
combo1.set("English")

#combo box 2
combo2=ttk.Combobox(root,values=lang_list,font=("Century",25),state="r")
combo2.grid(row=0,column=3,padx=20,pady=20)
combo2.set("SELECT LANGUAGE")

#frame 1
text_frame1=Frame(root)
text_frame1.grid(row=1,column=0,padx=20,pady=20,sticky="nesw")

#text box 1
text_box1=Text(text_frame1,font="Century",bg="light grey",relief=GROOVE,wrap=WORD,width=45,height=12)
text_box1.grid(row=1,column=0)

#scroll bar 1
scrollbar1=ttk.Scrollbar(text_frame1,orient=VERTICAL,command=text_box1.yview)
scrollbar1.grid(row=1,column=1,rowspan=4,sticky="ns")
text_box1.configure(yscrollcommand=scrollbar1.set)
#text_box1.bind('<Configure>',lambda e: text_box1.configure(scrollregion= text_box1.bbox("all")))


#frame 2
text_frame2=Frame(root)
text_frame2.grid(row=1,column=3,padx=20,pady=20,sticky="nesw")

#text box 2
text_box2=Text(text_frame2,font="Century",bg="light grey",relief=GROOVE,wrap=WORD,width=45,height=12)
text_box2.grid(row=1,column=0)

#scroll bar 2
scrollbar2=ttk.Scrollbar(text_frame2,orient=VERTICAL,command=text_box2.yview)
scrollbar2.grid(row=1,column=1,rowspan=4,sticky="ns")
text_box2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate_btn=Button(root,text="Translate",font=("Century",20),bg="lime green",command=translate_text)
translate_btn.grid(row=2,columnspan=4,pady=20)

root.mainloop()