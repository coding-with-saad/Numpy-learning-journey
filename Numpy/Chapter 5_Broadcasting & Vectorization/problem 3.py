"""
Docstring for Chapter 5_Broadcasting & Vectorization.problem 3

broadcasting allows numpy to perform operations on arrays of different shapes.
For example, multiplying each element of an array by a scalar value.

Example of broadcasting using 1d array 2d array operations.
"""


import numpy as np
arr=np.array([100,150,200,250,300])
res=arr*2
print(res)




import numpy as np
arr=np.array([[100,150,200,250,300],
              [110,160,210,260,310]])  #matrix of shape (2,5)

vector=np.array([1,2,3,4,5])    #vector of shape (5,)

re=arr*vector
re1=arr+vector
re2=arr/vector
re3=arr-vector
print(re)   #matrix of shape (2,5)
print(re1)   #matrix of shape (2,5)
print(re2)   #matrix of shape (2,5)
print(re3)   #matrix of shape (2,5)



import numpy as np
arr=np.array([[100,150,200],
              [110,160,210]])  #matrix of shape (2,3)

vector=np.array([1,2])    #vector of shape (2,)

re=arr*vector
print(re)   #matrix of shape (2,3)