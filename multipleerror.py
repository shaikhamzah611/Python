try:
    num1,num2 = eval(input("Enter a  two number seperated by comma:"))
    result = num1/num2
    print("The Result is:",result)
except ZeroDivisionError:
    print("Division by zero is error!!!")
except SyntaxError:
    print("Comma is missing enter numbers separated by comma like this 1,2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("this will execute no matter what!")