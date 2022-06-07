# moment area method (iv) cantilever beam having point load at free end and having different i values.
import matplotlib.pyplot as plt
import numpy as np

l = float(input("Enter length of beam in m:"))
p = float(input("Enter value of point load in kN:"))
e = float(input("Enter elastic modulus value in kN/mm^2:"))
i = float(input("Enter moment of inertia value in mm^4:"))

x = np.linspace(0, l)
y = np.linspace(l/2, l)
a = -(p) * x
b = -(p) * y * 0.5
plt.plot(x, a)
plt.fill_between(x/2, a/2)
plt.fill_between(y, b)
plt.show()

#According to MAM theorem the change in slope between any two points on the elastic curve
# equals the area of the M/EI (moment) diagram between these two points.
x = (5*p*(l ** 2))/(16*e*i)
print("slope at free end of given beam is:",x)
print("anticlockwise")

#According to MAM theorem The vertical deviation of a point A on an elastic curve with respect to the tangent which is
# extended from another point B equals the moment of the area under the M/EI diagram between those two points.
y = (3*p*(l ** 3))/(16*e*i)
print("deflection at free end of given beam is:",y)
print ("Downward")