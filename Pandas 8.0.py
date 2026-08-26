import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/iris.csv")

print(Variable1[(Variable1["species"] == "setosa")&(Variable1["sepal_length"] > 5)])
print(Variable1[(Variable1["species"] == "versicolor")&(Variable1["petal_length"] > 4)])
print(Variable1[(Variable1["species"] == "virginica")&(Variable1["petal_width"] > 2)])
print(Variable1.loc[Variable1["petal_length"] > 5, ["species", "sepal_length", "petal_length"]])
print(Variable1[(Variable1["species"] == "setosa")|(Variable1["species"] == "virginica")])
print(Variable1[(Variable1["sepal_length"] > 6)&(Variable1["petal_width"] > 1.5)])
print(Variable1[(Variable1["sepal_length"] > 6)|(Variable1["petal_length"] > 5)])
print(Variable1[(Variable1["species"] == "versicolor")|(Variable1["species"] == "virginica")])
print((Variable1["species"] != "setosa").sum())