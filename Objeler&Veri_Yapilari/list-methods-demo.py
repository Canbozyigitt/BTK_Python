names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1
names.append("Cenk")

# 2 
names.insert(0, "Sena")

# 3
#names.remove("Deniz")

# 4
result = names.index("Deniz")

# 5
result = "Ali" in names

# 6
names.reverse()

# 7
names.sort()

# 8
years.sort()

# 9
str = "Chevrolet, Dacia".split(",")

# 10
years.sort()
maxNumber = years[-1]
minNumber = years[0]

# 11
result = years.count(1998)

# 12
del years

# 13
markalar = []
for i in range(3):
    userInput = input(f"{i}. markayı giriniz: ")
    markalar.append(userInput)





print(names)
print(result)
print(years)