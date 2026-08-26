import matplotlib.pyplot as plots
import numpy as np
m = int(input("What is your value for m?"))
c = int(input("What is your value for c?"))

x = np.arange(-20, 20, 1)
y = m*x + c

plots.plot(y)
plots.show()