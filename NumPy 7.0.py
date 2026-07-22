import numpy as np

Array = np.random.randint(1, 50, 10)

Array = np.sort(Array)

print(Array[0])
print(Array[9])
print(Array)

Array = np.random.permutation(Array)
print(Array)

Array = Array.reshape(1, 2, 5)
print(Array)

Array = np.sort(Array)

print(Array)

Array[Array % 2 == 0] = 0
Array[Array % 2 == 1] = 1
print(Array)