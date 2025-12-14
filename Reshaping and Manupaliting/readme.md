### **Reshaping in NumPy**

Reshaping means changing the shape of an array without changing its data.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)
print(reshaped)
```

Output will be a 2×3 array.

---

### **Manipulating Arrays in NumPy**

Some common ways to manipulate arrays are:

#### **1. Changing Shape**

```python
print(arr.reshape(3, 2))
```

---

#### **2. Flattening an Array**

Flatten converts a multi-dimensional array into one dimension.

```python
flat = reshaped.flatten()
print(flat)
```

---

#### **3. Transpose**

Transpose swaps rows and columns.

```python
print(reshaped.T)
```

---

#### **4. Joining Arrays**

Arrays can be combined using `concatenate`.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

joined = np.concatenate((a, b))
print(joined)
```

---

#### **5. Splitting Arrays**

An array can also be split into smaller parts.

```python
split_arr = np.array_split(arr, 3)
print(split_arr)
```

---

These operations are commonly used to organize and manage data efficiently in NumPy.














### **Ravel and Flatten in NumPy**

Both `ravel()` and `flatten()` are used to convert a multi-dimensional array into a one-dimensional array.

---

### **flatten()**

`flatten()` returns a new array. Changes made to the flattened array do not affect the original array.

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])

flat_arr = arr.flatten()
flat_arr[0] = 99

print("Flattened array:", flat_arr)
print("Original array:", arr)
```

---

### **ravel()**

`ravel()` returns a view of the original array when possible. Changes made to the raveled array can affect the original array.

```python
ravel_arr = arr.ravel()
ravel_arr[0] = 88

print("Raveled array:", ravel_arr)
print("Original array:", arr)
```

---

### **Main Difference**

The main difference is that `flatten()` creates a copy of the data, while `ravel()` usually creates a view. Because of this, `ravel()` is faster and uses less memory, but changes may reflect in the original array.

---

This explanation is simple, clear, and good for understanding basic NumPy concepts.

