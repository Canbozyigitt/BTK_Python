import pandas as pd

df = pd.read_csv("nba.csv")

# ilk 10 kaydı getiriniz.
result = df.head(10)

# Toplam kaç kayıt vardır?
result = len(df)

# Tüm oyuncuların toplam maaş ortalaması nedir?
result = df["Salary"].mean()

# En yüksek maaşı ne kadardır?
result = df["Salary"].max()

# En yüksek maaşı alan oyuncu kimdir?
result = df[df["Salary"] == df["Salary"].max()]["Name"]

# Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımlar?
result = df[(df["Age"] > 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values("Age", ascending=False)

# "John Holland" isimli oyuncunun oynadığı takım hangisidir?
result = df[df["Name"] == "John Holland"][["Name","Team"]]

# Takımlara göre oyuncuların ortalama maaş bilgisi nedir?
result = df.groupby("Team")["Salary"].mean()

# Kaç farklı takım mevcut?
result = df["Team"].nunique()

# Her takımda kaç oyuncu oynamaktadır?
result = df["Team"].value_counts()

# İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace=True)
result = df[df["Name"].str.contains("and")]



print(result)