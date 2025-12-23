"""
Docstring for Handling missing value.problem 2
nan to number conversion
np.nan_to_num() function is used to replace nan with a specified value (default is 0)
"""

import numpy as np
arr=np.array([1,2,np.nan,4,5,np.nan])
print("Original array:", arr)
print("Replace nan with 15", np.nan_to_num(arr, nan=15))
# Replace nan with 0
print("Replace nan with 0", np.nan_to_num(arr))



"""
Docstring for Handling missing value.problem 3
infinite values handling
np.isinf() -> detect infinite values
np.isfinite() -> detect finite values
"""

import numpy as np
arr=np.array([1,2,np.inf,-np.inf,5])
print("Original array:", arr)
# Detect infinite values
print("Infinite values:", np.isinf(arr))
# Detect finite values
print("Finite values:", np.isfinite(arr))




# convert isinf or isfinate to number using nan_to_num

cleard_inf=np.nan_to_num(arr, posinf=1000, neginf=-1000)
print("Replace inf with large number:", cleard_inf)