from sympy import *
from numpy import *

distance_1 = float(input("Enter Length of the Left Overhang (m) : "))
distance_2 = float(input("Enter Distance between the Supports (m) : "))
distance_3 = float(input("Enter Length of the Right Overhang (m) : "))
left_point_load = float(input("Enter The Point Load at Left End (kN) : "))
right_point_load = float(input("Enter The Point Load at Right End (kN) : "))

EI = 5000  # in kNm2
K = zeros([8, 8])
length_of_element = [distance_1, distance_2, distance_3]
d = 0

for i in range(0, 6, 2):
    local_stiffness_matrix = array([[12, 6 * length_of_element[d], -12, 6 * length_of_element[d]],
                                    [6 * length_of_element[d], 4 * length_of_element[d] ** 2,
                                     -6 * length_of_element[d], 2 * length_of_element[d] ** 2],
                                    [-12, -6 * length_of_element[d], 12, -6 * length_of_element[d]],
                                    [6 * length_of_element[d], 2 * length_of_element[d] ** 2,
                                     -6 * length_of_element[d],
                                     4 * length_of_element[d] * 2]]) * EI / length_of_element[d] * 3
    ind = array([[i, i + 1, i + 2, i + 3]])   # Notice the 2D array
    rows = broadcast_to(ind.transpose(), (4, 4))
    cols = broadcast_to(ind, (4, 4))
    K[rows, cols] += local_stiffness_matrix
    d += 1
K = Matrix(K)

F3, F5, u1, u2, u4, u6, u7, u8 = symbols('F3 F5 u1 u2 u4 u6 u7 u8')
U = Matrix([u1, u2, 0, u4, 0, u6, u7, u8])
F = Matrix([-left_point_load, 0, F3, 0, F5, 0, -right_point_load, 0])

solution = solve((K*U - F), (F3, F5, u1, u2, u4, u6, u7, u8))

x = distance_2 / 2
length_of_beam = distance_2
v = (x - 2 * x * 2 / length_of_beam + x * 3 / length_of_beam ** 2) * solution[u4] + \
    (-x * 2 / length_of_beam + x * 3 / length_of_beam ** 2) * solution[u6]
c = (1 - 4 * x / length_of_beam + 3 * x * 2 / length_of_beam * 2) * solution[u4] + \
    (-x * 2 / length_of_beam + 3 * x * 2 / length_of_beam * 2) * solution[u6]

print("\nDeflection at Left End : ", round(solution[u1], 5) * 1000, " mm")
print("Rotation at Left End : ", round(deg(solution[u2]), 2), u'\N{DEGREE SIGN}')
print("\nReaction at Left Support : ", round(solution[F3], 2), " kN")
print("Moment at Left Support : ", round(-left_point_load * distance_1, 2), " kNm")
print("Rotation at Left Support : ", round(deg(solution[u4]), 2), u'\N{DEGREE SIGN}')
print("\nDeflection at Centre of Beam : ", round(v, 5) * 1000, " mm")
print("Rotation at Centre of Beam : ", round(deg(c), 2), u'\N{DEGREE SIGN}')
print("\nReaction at Right Support : ", round(solution[F5], 2), " kN")
print("Moment at Right Support : ", round(-right_point_load * distance_3, 2), " kNm")
print("Rotation at Right Support : ", round(deg(solution[u6]), 2), u'\N{DEGREE SIGN}')
print("\nDeflection at Right End : ", round(solution[u7], 5) * 1000, " mm")
print("Rotation at Right End : ", round(deg(solution[u8]), 2), u'\N{DEGREE SIGN}')