import numpy as np
ar1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(ar1)
print("display all elements excluding first row:")
print(ar1[1:,:])
print("display all elements excluding last column:")
print(ar1[:,:3])
print("display all elements 1st and 2nd column in 2nd and 3rd row:")
print(ar1[1:3,0:2])
print("display all elements 2st and 3rd column ")
print(ar1[:,1:3])
print("display elements 2nd and 3rd element of 1 row:")
print(ar1[:1,1:3])


--------------
out put

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
display all elements excluding first row:
[[ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
display all elements excluding last column:
[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]
 [13 14 15]]
display all elements 1st and 2nd column in 2nd and 3rd row:
[[ 5  6]
 [ 9 10]]
display all elements 2st and 3rd column 
[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]
display elements 2nd and 3rd element of 1 row:
[[2 3]]
