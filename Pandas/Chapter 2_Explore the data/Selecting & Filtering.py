"""
Docstring for Pandas.Explore the data.Selecting & Filtering

When you have a dataset, you often need to select specific rows or columns based on certain conditions. Pandas provides powerful tools for selecting and filtering data in DataFrames.


when you have a dataset you know how to select specific rows or columns based on certain conditions using pandas.
filter rows based on conditions using boolean indexing.
combine multiple conditions using logical operators (& for AND, | for OR).
square brackets [] to select columns by name.
.loc[] and .iloc[] for label-based and position-based indexing, respectively.

Access multiple columns syntax: df[['Column1', 'Column2']]
filter rows based on condition syntax: df[df['Column'] > value]
if the condition is more than one what th synatx: df[(df['Column1'] > value1) & (df['Column2'] < value

"""


import pandas as pd

df=pd.read_csv("e:\Machine Learning\Pandas\Chapter 1_Basic Pandas knowledge\employee_dataset_100.csv")
data=pd.DataFrame(df)
print(df)
 
print("Select specific columns (e.g., 'Name' and 'Age'):")
print(df[['Name', 'Age']])