# a. Simply supported beam having udl and find deflection at center and rotations at the ends.

l = float(input("Enter length of beam in m:"))
# x here is taken from left end of simply supported beam
w = float(input("Enter value for udl in kN/m:"))
x = float(input("Enter position for deflection within length limit in m:"))

e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))

z = (((w*l*x*x*x)/12 - (w*x*x*x*x)/24 - (w*l*l*l*x)/24)/(e*i))

print("\nDeflection in simply supported beam:",z)
if(z<=0):
    print("Downward Deflection")
else:
    print("upward deflection")
#considering downward deflection as negative

# r here is taken from left end of simply supported beam
r = float(input("\nEnter slope position in m:"))
y = (((w*l*r*r)/4 - (w*r*r*r)/6 - (w*l*l*l)/24)/(e*i))
print("Rotaion in simply supported beam at given position:",y)
if(y<=0):
    print("Anti-clock wise rotation")
else:
    print("clockwise rotation")
#considering clockwise roation as positive and vice-versa