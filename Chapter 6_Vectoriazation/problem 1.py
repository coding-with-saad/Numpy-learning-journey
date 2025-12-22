"""
Docstring for Chapter 6_Vectoriazation.problem 1
Vectorization is the process of converting iterative operations into array operations to improve performance.
This example demonstrates vectorized operations using NumPy to perform element-wise addition, subtraction, multiplication, and division on arrays.
"""



arr1=[1,2,3,4,5]
arr2=[6,7,8,9,10]
# Element-wise addition
add=[x+y for x,y in zip(arr1,arr2)]
print("Addition:", add)
# Element-wise subtraction
sub=[x-y for x,y in zip(arr1,arr2)]
print("Subtraction:", sub)
# Element-wise multiplication
mul=[x*y for x,y in zip(arr1,arr2)]
print("Multiplication:", mul)
# Element-wise division
div=[x/y for x,y in zip(arr1,arr2)]
print("Division:", div)



import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
# Element-wise addition
add=arr1+arr2
print("Addition:", add)