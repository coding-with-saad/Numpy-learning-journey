"""
Docstring for Numpy.Implementation in data set.dataset

This module demonstrates how to implement NumPy functionalities in a dataset using Pandas DataFrame.


Pandas libraries plays a important role in machine learning.They help to manipulate and analyze data efficiently, especially when dealing with large datasets, by providing powerful data structures like DataFrames that are built on top of NumPy arrays.


And

Numpy provides support for multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
"""


from ast import Or
import pandas as pd
import numpy as np

df=pd.read_csv(r'E:\Numpy\Numpy\Implementation in data set\employee_dataset_100.csv')
print(df.head())


print("When the data set comes you first check the missing values in the data set. The syntax is:")
print(df.isnull().sum())


print("we see that some missing values are come soo we handle it first The syntax is:")

# Fill missing values
# Handling missing values by replacing with mean for numerical columns
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Handling missing values by replacing with mode for categorical columns
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# This section handles infinite values and fills missing values with the mean of each column
df.replace([np.inf, -np.inf], np.nan, inplace=True)


# Remove duplicates Values
df.drop_duplicates(inplace=True)

# Replace negatives salary
df["Salary"]=np.where(df['Salary']<0,df['Salary'].mean(),df['Salary'])

salary_mean=df["Salary"].mean()
print("Mean Salary after replacing negatives:", salary_mean)
salary_std=df["Salary"].std()
print("Standard Deviation Salary after replacing negatives:", salary_std)
lower_bound=salary_mean - 3*salary_std
print("Lower Bound Salary after replacing negatives:", lower_bound)
upper_bound=salary_mean + 3*salary_std
print("Upper Bound Salary after replacing negatives:", upper_bound)

# remove rows were salary is to higher than upper bound
df=df[(df["Salary"]>=lower_bound) & (df["Salary"]<=upper_bound)]


# Save the updated DataFrame back to CSV
df.to_csv(r'E:/Numpy/Numpy/Implementation in data set/Cleaned data.csv', index=False)
print("Data Cleaning Completed. Check the cleaned data file.")


print(df.isnull().sum())










"""
Pandas is saying:
“You are modifying a column slice. In future versions, this may not update the original DataFrame.”
Right now it still works, but in pandas 3.0 this may stop working.
"""
# # Handling missing values by replacing with mean for numerical columns
# df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# # Handling missing values by replacing with mode for categorical columns
# df['Department'].fillna(df['Department'].mode()[0], inplace=True)
# df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)
"""
Or 
you can also use a dictionary to fill multiple columns at once:
"""

# df.fillna({
#     'Salary': df['Salary'].mean(),
#     'Age': df['Age'].mean(),
#     'Department': df['Department'].mode()[0]
# }, inplace=True)
