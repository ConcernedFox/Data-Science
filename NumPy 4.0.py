import numpy as np

zero = np.zeros(10, int)
one = np.ones(10, int)
two = np.full(10, 2)
three = np.full(10, 3)
four = np.full(10, 4)
five = np.full(10, 5)
six = np.full(10, 6)
seven = np.full(10, 7)
eight = np.full(10, 8)
nine = np.full(10, 9)
ten = np.full(10, 10)
eleven = np.full(10, 11)
twelve = np.full(10, 12)
thirteen = np.full(10, 13)
fourteen = np.full(10, 14)
fiften = np.full(10, 15)
sixteen = np.full(10, 16)
seventeen = np.full(10, 17)
eighteen = np.full(10, 18)
nineteen = np.full(10, 19)
twenty = np.full(10, 20)
twentyone = np.full(10, 21)
twentytwo = np.full(10, 22)
twentythree = np.full(10, 23)
twentyfour = np.full(10, 24)

print(five)

print(eleven.ndim)

print(eleven.shape)

Array1D = [1]
Array1 = np.array(Array1D)
Array2D = [[1],[1]]
Array2 = np.array(Array2D)
Array3D = [[[1],[1]],[[1],[1]]]
Array3 = np.array(Array3D)
print(type(Array1))

twentyfive = np.zeros((11,11,11), int)
print(twentyfive)
print(twentyfive.ndim)
print(twentyfive.shape)

array = np.arange(1,25)
array = array.reshape(2,3,4)
print(array)
print(array.ndim)

linspace = np.linspace(1, 25, 4)
print(linspace)
#™