import numpy as np
ar1=np.array([[1,2],[5,6]])
ar2=np.array([[2,1],[6,5]])
print(ar1)
print(ar2)
print("Matrix Addition")
print(np.add(ar1,ar2))

print("Matrix Subtraction")
print(np.subtract(ar1,ar2))

print("Matrix multiplication")
print(np.multiply(ar1,ar2))

print("Matrix Division")
print(np.divide(ar1,ar2))

print("Matrix Multiplication")
print(np.dot(ar1,ar2))

print("Matrix Transpose")
print(ar1.transpose())

print("Sum of diagonal Matrix ")
print(np.trace(ar1))


---------------------

output

[[1 2]
 [5 6]]
[[2 1]
 [6 5]]
Matrix Addition
[[ 3  3]
 [11 11]]
Matrix Subtraction
[[-1  1]
 [-1  1]]
Matrix multiplication
[[ 2  2]
 [30 30]]
Matrix Division
[[0.5        2.        ]
 [0.83333333 1.2       ]]
Matrix Multiplication
[[14 11]
 [46 35]]
Matrix Transpose
[[1 5]
 [2 6]]
Sum of diagonal Matrix 
7

