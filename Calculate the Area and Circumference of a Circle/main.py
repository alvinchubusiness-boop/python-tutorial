import math 


radius = float(input("Enter the radius of the circle (cm): "))


circumference = 2 * math.pi * radius


area = math.pi * (radius ** 2)


print("The circumference is:", round(circumference, 2), "cm")
print("The area is:", round(area, 2), "cm²")