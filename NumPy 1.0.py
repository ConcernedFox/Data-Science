import numpy as np

Number_List = [1,11,3,4,23,24,7,44,81,55,92]
print(Number_List)
print(type(Number_List))
Number_Array = np.array(Number_List)
print(Number_Array)
print(type(Number_Array))
for i in range(len(Number_List)):
    Number_List[i] += 1
    print(Number_List[i])

print(Number_List)

List = [1, 2, 3, 4, 5]

print(List)

Array = np.array(List)
print(Array)
print(type(Array))

Array = Array + 1
print(Array)

Array = Array - 1
print(Array)

Array = Array * 2
print(Array)