"""
Docstring for Pandas.Explore the data.1

When the dataset is ready, we can explore it using various pandas functions.

Explore steps:
Understand the dataset structure and contents.
Identify missing values or inconsistencies.
plan next steps for data cleaning or analysis.


1. Import pandas library.
2. Load the dataset using pd.read_csv("file_path.csv").
3. Use df.head() to view the first few rows of the dataset.

"""
import pandas as pd

df=pd.read_csv("e:\Machine Learning\Pandas\Chapter 1_Basic Pandas knowledge\employee_dataset_100.csv")

print("Display the info of dataset")
print(df.info())