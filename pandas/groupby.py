import pandas as pd
import numpy as np

personeller = {
    "Çalışan": ["Ahmet Yılmaz", "Can Ertürk", "Hasan Korkmaz", "Cenk Saymaz", "Ali Yürek", "Mustafa Haita", "Buse Ateşçi"],
    "Departman": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Yazılımcı", "Yazılımcı", "Doktor"],
    "Yaş": [30,25,45,50,23,34,43],
    "Semt": ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Maltepe", "Tuzla", "Kadıköy"],
    "Maaş": [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df

result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman", "Semt"]).groups

semtler = df.groupby("Semt")

# for name, group in semtler:
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Maaş"].max()["Yazılımcı"]
result = df.groupby("Departman").agg(np.mean)



print(result)