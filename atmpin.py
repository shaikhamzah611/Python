import tkinter as tk

root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("400x450")

f1 = tk.Frame(root, bd=3, relief="raised")
f1.place(x=30, y=30, width=340, height=120)

tk.Label(f1, text="Account Details").grid(row=0, column=0, columnspan=2)

tk.Label(f1, text="Name:").grid(row=1, column=0)
name = tk.Entry(f1)
name.grid(row=1, column=1)

tk.Label(f1, text="PIN:").grid(row=2, column=0)
pin = tk.Entry(f1, show="*")
pin.grid(row=2, column=1)

# Keypad
f2 = tk.Frame(root, bd=3, relief="sunken")
f2.place(x=80, y=170, width=240, height=180)

def add(x):
    pin.insert(tk.END, x)

for i in range(1, 10):
    tk.Button(f2, text=i, width=5,
              command=lambda x=i: add(x)).grid(
              row=(i-1)//3, column=(i-1)%3)

tk.Button(f2, text="0", width=5,
          command=lambda: add(0)).grid(row=3, column=1)

def show():
    text.delete("1.0", tk.END)
    text.insert(tk.END, "Name: " + name.get() +
               "\nPIN: " + pin.get())

tk.Button(root, text="Show Details", command=show).place(x=145, y=365)

text = tk.Text(root, width=35, height=4)
text.place(x=30, y=400)

root.mainloop()