import numpy as np
arr=np.array([5, 10, 15, 20, 25])
print(arr)
a=arr.shape
print(a)
print(type(arr))
# type(arr)
print(arr.dtype)



a=np.zeros((2,3))
print(a)
b=np.ones((3,2))
print(b)


arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr1[arr1>5]=0
print(arr1)



arr2=np.array([10, 20, 30, 40, 50])
print(arr2.std())
print(arr2.mean())


arr3=np.array([1, 2, 3])
arr4=np.array([4, 5, 6])
sabi=np.concatenate((arr3,arr4))
print(sabi)
saif=sabi.reshape((2,3))
print(saif)

