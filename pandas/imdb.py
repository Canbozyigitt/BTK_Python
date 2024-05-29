import pandas as pd

df = pd.read_csv("sample.csv", encoding="unicode_escape")

# 1- Dosya hakkındaki bilgiler
result = df

# 2- ilk 5 kayıt
result = df.head()

# 3- ilk 10 kayıt
result = df.head(10)

# 4 - Son 5 kayıt
result = df.tail()

# 5 - Son 10 kayıt
result = df.tail(10)

# 6- Sadece Movie_Title kolonunu alın
result = df["title"]

# 7- Sadece Movie_Title kolonunu içeren 5 kaydı alın
result = df["title"].head()

# 8- Sadece Movie_Title ve Rating kolonunu içeren 5 kaydı alın
result = df[["title", "ranking_in_category_guardian"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın
result = df[["title", "ranking_in_category_guardian"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın
result = df[5:][["title", "ranking_in_category_guardian"]].head()

# 11* Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
#result = df[df["imdb"] > 8.0][["title", "ranking_in_category_guardian"]].head(50)

# 12- Yayın tarihi 2000 ile 2015 arasında olan filmlerin isimleri getiriniz.
result = df[(df["year_released"] > 2000) & (df["year_released"] < 2015)][["title", "ranking_in_category_guardian"]]





print(result)