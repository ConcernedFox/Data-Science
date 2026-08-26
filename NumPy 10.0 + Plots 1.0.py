import matplotlib.pyplot as plots
import numpy as np

Listx = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,.9,1,281,397,885,870,214,165,208,366,660,1000]
Listy = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,.9,1,281,397,885,870,214,165,208,366,660,1000]
plots.plot(Listx, Listy, "r--")
plots.xlabel("Students")
plots.ylabel("Marks")
plots.axis((-10000, 10000, -10000, 10000))
plots.title("0-10:Marks of Vice Admiral Holdo's students/10-20:Marks of Yoda's students")

plots.legend()
plots.show()