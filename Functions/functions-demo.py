# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def display(adet, kelime):
    for i in range(adet):
        print(kelime)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.
def toList(*args):
    list = []
    for i in range(len(args)):
        list.append(args[i])
    return list

result = toList("Mustafa", "Haita", "Egemen")

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalBul(num1, num2):
    asalSayilar = []
    for i in range(num1, num2+1):
        if i > 1:
            for k in range(2, i):
                if(i % k == 0):
                    break
        else:
            asalSayilar.append(i)
    return asalSayilar