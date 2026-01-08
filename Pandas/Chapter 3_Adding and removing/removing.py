import pandas as pd

data = {
    "Name": ["Saad","Safa", "Ahmed"],
    "Age": [20, 22, 21]
}

df = pd.DataFrame(data)
print(df)

df.loc[3] = ["Lina", 23]
print(df)

df["Passed"] = "Yes"
print(df)
df.drop("Passed", axis=1, inplace=True)
print(df)

df["Age_after_5_years"] = df["Age"] + 5
print(df)
df.drop(["Age_after_5_years"], axis=1, inplace=True)
print(df)
