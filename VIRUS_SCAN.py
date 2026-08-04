from tkinter import messagebox
from tkinter import *

root = Tk()
root.geometry("100x100")

def msg():
    messagebox.showwarning("Alert", "We found a virus from China")

button = Button(root,text = "Scan for Virus",command=msg)
button.place(x=20,y=20)

root.mainloop()