import numpy as NumPy
import matplotlib.pyplot as Plots

Variable = NumPy.random.randint(1,10,10)
print(Variable)
Variable2 = [1,3,4,7,9,13,14,16,19,20]
Array1 = NumPy.array(Variable2)
Average1 = Array1.mean()
print(Variable2)
Variable3 = [21,25,29,30,33,34,35,38,40,44]
Array2 = NumPy.array(Variable3)
Average2 = Array2.mean()
print(Variable3)
Variable4 = Plots.scatter(Variable2, Variable3, color = "Gold")
#Variable4 = Plots.show()
M = (NumPy.sum((Array1 - Average1)*(Array2 - Average2))/NumPy.sum((Array1 - Average1)**2))
print(M)
C = (Average2 - M*Average1)
print(C)
Y = M*Array1 + C
print(Y)
Y = Plots.plot(Array1, Y, color = "Gold")
Y = Plots.show()
