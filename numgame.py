import random
playing = True
num = str(random.randint(0,11))

print("I am going to generate a number from 0 to 11,and you have to guess what it is")
print("The game ends when guess the number correctly")

while playing:
    guess = input("Enter your guess:")
    if num == guess:
        print("You won the game!!")
        print("The number was",num)
        break

    else:
        print("Your guess is not correct ,  Try again.\n")