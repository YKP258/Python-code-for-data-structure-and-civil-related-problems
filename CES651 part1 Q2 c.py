# c. Fixed beam: deflection as well as rotation at 0.25L and 0.60L from the left end.

l = float(input("Enter length of beam in m:"))
# x here is taken from left end of fixed beam
w = float(input("Enter value for udl in kN/m:"))
x = float(input("Enter position for deflection within length limit in m:"))

e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))


z = ((-(w*l*x*x*x)/12 + (w*l*l*x*x)/24 + (w*x*x*x*x)/24)/(e*i))
print("Deflection in fixed beam:",z)
#considering downward deflection as negative
if(z<=0):
    print("Downward Deflection")
else:
    print("upward deflection")


# r here is taken from left end of fixed beam
r = float(input("Enter slope position in m:"))
y = ((-(w*l*r*r)/4 + (w*l*l*r)/12 + (w*r*r*r)/6)/(e*i))
print("Rotaion in fixed beam at given position:",y)
if(y<=0):
    print("Anti-clock wise rotation")
else:
    print("clockwise rotation")
#considering clockwise roation as positive and vice-versa
