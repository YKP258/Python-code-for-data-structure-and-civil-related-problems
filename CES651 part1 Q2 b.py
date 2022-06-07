# b. Cantilever beam: deflection as well as rotation at the center and at the ends.

l = float(input("Enter length of beam in m:"))
# x here is taken from free end of cantilever beam
w = float(input("Enter value for udl in kN/m:"))
x = float(input("Enter position for deflection from right end m:"))

e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))

a = (((w*l*l*l*x)/6 - (w*x*x*x*x)/24 - (w*l*l*l*l)/8)/(e*i))
print("\nDeflection in cantilever beam:",a)
#considering downward deflection as negative
if(a<=0):
    print("Downward Deflection")
else:
    print("upward deflection")


# r here is taken from free end of cantilever beam
r = float(input("\nEnter slope position from right end m:"))
b = ((-(w*r*r*r)/6 + (w*l*l*l)/6)/(e*i))
print("Rotaion in cantilver beam at given position:",b)

if(b<=0):
    print("Anti-clock wise rotation")
else:
    print("clockwise rotation")
#considering clockwise roation as positive and vice-versa