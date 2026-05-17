print("Enter numbers to be swapped")
a = int(input("Enter first Value:"))
b = int(input("Enter second Value:"))
c = int(input("Enter third Value:"))
if a==b==c:
    print("Invalid input all values are same")
else:
    print(f"Original value:a={a},b={b},c={c}")
    print(f"Swapped value:a={c},b={a},c={b}")
a,b,c = c,a,b