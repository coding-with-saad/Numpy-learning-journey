import numpy as np
arr=np.array([1,2,3])
print(arr)
new_arr=np.delete(arr,1)  # delete value at index 1
print("Original array:", new_arr)


import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
new_arr_2d=np.delete(arr_2d,1,axis=1)
print(new_arr_2d)

"""
axis means whether we want to delete row or column
axis=0  --> row
axis=1  --> column

"""