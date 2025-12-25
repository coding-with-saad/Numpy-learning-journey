import numpy as np
# ar=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# p=np.arange(0,12,4)
ar=np.arange(1,13)
reshaped_a=ar.reshape((3,4))
print(reshaped_a)


import numpy as np
arr=np.array([[2, 4, 6],
            [1, 3, 5],
            [7, 9, 11]])

a=np.sum(arr,axis=0)
b=np.sum(arr,axis=1)
print(a)
print(b)




import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arr1[arr1%2==0])



import numpy as np
arr2=np.array([12, 45, 7, 32, 50, 18])
max_value=np.max(arr2)
max_index=np.argmax(arr2)
print(max_value)
print(max_index)



import numpy as np
arr2d1=np.array([[1, 2],
                [3, 4]])

arr2d2=np.array([[2, 0],
                [1, 2]])


multiply=arr2d1@arr2d2
print(multiply)