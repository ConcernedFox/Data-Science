import numpy as np

x = [11, 24, 10, 7, 13]
x = np.array(x)
y = [1, 2, 3, 4, 5]
y = np.array(y)


z = ((x*2)+y)-3

print(z)

cylinder = []
cylinder = np.random.randint(1, 50, 10)
print(cylinder)
height = []
height = np.random.randint(1, 50, 10)
print(height)
SA = []
def form():
    formula = cylinder * 3.14 * 2 * height
    print(formula)
    SA = [formula]
form()