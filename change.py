try:
    amount = float(input("Enter the amount shopkeeper is asking:"))
    bill = float(input("Enter the amount you gave:"))

    if bill>amount:
       pay1 = bill-amount
       print("You need to give shopkeeper:",pay1)

    elif bill<amount:
       pay2=amount-bill
       print("You owe shopkeeper:",pay2)
    else:
       print("Input numbers properly!") 
except ValueError:
   print("Numbers only!!")