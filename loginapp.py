from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("300x300")

frame = Frame(master=root, height = 150,width=250,bg="lightblue")

lbl1 = Label(master=frame, text="Username",bg="yellow",fg="black",width=13)
lbl2 = Label(master=frame, text="Password",bg="green",fg="white",width=13)  
lbl3 = Label(master=frame, text="Nick name",bg="red",fg="white",width=13)

name_entry = Entry(frame)
username_entry = Entry(frame)
password_entry = Entry(frame,show="*")

def display():
    name = name_entry.get()
    greet = "HELLO "+name
    message = "\nCongratulations! You have successfully created an account."
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox = Text(bg="#BEBEBE",fg="black")

btn = Button( text="Submit",command=display,bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=120,y=20)
lbl2.place(x=20,y=60)
username_entry.place(x=120,y=100)
lbl3.place(x=20,y=100)
password_entry.place(x=120,y=60)
btn.place(x=120,y=140)
textbox.place(x=20,y=180)
root.mainloop()