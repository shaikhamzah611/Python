from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("90x90")

def handle_keypress(event):
    """Print the character associated with the key pressed."""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("I LIKE SPACE")

button = Button(text="Click")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()