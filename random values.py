import numpy as np
n=np.random.randint(10,size=(2,2))
print(n)

print("determinant")
print(np.linalg.det(n))

print("inverse")
print(np.linalg.inv(n))

print("matrix Rank")
print(np.linalg.matrix_rank(n))


-----------------

output

[[2 0]
 [5 8]]
determinant
15.999999999999998
inverse
[[ 0.5     0.    ]
 [-0.3125  0.125 ]]
matrix Rank
2
