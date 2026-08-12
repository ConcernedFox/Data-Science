import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/titanic(1).csv")

print(Variable1[Variable1["Age"] > 18])
print(Variable1[Variable1["Pclass"] == 1])
print(Variable1[(Variable1["Age"] < 10)|(Variable1["Age"] > 60)])
print(Variable1[Variable1["Gender"] == "female"].head(10))

