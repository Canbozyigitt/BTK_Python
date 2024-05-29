ogrenciler = {}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phoneNo = input("Öğrenci telefon no: ")

ogrenciler[number] = {
    'name': name.capitalize(),
    'surname': surname.upper(),
    'phoneNo': phoneNo
}

print(ogrenciler)