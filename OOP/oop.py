class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def intro(self):
        print("Hello there")

    def calculateAge(self):
        return 2024 - self.year
    
class Circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevreHesapla(self):
        return 2 * self.pi + self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)

p1 = Person(name="Mustafa", year=2004)

print(f"{p1.name} {p1.year}")

