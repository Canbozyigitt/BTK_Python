import pandas as pd
import numpy as np

df = pd.read_csv("datasets/GBvideos.csv")

# İlk 10 kaydı getiriniz.
result = df.head(10)

# İkinci 5 kaydı getiriniz.
result = df[5:].head()

# Dataset'de bulunan kolon isimlerini ve sayısını bulunuz.
result = df.columns 
result = df.columns.size

#Aşağıda bulunan kolonları silin ve kalan kolonları listeleyin
# (thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description)
result = df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis=1)

# Beğenme ve beğenmeme sayılarının ortalamasını bulunuz.
result = df["likes"].mean()
result = df["dislikes"].mean()

# ilk 50 videonun like ve dislike kolonunu getiriniz.
result = df[["likes", "dislikes"]].head(50)

# en çok görüntülenen video hangisidir?
result = df[df["views"].max() == df["views"]]

# en düşük görüntülenen video hangisidir?
result = df[df["views"].min() == df["views"]]

# en fazla görüntülenen ilk 10 video hangileridir?
result = df.sort_values("views", ascending=False)[["title", "views"]]

# Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
#result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# Her kategoride kaç video vardır.
result = df["category_id"].value_counts()

# kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
#result = df.groupby("category_id").sum().sort_values("comments")["title"]



print(result)