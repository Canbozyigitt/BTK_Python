import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# df = pd.DataFrame([1,2,3,4])

data = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]

df = pd.DataFrame(data, columns=["Name", "Grade"], index=[1,2,3,4])
print(df)