import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr.reshape(2,5))  # 2 row and 5 column
print(arr.reshape(5,2))  # 5 row and 2 column

# reshape doesnot create a new array it just change the shape of existing array
# so if we change any value in reshaped array it will reflect in original array


