import numpy as np

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Array = np.array(List)

Permutation = np.random.permutation(Array)
print(Permutation)

Array = np.random.randint(1, 100, 11)

print(Array)

Array.reshape(1, 1, 11)

Array = np.random.randint(1, 100,(2, 5))

print(Array)

ARRAY = np.sort(Array)
print(ARRAY)

List2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

ARRAY2 = np.array(List2)
ARRAY2 = np.random.permutation(ARRAY2)
print(ARRAY2)
print(ARRAY2[ARRAY2 % 2 == 0])

print(ARRAY2[2:8:1])
print(ARRAY2[9: :-1])

ARRAY2 = np.random.permutation(ARRAY2)
print(ARRAY2)
print(ARRAY2[ARRAY2 > 13])