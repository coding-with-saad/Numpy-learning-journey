import numpy as np
arr=np.arange(1,10,2)
print(arr)

# it was use ful for large amount of data when we are multiplay our data check data or add data
import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
print(arr_1d+5)
print(arr_1d*2)
print(arr_1d**2)



# In NumPy, an aggregation function is used to combine many values into a single value. These functions are mostly used to summarize data, like finding the total, average, or maximum value of an array.

# Some common aggregation functions in NumPy are:

# * `np.sum()` calculates the total of all elements.
# * `np.mean()` finds the average value.
# * `np.max()` and `np.min()` give the largest and smallest values.
# * `np.std()` calculates the standard deviation.
# * `np.var()` calculates the variance.
# * `np.prod()` multiplies all elements together.

# These functions can be applied to the whole array or along a specific axis (row-wise or column-wise). Aggregation functions are very useful in data analysis because they help reduce large datasets into simple, meaningful values.


import numpy as np

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Apply aggregation functions
total = np.sum(data)
average = np.mean(data)
maximum = np.max(data)
minimum = np.min(data)
standard_deviation = np.std(data)
variance = np.var(data)
product = np.prod(data)

# Print results
print("Array:", data)
print("Sum:", total)
print("Mean:", average)
print("Max:", maximum)
print("Min:", minimum)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)
print("Product:", product)


