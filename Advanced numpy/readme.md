## Inserting Elements in NumPy Arrays

This document explains different ways to insert numbers or matrices into arrays using NumPy. It also includes a comparison between NumPy array insertion and Python list insertion.

---

### **1. Using `np.insert()`**

This method inserts values at a specific index.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
new_arr = np.insert(arr, 2, 25)
print(new_arr)
```

You can also insert multiple values:

```python
new_arr = np.insert(arr, 1, [15, 18])
print(new_arr)
```

---

### **2. Inserting Rows or Columns in 2D Arrays**

**Insert a row:**

```python
matrix = np.array([[1, 2], [3, 4]])
new_matrix = np.insert(matrix, 1, [5, 6], axis=0)
print(new_matrix)
```

**Insert a column:**

```python
new_matrix = np.insert(matrix, 1, [9, 9], axis=1)
print(new_matrix)
```

---

### **3. Using `np.append()`**

This method adds values at the end of the array.

```python
arr = np.array([1, 2, 3])
new_arr = np.append(arr, 4)
print(new_arr)
```

---

### **4. Using `np.concatenate()`**

This method joins two arrays together.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5])
result = np.concatenate((a, b))
print(result)
```

---

### **5. Using Python List then Converting to NumPy**

```python
lst = [1, 2, 3]
lst.insert(1, 99)
arr = np.array(lst)
print(arr)
```

---

## Comparison: NumPy Insertion vs Python List Insertion

**NumPy Array Insertion**

* NumPy arrays have fixed size.
* Inserting elements creates a new array every time.
* Slower for frequent insertions.
* Best for numerical operations and large datasets.

**Python List Insertion**

* Python lists are dynamic in size.
* Insertion happens directly in the same list.
* Faster and easier for frequent insertions.
* Better choice when data size changes often.

---

### **Conclusion**

Use NumPy insertion methods when working with numerical data and arrays. Use Python lists when you need frequent insertions and flexibility.
