import numpy as np
arr=np.array([10,20,30,40])
new_arr=np.insert(arr,2,25)  # insert 25 at index 2
print("Original array:", arr)
print("Original array:", new_arr)



# insert value in 2d array

import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
new_arr_2d=np.insert(arr_2d,1,[5,6,7],axis=1)  # insert 10 at row index 1
print("Original 2D array:\n", arr_2d)
print("Original 2D array:\n", new_arr_2d)