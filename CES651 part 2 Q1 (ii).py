# moment area method (ii) cantilever beam having moment at center
import matplotlib.pyplot as plt
import numpy as np

l = float(input("Enter length of beam in m:"))
m = float(input("Enter value of moment in kN-m:"))
e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))

x = np.linspace(0, l)
a = -(m) * x ** 0
plt.plot(x, a)
plt.fill_between(x/2, a)
plt.show()

#According to MAM theorem the change in slope between any two points on the elastic curve
# equals the area of the M/EI (moment) diagram between these two points.
A1 = ((m/2)*l)
x = (A1)/(e*i)
print("slope at free end of given beam is:",x)

#According to MAM theorem The vertical deviation of a point A on an elastic curve with respect to the tangent which is
# extended from another point B equals the moment of the area under the M/EI diagram between those two points.
C1 = (3*l)/4
y = (A1*C1)/(e*i)
print("deflection at free end of given beam is:",y)

A2 = (m/2)*l
z = (A2)/(e*i)
print("slope at center of beam:",z)

C2 = (l)/4
w = (z*C2)/(e*i)
print("deflection at center of beam",w)