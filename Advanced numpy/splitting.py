"""
Docstring for Advanced numpy.splitting
"""


import numpy as np
arr=np.array([1,2,3,4])
print(np.split(arr,4))



import numpy as np
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(np.stack(arr_2d))  # default axis=0
print(np.stack(arr_2d,axis=1))  # axis=1
print(np.array_split(arr_2d,2,axis=1))  # split column wise
print(np.array_split(arr_2d,2,axis=0))  # split row wise


"""
split function is used to split the array into multiple sub-arrays.
stack function is used to stack the arrays along a new axis.


"""


import numpy as np
arr=np.array([1,2,3,4])
print(np.hsplit(arr,2))  # horizontal split


import numpy as np
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])  
print(np.vsplit(arr_2d,2))  # vertical split