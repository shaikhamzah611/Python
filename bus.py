class vehicle:
    def __init__(self,name,topspeed,mileage):
        self.name = name
        self.topspeed = topspeed
        self.mileage = mileage
class bus(vehicle):
    pass
SchoolBus = bus("Bharat Benz",200,15)
print("\nVehicle name: ",SchoolBus.name,"Maximum Speed:",SchoolBus.topspeed,"Mileage:",SchoolBus.mileage,"\n")