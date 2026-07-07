class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

Bluey = parrot("Bluey",13)
Rocket = parrot("Rocket",14)

print("Bluey is a {}".format(Bluey.species))
print("Rocket is a {}".format(Rocket.species))

print("{} is {} years old".format(Bluey.name,Bluey.age))
print("{} is {} years old".format(Rocket.name,Rocket.age))