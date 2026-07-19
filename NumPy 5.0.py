import numpy as np

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

Array = np.array(List)

Array = Array.reshape(1, 1, 24)
print(Array)
Array = Array.reshape(1, 2, 12)
print(Array)
Array = Array.reshape(2, 2, 6)
print(Array)
Array = Array.reshape(2, 3, 4)
print(Array)