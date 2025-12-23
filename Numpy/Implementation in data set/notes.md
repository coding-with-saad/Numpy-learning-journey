Good question, Malik. You don’t need to ignore the warning. You should **change the way you fill values** so it is safe for future Pandas versions.

The warning comes because of this pattern:

```python
df['Salary'].fillna(..., inplace=True)
```

Pandas says this may not work in pandas 3.0.

---

## ✅ Best way to manage the warning

Use **assignment instead of `inplace=True`**.

### ✔ Replace your lines with:

```python
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
```

This directly updates the DataFrame and removes the warning.

---

## ✅ Or fill multiple columns together

```python
df = df.fillna({
    'Salary': df['Salary'].mean(),
    'Age': df['Age'].mean(),
    'Department': df['Department'].mode()[0]
})
```

Clean and future-safe.

---

## ❌ What not to use now

Avoid:

```python
df['col'].fillna(value, inplace=True)
```

This is what triggers the warning.

---

## 🎯 Why this works

* You are not modifying a slice.
* You assign the result back to the column.
* Pandas is happy. No warning.

---

## 📝 Short summary

To manage the warning:

* Stop using `inplace=True` with `df['col']`.
* Use assignment or `df.fillna({...})`.

After this, your code will run cleanly without warnings.
