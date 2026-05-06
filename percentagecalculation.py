print("Enter marks obtained in 4 subjects:")
math = int(input("math:"))
science = int(input("science:"))
english = int(input("english:"))
hindi = int(input("hindi:"))

sum = math+science+english+hindi
print("Sum of math,science,english,hindi=",sum)

perc = (sum/400)*100

print(end="Percentage Mark =",)
print(perc)