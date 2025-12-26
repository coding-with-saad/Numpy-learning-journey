"""
Docstring for Pandas.Explore the data.shapes & colums
When the dataset comes we explore how big is the dataset and what are the columns present in the dataset.


In pandas, the shape attribute of a DataFrame returns a tuple representing the dimensions of the DataFrame, specifically the number of rows and columns it contains.

The columns attribute of a DataFrame returns an Index object containing the column labels of the DataFrame.
"""

import pandas as pd

df=pd.read_csv("e:\Machine Learning\Pandas\Chapter 1_Basic Pandas knowledge\employee_dataset_100.csv")
data=pd.DataFrame(df)
print("Shape of the dataset (rows, columns):")
print(data.shape)  # prints the shape of the dataset