# import pandas as pd

# data = {
#     "Name": ["Ali", "Sara", "Ahmed"],
#     "Age": [20, 22, 21]
# }

# df = pd.DataFrame(data)
# print(df)


import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zara"],
    "Age": [20, 22, 21, 23],
    "Marks": [85, 90, 88, 92]
}

df = pd.DataFrame(data)
print(df)
print(df.iloc[0]) # First row by position
print(df.iloc[1]) # Second row by position
print(df.iloc[0:3]) # First three rows by position
print(df.iloc[0, 1]) # Element at first row, second column by position
print(df.iloc[0:2, 0:2]) # First two rows and first two columns by position
print(df.loc[0]) # First row by label
print(df.loc[:, "Name"]) # All rows for 'Name' column by label
print(df[df["Marks"] > 88]) #show rows where Marks > 88
print(df.sort_values("Age")) #show age in assending order