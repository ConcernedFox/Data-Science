import matplotlib.pyplot as plots
x = ["Mortgage", "Food", "Transport", "Entertainment", "Savings"]
y = [54, 13, 2, 4, 27]
plots.pie(y, labels = x, colors = ["Red", "Blue", "Green", "Yellow", "Purple"], shadow = 1, startangle = 90)
plots.show()
