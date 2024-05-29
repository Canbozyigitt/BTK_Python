import pandas as pd

data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

#data["Name"] = data["Name"].str.upper()
#data["index"] = data["Name"].str.find("a")
#data = data[data["Name"].str.contains("Jordan")]
#data = data["Team"].str.replace(" ", "-")

print(data.head(10))

