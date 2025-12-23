"""
Docstring for Chapter 4_Advance Reshaping.stacking

stack() function is used to stack arrays in sequence vertically (row wise) or horizontally (column wise).
np.stack(arrays, axis=0)
vstack() function is used to stack arrays in sequence vertically (row wise).
np.vtack(arr,arra)
hstack() function is used to stack arrays in sequence horizontally (column wise).
np.hstack(arr,arra)
"""

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new=np.vstack((arr1,arr2))
print(new)


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new=np.hstack((arr1,arr2))
print(new)