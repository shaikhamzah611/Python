class vehicle:
    def __init__(self,topspeed,model,mileage):
        self.topspeed=topspeed
        self.model=model
        self.mileage=mileage
class car(vehicle):
    def __init__(self, topspeed, model, mileage):
        super().__init__(topspeed, model, mileage)

carX = car(250,"BMW",20)
print("The car is: ",carX.model)
print("The topspeed of the car is: ",carX.topspeed)
print("The mileage of the car is: ",carX.mileage)

print("Is car the subclass of vehicle:", issubclass(car, vehicle))