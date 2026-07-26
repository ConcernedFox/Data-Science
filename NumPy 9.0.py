import numpy as np

List = np.random.randint(1, 15, 15)

Array = np.array(List)
print(Array)

len1 = len(Array[Array < 8])
len2 = len(Array[Array > 10])
len3 = len(Array[Array % 2 == 1])
print(Array[Array < 8])
print(Array[Array > 10])
print(Array[Array % 2 == 1])

print(len1 + len2 + len3)