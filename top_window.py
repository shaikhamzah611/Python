from tkinter import *

root = Tk()
root.title("main")
root.geometry("400x300")

def topwin():
    top = Toplevel(root)
    top.geometry("180x180")
    top.title("Top Level")

    l2 = Label(top,text="This is a toplevel window,Nothing")
    l2.pack()
    top.mainloop()

l = Label(root,text="This is a root window")
l.pack()
btn = Button(root,text="Click for an gift",command=topwin)
btn.pack()

root.mainloop()