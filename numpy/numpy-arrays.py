import numpy as np

result = np.array([1,3,5,7,9])
result = np.arange(1, 10)
result = np.arange(10,100,3)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0, 100, 5) # [  0.  25.  50.  75. 100.]
result = np.linspace(0, 5, 5) # [0.   1.25 2.5  3.75 5.  ]
result = np.random.randint(1, 10) 
result = np.random.randint(1, 10, 3) # [6 4 5] rastgele

print(result)