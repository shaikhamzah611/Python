class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print()

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print("Details of Dog 1:")
dog1.display()

print("Details of Dog 2:")
dog2.display()