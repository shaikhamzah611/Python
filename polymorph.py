class BMW:
       def fuel_type(self):
        print("Petrol")
    
       def engine_type(self):
        print("BMW S14 Engine")
    
       def model(self):
        print("BMW M3 E30")

class Ferrari:
       def fuel_type(self):
        print("Petrol")
    
       def engine_type(self):
        print("V12 Engine")
    
       def model(self):
        print("Ferrari F40")

Bmw = BMW()
ferrari = Ferrari()
print("BMW: ")
Bmw.model()
Bmw.engine_type()
Bmw.fuel_type()

print("Ferrari: ")
ferrari.model()
ferrari.engine_type()
ferrari.fuel_type()