"""
Docstring for Pandas.Chapter 1_Basic Pandas knowledge.basic

Data Manipulation means transforming data into a format that is easier to read and analyze. This includes tasks such as cleaning, filtering, aggregating, and reshaping data.

Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making.



Sometimes one error come unicode error while reading csv file in pandas. To avoid this error use encoding parameter while reading csv file.


latin-1 encoding: Latin-1 (also known as ISO-8859-1) is a character encoding standard that can represent the first 256 Unicode characters. It is commonly used for Western European languages.


Encoding is the process of converting data from one form to another. In the context of text files, encoding refers to the way characters are represented in bytes. Different encoding schemes can represent the same characters using different byte sequences.


if the data are stored in cloud or platform(such as google colab,google storage) then we install python libraray name gcsfs.

pd.read_json()
pd.read_xls()
"""

import pandas as pd

df=pd.read_csv("e:\Machine Learning\Pandas\Chapter 1_Basic Pandas knowledge\employee_dataset_100.csv")

print(df)
print(df.head(10)) # displays first 10 rows
print(df.tail(10)) # displays last 10 rows
print("Display the info of dataset")
print(df.info()) # displays the info of dataset