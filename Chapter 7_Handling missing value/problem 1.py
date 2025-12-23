"""
Docstring for Handling missing value.problem 1

# Handling Buildin Functions
np.isnan->detect missing value
np.nan->represents missing value
np.nanmean->compute mean ignoring nan values
np.nanstd->compute std ignoring nan values
np.nansum->compute sum ignoring nan values
np.nanmin->compute min ignoring nan values
np.nanmax->compute max ignoring nan values
"""

import numpy as np
arr=np.array([1,2,np.nan,4,5,np.nan])
print("Original array:", arr)
# Detect missing values
print("Missing values:", np.isnan(arr))
# Compute mean ignoring nan values
print("Mean ignoring nan:", np.nanmean(arr))
# Compute std ignoring nan values
print("Std ignoring nan:", np.nanstd(arr))
# Compute sum ignoring nan values
print("Sum ignoring nan:", np.nansum(arr))
# Compute min ignoring nan values
print("Min ignoring nan:", np.nanmin(arr))
# Compute max ignoring nan values
print("Max ignoring nan:", np.nanmax(arr))