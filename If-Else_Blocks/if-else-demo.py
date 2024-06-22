# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input("İsminizi giriniz: ")
yas = input("Yaşınızı giriniz: ")
egitim = input("Eğitim seviyesi (Lise, Üniversite): ").lower().strip()

if(yas > 18 and (egitim == "lise" or egitim == "üniversite")):
    print(f"{isim} ehliyet alabilirsiniz")
else:
    print(f"{isim} maalesef ehliyet alamazsınız...")