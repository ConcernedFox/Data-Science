import matplotlib.pyplot as plots
import numpy as np

Listx = np.arange(-5, 5, 0.1)
print(Listx)

Listy = Listx
Listz = Listx*Listx
Listw = Listz*Listx
plots.xlabel("?")
plots.ylabel("??")
plots.title("???")
plots.plot(Listx, Listy, label = "y = x")
plots.plot(Listx, Listz, label = "y = x**2")
plots.plot(Listx, Listw, label = "y = x**3")
plots.legend()
plots.show()