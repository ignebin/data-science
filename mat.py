import numpy as np


A = np.array([[1, 2], [3, 4]])


U, s, Vt = np.linalg.svd(A)

import numpy as np

# Create a zero matrix of size 3x3
zero_matrix = np.zeros((2, 2))

Sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(Sigma, s)


A_reconstructed = np.dot(U, np.dot(Sigma, Vt))

print("Original matrix:")
print(A)
print("\nLeft singular vectors (U):")
print(U)
print("\nSingular values (s):")
print(s)
print("Zero Matrix:")
print(zero_matrix)
print("\nDiagonal matrix (Sigma):")
print(Sigma)
print("\nRight singular vectors (Vt):")
print(Vt)
print("\nReconstructed matrix from SVD:")
print(A_reconstructed)



-------------
output

Original matrix:
[[1 2]
 [3 4]]

Left singular vectors (U):
[[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]]

Singular values (s):
[5.4649857  0.36596619]
Zero Matrix:
[[0. 0.]
 [0. 0.]]

Diagonal matrix (Sigma):
[[5.4649857  0.        ]
 [0.         0.36596619]]

Right singular vectors (Vt):
[[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]

Reconstructed matrix from SVD:
[[1. 2.]
 [3. 4.]]

