
n = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, n) if i % 2 != 0]
even_numbers = [i for i in range(1, n) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("\nOriginal list:", fruits)
print("Updated list:", updated_fruits)