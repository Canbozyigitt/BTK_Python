# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = int(input("Bir sayı giriniz: "))
if(sayi > 0 and sayi < 100):
    print("Girdiğiniz sayı 0 ile 100 arasında.")
else:
    print("Girdiğiniz sayı 0 ile 100 aralığında değil.")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Bir sayı giriniz: "))
if(sayi > 0):
    if(sayi % 2 == 0):
        print("Girilen sayı pozitif bir çift sayıdır.")
    else:
        print("Girilen sayı pozitif bir tek sayıdır.")
else:
    print("Girilen sayı bir çift sayı değildir.")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
loggedEmail = "canbozyigit@gmail.com"
loggedPassword = "1234567"
emailInput = input("Email adresi: ")
passwordInput = input("Şifre: ")

if((loggedEmail == emailInput.lower().strip()) and (loggedPassword == passwordInput)):
    print("Giriş başarılı.")
else:
    print("Bilgiler uyuşmuyor.")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
numbers = []
for i in range(3):
    num = int(input(f"{i + 1}. sayıyı giriniz: "))
    numbers.append(num)
numbers.sort()
numbers.reverse()
numStr = f"{numbers[2]} < {numbers[1]} < {numbers[0]}"
print(numStr)
