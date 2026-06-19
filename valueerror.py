
try:
    number = int(input("Enter a number:"))
    print("Number entered is:",number)
except ValueError as ex:
    print("Exeption:",ex)