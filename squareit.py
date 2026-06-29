
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

odd_squares = []
even_squares = []

for num in range(start, end + 1):
    square = num ** 2

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Odd square numbers:", odd_squares)
print("Even square numbers:", even_squares)