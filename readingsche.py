import tkinter as tk

root = tk.Tk()
root.title("Reading Schedule")
root.geometry("300x200")

def planner():
    win = tk.Toplevel(root)
    win.title("Reading Planner")
    win.geometry("300x220")

    tk.Label(win, text="Total Pages").pack()
    pages = tk.Entry(win)
    pages.pack()

    tk.Label(win, text="Pages Per Day").pack()
    daily = tk.Entry(win)
    daily.pack()

    result = tk.Label(win, text="")
    result.pack()

    def calculate():
        try:
            p = int(pages.get())
            d = int(daily.get())

            days = p // d
            left = p % d

            result.config(text=f"Days: {days}\nPages left: {left}")
        except:
            result.config(text="Enter whole numbers!")

    tk.Button(win, text="Calculate",
              command=calculate).pack()

tk.Button(root, text="Open Planner",
          command=planner).pack(pady=70)

root.mainloop()