import math

def calculate_circumference(radius):
    circumference=2*math.pi*radius
    return circumference
radius_str = input("Enter the radius of circle:")
radius=float(radius_str)
result = calculate_circumference(radius)

print(f"The circumference of circle is ={result:.2f}".format(result))