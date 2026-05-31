number = int(input("Enter a number: "))

count = 0
n = number

while n != 0:
    n = n // 10
    count += 1

print("Number of digits:", count)