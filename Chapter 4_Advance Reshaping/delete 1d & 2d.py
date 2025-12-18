"""
Docstring for Chapter 4_Advance Reshaping.delete 1d & 2d


delete() function is used to delete elements from an array.
np.delete(array, index, axis=None)
"""


import numpy as np
arr=np.array([1,2,3,4,5,6])
new_arr=np.delete(arr,2)
print(new_arr)



import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new_arr=np.delete(arr,1,axis=0)
print(new_arr)


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new_arr=np.delete(arr,1,axis=1)
print(new_arr)