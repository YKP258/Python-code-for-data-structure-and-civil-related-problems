import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries for matrix 1 in a single line (separated by space): ")
X = list(map(int, input().split()))
A = np.array(X).reshape(R, C)
print(A)
print("Enter the entries for matrix 2 in a single line (separated by space): ")
Y = list(map(int, input().split()))
B = np.array(Y).reshape(R, C)
print(B)

a = np.trace(A)
print("\n(a) TRACE of matrix A is :",a)

b = np.product(A)
print("\n(b) Product of the elements of [A] is :",b)

c = np.matrix.diagonal(B)
d = np.product(c)
print("\n\n(c) The Product of the diagonal elements of [B] is :",d)

e = np.transpose(B)
print("\n(d) Transpose of matrix B is :\n ",e)

f = np.add(A, B)
print("(e) Addition of matrix A+B is :\n ",f)

g = np.subtract(A, B)
print("\n(f) Subtraction of matrix is A-B :\n ",g)

h = np.dot(A, B)
print("\n(g) Multiplication of matrix A*B is :\n ",h)

i = np.dot(B, A)
print("\n(h) Multiplication of matrix B*A is :\n ",i)

n = int(input("Enter a number n :"))
x = np.multiply(n, B)
y = np.dot(B, x)
print("\n(i) Multiplication of matrix n[B] is :\n  ",x)
print("\n(i) Multiplication of matrix [B]*n[B] is :\n ",y)

j = np.transpose(A)
k = np.dot(B, j)
print("\n(j) The multiplication of matrix B*AT is :\n ",k)

l = np.linalg.matrix_rank(B)
print("\n(k) Rank of matrix [B] is :",l)

m, v = np.linalg.eig(A)
print("\n(l) Eig of matrix [A]:", m,end="")

n = np.linalg.inv(B)
print("\n\n(m) Inv of matrix [B] is :\n ",n)














