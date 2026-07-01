number1 = [1,2,3,4]
number2 = [3,4,5,6]

result = map(lambda x,y: x+y,number1,number2)
print("Addition of both: ")
print(list(result))

num = [6,8,4,0,2,1]
def sq(n):
    return n*n
square = list(map(sq,num))
print("The square of the numbers in list: ")
print(square)