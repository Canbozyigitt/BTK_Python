website = "http://www.mustafahaita.com"
course = "Python Kursu: Baştan Sona Python Programlama"

result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()

result = website.lstrip("/:pth") # www.mustafahaita.com

result = website.strip("w.moc") # http://www.mustafahaita

result = course.lower() # python kursu: baştan sona python programlama
result = course.upper() 
result = course.title() # Python Kursu: Baştan Sona Python Programlama

result = website.count("a") # 4

result = website.lstrip(":/pth").startswith("www") # True
result = website.endswith(".com") # True

result = website.find(".com") # 23

result = "Hello World".replace("World", "There") # Hello There

result = course.split(" ") # ['Python', 'kursu:', 'Baştan', 'Sona', 'Python', 'Programlama']




print(result)