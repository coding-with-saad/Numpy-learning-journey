"""
Docstring for Chapter 4_Advance Reshaping.insert
np.insert(array,index,value,asix=none)
array=original array
index=position where we want to insert value
value=value to be inserted
axis=0 for row and 1 for column
"""


import numpy as np
arr=np.array([[1,2,3,4,5,6]])
new=np.insert(arr, 5, 10)  
print(new)


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new=np.insert(arr, 2, [10,20,30],axis=0)  
print(new) 




import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
new=np.insert(arr, 3, [10,20,30] ,axis=1)  
print(new)




import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
new=np.insert(arr, 3, [10,20,30] ,axis=0)  
print(new)