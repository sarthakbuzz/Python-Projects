from googletrans import Translator
from gtts import gTTS
from tkinter import *


window=Tk()
window.geometry("600x280")
window.title("Translator")
bg_color="#074463"
window.config(bg=bg_color)

e1=Entry(window,bg="white",bd=2,fg="black",font=("arial",15,"bold"))
e1.place(x=20,y=20)

def convert_language():
    a1=e1.get()
    t1=Translator()
    t2=click_option.get()
    
    if t2=="English":
        convert="en"
    elif t2=="Hindi":
        convert="hi"
    elif t2=="German":
        convert="de"
    elif t2=="Spanish":
        convert="es"
    elif t2=="Russian":
        convert="ru"
    
    trans_text=t1.translate(a1,dest=convert)
    trans_text=trans_text.text
    ob1=gTTS(text=trans_text,slow=False,lang=convert)
    
    F2.config(text=trans_text)
    
    
choices=[
    "English",
    "Hindi",
    "German",
    "French",
    "Spanish",
    "Russian"
]

click_option=StringVar()
click_option.set("Select Language")

list_drop=OptionMenu(window,click_option,*choices)
list_drop.configure(background="green",foreground="white",font=("arial",15,"bold"))
list_drop.place(x=400,y=20)

F2=Label(window,text="\t\t\t\t\t\t\t\t",bg="black",fg="white",font=("arial",20,"bold"))
F2.place(x=0,y=120)
F2=Label(window,text="Translated text",bg="black",fg="white",font=("arial",20,"bold"))
F2.place(x=180,y=120)

btn_1=Button(window,text="Translate",bd=2,bg="blue",fg="white",font=("arial",20,"bold"),command=convert_language)
btn_1.place(x=200,y=180)

window= mainloop()