string = input("Please Enter Your String:")

string2 = ("")

for i in string:
    string2 = i + string2 +i

print("\nOriginal String =",string)
print("\nReversed String = ",string2)