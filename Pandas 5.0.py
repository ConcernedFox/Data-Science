import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/titanic(1).csv")

print(Variable1[Variable1["Age"] > 18])
print(Variable1[Variable1["Pclass"] == 1])
print(Variable1[(Variable1["Age"] < 10)|(Variable1["Age"] > 60)])
print(Variable1[Variable1["Gender"] == "female"].head(10))
print(Variable1.iloc[200:501,2:5])
print(Variable1.loc[Variable1["Survived"] == 1, ["Name", "Age", "Fare", "Survived"]])
print(Variable1["Name"].head(10))
Variable1.loc[0:4, ["Name"]] = ["Darth Vader", "Yoda", "General Grievous", "Darth Sidious", "Captain Rex"]
Variable1.loc[0:4, ["Gender"]] = ["Male","Male","Male","Male","Male"]
print(Variable1.iloc[0:5,2:4])