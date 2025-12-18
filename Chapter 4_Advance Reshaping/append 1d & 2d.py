import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new=np.append(arr,[[7,8,9]],axis=0)
print(new)   #2d array after appending row




import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new=np.append(arr,[[7],[8]],axis=1)
print(new)   #2d array after appending row



import numpy as np
arr=np.array([[1,2,3,4,5,6]])
new=np.append(arr,[[7,8,9]])
print(new)   #1d array after appending elements