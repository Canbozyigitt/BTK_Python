import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x, y, "o--r")
plt.axis([0,6,0,20])

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
"""

"""
x = np.linspace(0,2,100)

plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Simple Plot")

plt.legend()

plt.show()
"""

"""
x = np.linspace(0,2,100)
fig, axis = plt.subplots(2)

axis[0].plot(x, x, color="red")
axis[1].plot(x, x**2, color="green")

plt.show()
"""
df = pd.read_csv("../pandas/datasets/nba.csv")

df = df.drop(["Number", "Name", "College", "Position", "Height"], axis=1).groupby("Team").agg(lambda x: np.mean(x))
df.plot(subplots=True)
plt.legend()

plt.show()
