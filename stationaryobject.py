import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Stationery Order Management App")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

try:
    bg_image = tk.PhotoImage(file="background.png")
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
except:
    canvas.configure(bg="lightblue")

frame = ttk.Frame(canvas, padding=20)
canvas.create_window(400, 300, window=frame)

title = ttk.Label(
    frame,
    text="Stationery Order Management",
    font=("Arial", 22, "bold")
)
title.grid(row=0, column=0, columnspan=4, pady=15)

ttk.Label(frame, text="Currency:").grid(row=1, column=0, padx=5, pady=5)

currency = ttk.Combobox(
    frame,
    values=["USD", "INR"],
    state="readonly",
    width=10
)
currency.current(0)
currency.grid(row=1, column=1, padx=5, pady=5)

items = [
    ("Pen", 1.50),
    ("Pencil", 0.50),
    ("Notebook", 3.00),
    ("Eraser", 0.75),
    ("Marker", 2.00)
]

quantities = []

ttk.Label(frame, text="No.", font=("Arial", 11, "bold")).grid(
    row=3, column=0, padx=10, pady=5
)

ttk.Label(frame, text="Item", font=("Arial", 11, "bold")).grid(
    row=3, column=1, padx=10, pady=5
)

ttk.Label(frame, text="Price", font=("Arial", 11, "bold")).grid(
    row=3, column=2, padx=10, pady=5
)

ttk.Label(frame, text="Quantity", font=("Arial", 11, "bold")).grid(
    row=3, column=3, padx=10, pady=5
)

for number, (item, price) in enumerate(items, start=1):

    ttk.Label(frame, text=str(number)).grid(
        row=number + 3, column=0, padx=10, pady=5
    )

    ttk.Label(frame, text=item).grid(
        row=number + 3, column=1, padx=10, pady=5
    )

    price_label = ttk.Label(frame, text=f"${price:.2f}")
    price_label.grid(
        row=number + 3, column=2, padx=10, pady=5
    )

    quantity = ttk.Entry(frame, width=10)
    quantity.grid(
        row=number + 3, column=3, padx=10, pady=5
    )

    quantities.append(quantity)

def update_currency(event=None):

    selected_currency = currency.get()

    for number, (item, price) in enumerate(items):

        # Ternary operator
        converted_price = price if selected_currency == "USD" else price * 83

        symbol = "$" if selected_currency == "USD" else "₹"

        price_label = frame.grid_slaves(
            row=number + 4,
            column=2
        )[0]

        price_label.config(
            text=f"{symbol}{converted_price:.2f}"
        )


currency.bind("<<ComboboxSelected>>", update_currency)

def place_order():

    total = 0

    for number, quantity_box in enumerate(quantities):

        quantity = quantity_box.get()

        
        if not quantity.isdigit():
            messagebox.showerror(
                "Invalid Quantity",
                "Please enter numbers only."
            )
            return

        quantity = int(quantity)

        price = items[number][1]

        if currency.get() == "USD":
            total += price * quantity
        else:
            total += price * 83 * quantity

    symbol = "$" if currency.get() == "USD" else "₹"

    messagebox.showinfo(
        "Order Complete",
        f"Your order has been placed!\n\n"
        f"Total: {symbol}{total:.2f}"
    )

order_button = ttk.Button(
    frame,
    text="Place Order",
    command=place_order
)

order_button.grid(
    row=10,
    column=0,
    columnspan=4,
    pady=20
)

root.mainloop()