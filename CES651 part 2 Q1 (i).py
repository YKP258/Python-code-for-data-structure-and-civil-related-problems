# moment area method (i) cantilever beam having udl
import matplotlib.pyplot as plt
import numpy as np

l = float(input("Enter length of beam in m:"))
w = float(input("Enter value for udl in kN/m:"))
e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))

x = np.linspace(0, l)
m = -(w/2)*(x ** 2)
plt.plot(x, m)
plt.fill_between(x, m)
plt.show()

#According to MAM theorem the change in slope between any two points on the elastic curve
# equals the area of the M/EI (moment) diagram between these two points.
A1 = ((1/3)*l*(w*l*l*0.5))
x = (A1)/(e*i)
print("slope at free end of given beam is:",x)

#According to MAM theorem The vertical deviation of a point A on an elastic curve with respect to the tangent which is
# extended from another point B equals the moment of the area under the M/EI diagram between those two points.
C1 = (3*l)/4
y = (A1*C1)/(e*i)
print("deflection at free end of given beam is:",y)

A2 = ((1/3)*l*(w*l*l*0.5))
A3 = ((1/3)*(l/2)*((w*l*l)/8))
z = (A2-A3)/(e*i)
print("slope at center of beam:",z)

C2 = (3*l)/4
C3 = (3*l)/8
C = l - (((A2*C2)+(A3*C3))/(A2+A3))
w = (z*C)/(e*i)
print("deflection at center of beam",w)