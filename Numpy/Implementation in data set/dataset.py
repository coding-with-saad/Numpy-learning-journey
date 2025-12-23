"""
Docstring for Numpy.Implementation in data set.dataset

This module demonstrates how to implement NumPy functionalities in a dataset using Pandas DataFrame.


Pandas libraries plays a important role in machine learning.They help to manipulate and analyze data efficiently, especially when dealing with large datasets, by providing powerful data structures like DataFrames that are built on top of NumPy arrays.


And

Numpy provides support for multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
"""


import pandas as pd
import numpy as np

df=pd.read_csv(r'E:\Numpy\Numpy\Implementation in data set\employee_dataset_100.csv')
print(df.head())


print("When the data set comes you first check the missing values in the data set. The syntax is:")
print(df.isnull().sum())


print("we see that some missing values are come soo we handle it first The syntax is:")
# Handling missing values by replacing with mean for numerical columns
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
# Handling missing values by replacing with mode for categorical columns
df['Department'].fillna(df['Department'].mode()[0], inplace=True)


print(df.isnull().sum())
