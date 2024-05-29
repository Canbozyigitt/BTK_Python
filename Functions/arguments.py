def displayUser(**args):
    for key, value in args.items():
        print(f"{key} is {value}")

displayUser(name="Mustafa", age = 20, city = "Kocaeli")