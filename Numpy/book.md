# 📘 NumPy for Beginners: A Practical Guide

Welcome to this beginner-friendly guide to **NumPy**, the core library for numerical computing in Python.
Think of this README like a small book you can read, practice, and grow with.

---

## 📌 What is NumPy?

NumPy stands for **Numerical Python**. It helps you work with numbers, arrays, and matrices fast and easily.

You will use NumPy when you work with:

* Data Science
* Machine Learning
* Scientific computing
* Image processing

---

## ⚙️ Installation

Make sure Python is installed, then run:

```bash
pip install numpy
```

Check installation:

```python
import numpy as np
print(np.__version__)
```

---

## 🚀 Getting Started

```python
import numpy as np
```

We usually use `np` as short name for NumPy.

---

## 🧱 NumPy Arrays

Arrays are the heart of NumPy.

```python
arr = np.array([1, 2, 3, 4])
print(arr)
```

Arrays are faster and more powerful than Python lists.

---

## 📐 Array Properties

```python
print(arr.shape)   # shape of array
print(arr.ndim)    # number of dimensions
print(arr.size)    # total elements
print(arr.dtype)  # data type
```

---

## 🔢 Creating Arrays

```python
np.arange(1, 10)         # range
np.linspace(0, 10, 5)   # evenly spaced
np.zeros((2,3))         # zeros
np.ones((2,3))          # ones
np.eye(3)               # identity matrix
```

---

## 🔍 Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # first element
print(arr[1:4])    # slicing
```

For 2D arrays:

```python
mat = np.array([[1,2,3], [4,5,6]])
print(mat[0, 1])   # row 0, column 1
```

---

## ➕ Element-wise Operations

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)
```

Operations happen element by element.

---

## 🔄 Reshape Arrays

```python
arr = np.arange(1, 7)
mat = arr.reshape(2, 3)
print(mat)
```

---

## 📏 Broadcasting

NumPy can work with arrays of different shapes.

```python
arr = np.array([1,2,3])
print(arr + 10)
```

---

## 🧮 Mathematical Functions

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
```

---

## 📊 Axis in 2D Arrays

```python
mat = np.array([[1,2,3], [4,5,6]])

print(np.sum(mat, axis=0))  # column-wise
print(np.sum(mat, axis=1))  # row-wise
```

---

## ✅ Boolean Indexing

```python
arr = np.array([5, 12, 7, 20, 3])
print(arr[arr > 10])
```

---

## 🔢 Sorting and Unique

```python
arr = np.array([3, 1, 2, 3, 2])

print(np.sort(arr))
print(np.unique(arr))
```

---

## 🧾 Joining Arrays

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a, b)))
```

---

## ✖️ Matrix Multiplication

```python
A = np.array([[1,2], [3,4]])
B = np.array([[2,0], [1,2]])

print(A @ B)
```

---

## 🔁 Transpose

```python
mat = np.array([[1,2,3], [4,5,6]])
print(mat.T)
```

---

## 💾 Save and Load Arrays

```python
np.save('data.npy', mat)
loaded = np.load('data.npy')
print(loaded)
```

---

## 📝 Practice Exercises

Try these:

1. Create array from 1 to 20 and print even numbers.
2. Reshape an array of size 12 into 3x4.
3. Find max and index in `[10, 45, 7, 32]`.
4. Replace values > 5 with 0 in array 1 to 10.
5. Multiply two 2x2 matrices.

---

## 🛠 Mini Projects

* Student marks analysis
* Temperature data statistics
* Image as matrix
* Random data generator

---

## 📚 How to Learn More

Use these for self study:

* Official docs: [https://numpy.org/doc/](https://numpy.org/doc/)
* Practice on small datasets
* Build small projects
* Read others code

---

## 🎯 Tips for Beginners

* Always print arrays to understand shape.
* Use `.shape` and `.dtype` often.
* Avoid Python loops, use NumPy functions.
* Practice daily.

---

## 🎲 Random Numbers

```python
arr = np.random.rand(5)
print(arr)
```

Use this to create random data for testing and simulations.

---

## 🧠 Advanced Indexing

```python
mat = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(mat[[0, 2], [1, 2]])
```

This picks specific elements using index lists.

---

## 📐 Broadcasting Deep Dive

```python
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
vec = np.array([10, 20, 30])

print(mat + vec)
```

Broadcasting lets arrays of different shapes work together without loops.

---

## 🧮 Linear Algebra Basics

```python
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))
print(np.linalg.inv(A))
```

Useful for matrix math like determinant and inverse.

---

## ⚡ Performance Tips

* Prefer vectorized operations over loops.
* Check `.shape` before operations.
* Use appropriate data types like `float32` when needed.
* Avoid unnecessary copies.

---

## 📖 Glossary

* **ndarray**: Core NumPy array object.
* **Axis**: Direction of operation in arrays.
* **Broadcasting**: Working with different shapes.
* **Vectorization**: Doing operations without loops.

---

## 🧪 Extra Practice

1. Create a 5x5 random matrix and find its mean.
2. Normalize an array to range 0 to 1.
3. Extract the diagonal of a matrix.
4. Replace NaN values with 0.
5. Sort each row of a 2D array.

---

## 🤝 Final Words

This README is your starting book.
Read one section daily, try code, change values, and explore.

With practice, NumPy will become easy and powerful for you.

Happy Learning! 🚀
