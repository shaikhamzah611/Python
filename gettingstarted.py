from tkinter import *
from datetime import date

root = Tk()
root.title('JOB APLICATION')
root.geometry('300x300')

lbl = Label(text = "HELLO THERE",fg = "white",bg = "#4D719B",height=3,width=300)

name_lbl = Label(text="PLEASE ENTER YOUR FULL NAME",bg="#555BAD")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "WELCOME TO THE APPLICATION! \nTODAYS DATE IS: "
    greet = " HELLO "+name+" \n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box = Text(height=4)

btn = Button(text="BEGIN",command=display,height=3,bg="blue",fg="white")

lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()

root.mainloop()