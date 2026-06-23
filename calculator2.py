try:
    def add(A,B):
        return (A+B)
    def sub(A,B):
        return (A-B)
    def div(A,B):
        return (A/B)
    def mult(A,B):
        return (A*B)

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Chose anyone of the following ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = input("Enter choice a/b/c/d :")

    if choice=="a":
        print(num1,"+",num2,"is equal to=",add(num1,num2))
    elif choice=="b":
        print(num1,"-",num2,"is equal to=",sub(num1,num2))
    elif choice=="c":
        print(num1,"*",num2,"is equal to=",mult(num1,num2))
    elif choice=="d":
        print(num1,"/",num2,"is equal to=",div(num1,num2))
    else:
        pass
except ValueError:
    print("Invalid input!!")
except ZeroDivisionError:
    print("Do not input second number as zero!!")
except SyntaxError:
    print("Invalid!!")