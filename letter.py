import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Letter Writing App")

text = tk.Text(root, width=60, height=20)
text.grid(row=0, column=0, columnspan=3)

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        root.title(file)

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", tk.END))
        root.title(file)

tk.Button(root, text="Open", command=open_file).grid(row=1, column=0)
tk.Button(root, text="Save", command=save_file).grid(row=1, column=1)
tk.Button(root, text="Exit", command=root.destroy).grid(row=1, column=2)

root.mainloop()