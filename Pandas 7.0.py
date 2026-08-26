import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/iris.csv")

print(Variable1.groupby(["species"])[["sepal_length","petal_length","petal_width","sepal_width"]].mean())
print(Variable1.groupby(["species"])["petal_width"].max())
print(Variable1.groupby(["species"])["petal_width"].min())
print(Variable1.count())
print(Variable1.groupby(["species"])[["petal_length","petal_width"]].mean())
print(Variable1.groupby(["species"])[["petal_length","petal_width"]].max())
print(Variable1.groupby(["species"])["petal_length"].mean())