"""
In this file we make her own dataset using pandas DataFrame.
to save this dataset use df.to_csv("file_path.csv") function.

"""
import pandas as pd

data={
    "Name":["Saad","Bob","Charlie","David","Eva"],
    "Age":[24,27,22,32,29],
    "City":["New York","Los Angeles","Chicago","Houston","Phoenix"]
}

df=pd.DataFrame(data)
print(df)
print(df.info())  # to summarize our dataset

df.to_csv("E:\Machine Learning\Pandas\Chapter 1_Basic Pandas knowledge\own data.csv")