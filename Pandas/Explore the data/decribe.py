"""
Docstring for Pandas.Explore the data.decribe

Describe function in pandas provides a summary of statistics for numerical columns in a DataFrame. It includes measures such as count, mean, standard deviation, minimum, maximum, and quartiles.


Standard deviation (std) is a measure of the amount of variation or dispersion in a set of values. A low standard deviation indicates that the values tend to be close to the mean, while a high standard deviation indicates that the values are spread out over a wider range.

Mean (average) is the sum of all values divided by the number of values. It represents the central value of a dataset.


Count represents the number of non-null entries in a column.


Quatile Deviation is a statistical measure that describes the spread of data points in a dataset. It is calculated as the difference between the upper quartile (Q3) and the lower quartile (Q1), representing the range within which the central 50% of the data points lie.

"""
import pandas as pd

data={
    "Name":["Saad","Bob","Charlie","David","Eva"],
    "Age":[24,27,22,32,29],
    "City":["New York","Los Angeles","Chicago","Houston","Phoenix"],
    "Performance":[88,92,95,70,85]
}

df=pd.DataFrame(data)
print("sample dataframe")
print(df)
print("Descriptive statistics of the dataframe")
print(df.describe())
