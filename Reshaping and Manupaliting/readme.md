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
