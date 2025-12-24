"""
np.concatenate() function is used to join two or more arrays of the same shape along a specified axis.
np.concatenate((array1, array2, ...), axis=0)

axis=0: Join along columns (vertical stacking)
axis=1: Join along rows (horizontal stacking)
"""


import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11,12]])
new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)



import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11,12]])
new_arr = np.concatenate((arr1, arr2), axis=1)
print(new_arr)