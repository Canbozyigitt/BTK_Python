import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,45,25],
    "Column3": ["abc", "bca", "ade", "cba", "dea"]
}

df = pd.DataFrame(data)

def kareAl(x):
    return x * x

kareAl2 = lambda x: x * x

result = df

result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column1"] * 2
result = df["Column1"].apply(kareAl2)
df["Column4"] = df["Column3"].apply(len)
result = df.columns


print(result)