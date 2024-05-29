import numpy as np

py_list = [1,2,3,4,5,6,7,8,9]

np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(np_array))

py_multi = np_array.reshape(3,3)
print(py_multi)

print(py_multi.ndim)

print(py_multi.shape)