from sympy import *
from numpy import *

length_of_beam = float(input("Enter Length of the Beam (m) : "))
point_load = float(input("Enter The Point Load (kN) : "))
udl_value = float(input("Enter UDL intensity (kN/m) : "))
EI = 5000  # in kNm2
K = zeros([6, 6])
length_of_element = length_of_beam / 2
local_stiffness_matrix = array([[12, 6 * length_of_element, -12, 6 * length_of_element],
            [6 * length_of_element, 4 * length_of_element * 2, -6 * length_of_element, 2 * length_of_element * 2],
            [-12, -6 * length_of_element, 12, -6 * length_of_element],
            [6 * length_of_element, 2 * length_of_element ** 2, -6 * length_of_element,
            4 * length_of_element * 2]]) * EI / length_of_element * 3

for i in range(0, 4, 2):
    ind = array([[i, i + 1, i + 2, i + 3]])   # Notice the 2D array
    rows = broadcast_to(ind.transpose(), (4, 4))
    cols = broadcast_to(ind, (4, 4))
    K[rows, cols] += local_stiffness_matrix
K = Matrix(K)

F1, F2, u2, u3, u4, u6 = symbols('F1 F2 u2 u3 u4 u6')

U = Matrix([0, u2, u3, u4, 0, u6])
F = Matrix([F1 - udl_value * length_of_beam / 4, - udl_value * length_of_beam ** 2 / 48,
            - udl_value * length_of_beam / 2 - point_load, 0, F2 - udl_value * length_of_beam / 4,
            udl_value * length_of_beam ** 2 / 48])

solution = solve((K*U - F), (F1, F2, u2, u3, u4, u6))

print("\nReaction at Left End : ", round(solution[F1], 2), " kN")
print("Rotation at Left End : ", round(deg(solution[u2]), 2), u'\N{DEGREE SIGN}')
print("\nDeflection at Centre of Beam : ", round(solution[u3], 5) * 1000, " mm")
print("Rotation at Centre of Beam : ", round(deg(solution[u4]), 2), u'\N{DEGREE SIGN}')
print("\nReaction at Right End : ", round(solution[F2], 2), " kN")
print("Rotation at Right End : ", round(deg(solution[u6]), 2), u'\N{DEGREE SIGN}')