import matplotlib.pyplot as plots

x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
math = [90, 80, 60, 120, 100]
language = [15, 10, 25, 30, 10]
history = [40, 50, 55, 70, 50]
geography = [30, 50, 40, 20, 40]
science = [80, 60, 70, 50, 70]

plots.stackplot(x, math, language, history, geography, science,colors = ["Red", "Green", "Purple", "Orange", "Blue"], labels = ["Math", "Language", "History", "Geography", "Science"])
plots.legend()
plots.show()
