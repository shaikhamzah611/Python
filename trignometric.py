import math

degrees = float(input("Enter the angle (in degrees): "))

radians = math.radians(degrees)

sine_result = math.sin(radians)
cosine_result = math.cos(radians)
tangent_result = math.tan(radians)

print("Sine:", sine_result)
print("Cosine:", cosine_result)
print("Tangent:", tangent_result)