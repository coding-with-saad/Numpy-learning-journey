"""
Docstring for Chapter 4_Advance Reshaping.splitting

np.split() function is used to split an array into multiple sub-arrays.
np.split(array, indices_or_sections, axis=0)

np.hsplit()
np.vsplit()
"""


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(np.split(arr,4))