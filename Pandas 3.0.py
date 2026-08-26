import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/iris.csv")

print(Variable1.info())
print(Variable1.head(5))
print(Variable1.tail(5))
print(Variable1.describe())
print(Variable1["sepal_length"])
print(Variable1[["sepal_length","sepal_width","petal_length", "petal_width"]].mean())
print(Variable1[["sepal_length","sepal_width","petal_length", "petal_width"]].head(5))
print(Variable1[["sepal_length","sepal_width","petal_length", "petal_width"]].tail(5))
print(Variable1[["sepal_length","sepal_width","petal_length", "petal_width"]].min())
print(Variable1[["sepal_length","sepal_width","petal_length", "petal_width"]].max())
print(Variable1["species"].value_counts())
print(Variable1["species"])