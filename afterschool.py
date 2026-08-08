import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Routine Checker")
root.geometry("350x250")

task = tk.Entry(root)
task.pack(pady=20)

result = tk.Label(root, text="Type a task")
result.pack()

def key(event):
    result.config(text="Last character: " + event.char)

def click(event):
    result.config(text="You clicked the routine area")

def check():
    if task.get() == "":
        messagebox.showwarning("Warning", "Enter a task!")
    else:
        result.config(text="Next task: " + task.get())

task.bind("<Key>", key)

area = tk.Label(root, text="Click Routine Area", width=25, height=3)
area.pack()
area.bind("<Button-1>", click)

tk.Button(root, text="Check Routine", command=check).pack(pady=15)

root.mainloop()