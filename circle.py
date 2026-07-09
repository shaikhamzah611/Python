class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def peri(self):
        return 3.14*2*self.radius
    
r = float(input("Enter the radius: "))
c = circle(r)

print("Area of circle is: ",c.area())
print("Perimeter is: ",c.peri())