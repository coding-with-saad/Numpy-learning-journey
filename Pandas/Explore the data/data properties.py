import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 22, 21],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df) 
print(df.head()) #show first 3 row
print(df.tail()) #show last 3 row
print(df.describe()) #statistical summary
print(df.columns) #list of columns
print(df.combine) #function to combine dataframes
print(df.shape) #show the shape of data
print(df.info()) #summary of dataframe
print(df.dtypes) #data types of each column
print(df.isnull().sum()) #check for missing values