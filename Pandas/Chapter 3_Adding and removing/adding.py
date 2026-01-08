import pandas as pd

data = {
    "Name": ["Saad","Safa", "Ahmed"],
    "Age": [20, 22, 21]
}

df = pd.DataFrame(data)
print(df)

df.loc[3] = ["Lina", 23]
print(df)

df["Marks"] = [85, 90, 88,32]
print(df)


df["Age_after_5_years"] = df["Age"] + 5
print(df)
df["Passed"] = df["Marks"] > 86
df["Passed"]=df["Passed"].replace({True:"Pass",False:"Fail"})
print(df)


df["Remarks"] = ["Good" if mark > 88 else "Average" for mark in df["Marks"]]
print(df)