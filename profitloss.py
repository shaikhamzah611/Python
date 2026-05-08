actual_cost = float(input("Enter the Actual Product Price:"))
sale_amount = float(input("Enter the Sale Amount:"))
if (sale_amount > actual_cost):
    amount = sale_amount-actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No Profit!!")