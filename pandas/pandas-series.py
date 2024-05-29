import pandas as pd

# data
numbers = [20,30,40,50]

pandas_series = pd.Series(numbers)


opel2018 = pd.Series([20,30,40,10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40,30,20,10], ["astra", "corsa", "grandland", "insignia"])

total = opel2018 + opel2019
print(total["astra"])