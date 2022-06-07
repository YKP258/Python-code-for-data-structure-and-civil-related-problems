import math

x = int(input("enter raduis of 1st sphere:"))
y = int(input("enter radius of 2nd sphere:"))
print("volume of 1st sphere is:",4/3*math.pi*x**3)
print("volume of 2nd sphere is:",4/3*math.pi*y**3)

v = 4/3*math.pi*(x**3-y**3)

print("difference between voulume of above two spheres is:", v)