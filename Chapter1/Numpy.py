import numpy as np

# numpy array
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

y = np.array([2.0, 4.0, 6.0])

# numpy element-wise something. plus, minus, product
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# numpy N dimension array
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
print(A+B)
print(A*B)

# numpy broadcast
print(2.0 * x)

C = np.array([[1, 2], [3, 4]])
D = np.array([10, 20])
print(C * D)

# index
E = C * D
print(E[1][1])

X = E.flatten()
print(X)

print(X[np.array([0, 2])])