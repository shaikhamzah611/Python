base = int(input("Enter the base:"))
n = int(input("Enter the power(n):"))
result = 1
for i in range(n):
    result = result*base
print(base,"to the power",n,"is:",result)