import numpy as np

A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))
print(B.shape)

A2 = np.array([[1, 2], [3, 4]])
B2 = np.array([[5, 6], [7, 8]])
C2 = np.dot(A2, B2)
print(C2)
print(np.ndim(C2))
print(C2.shape)


A3 = np.array([[1, 2, 4], [4, 5, 6]])
B3 = np.array([[1, 2], [3, 4], [5, 6]])
C3 = np.dot(A3, B3)
print(C3)
print(np.ndim(C3))
print(C3.shape)

# error test
D3 = np.array([[1, 2], [3, 4]])
#np.dot(A3, D3)

X = np.array([1, 2])
print(X.shape)
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W)
print(W.shape)
Y = np.dot(X, W)
print(Y)