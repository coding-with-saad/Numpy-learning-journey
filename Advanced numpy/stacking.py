import numpy as np
arr=np.array([1,2,3])
arr=np.array([4,5,6])
print(np.vstack((arr,arr)))  # vertical stack
print(np.hstack((arr,arr)))  # horizontal stack
print(np.stack((arr,arr),axis=0))  # stack along rows
print(np.stack((arr,arr),axis=1))  # stack along columns





"""
different between vstack , hstack and stack is that vstack and hstack are used to combine arrays along vertical and horizontal axes respectively, while stack allows you to specify the axis along which to stack the arrays, providing more flexibility in how the arrays are combined.

"""
