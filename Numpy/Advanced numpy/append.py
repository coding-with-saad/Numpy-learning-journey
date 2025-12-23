import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)
new_arr=np.append(arr,[70,80,90])  # append value at the end of array
print(new_arr)


"""
np.concatenate() can also be used to append values to an array. However, there are some differences between np.append() and np.concatenate():
1. Functionality:
   - np.append(): Specifically designed to append values to the end of an array. It can also append along a specified axis for multi-dimensional arrays.
   - np.concatenate(): A more general function that concatenates two or more arrays along a specified axis. It requires all input arrays to have the same shape, except in the dimension corresponding to the axis along which they are concatenated.
2. Input Requirements:
   - np.append(): Takes a single array and the values to be appended. The values can be a single value or an array-like structure.
   - np.concatenate(): Takes a sequence (like a list or tuple) of arrays to be concatenated. All arrays must have compatible shapes.
3. Axis Handling:
    - np.append(): By default, it flattens the input array before appending. You can specify an axis for multi-dimensional arrays.
    - np.concatenate(): Requires you to explicitly specify the axis along which to concatenate the arrays. It does not flatten the arrays.

In summary, use np.append() when you want to add values to the end of an array, and use np.concatenate() when you want to combine multiple arrays along a specific axis.
"""

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new=np.concatenate((arr1,arr2))
print(new)