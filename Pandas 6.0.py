import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/titanic(1).csv")

Variable1["Gender"] = Variable1["Gender"].replace({"male":"M", "female":"F"})
print(Variable1["Gender"])

print(Variable1[["Gender", "Survived", "Pclass", "Name", "Age", "Fare", "Parents/Children Aboard", "Siblings/Spouses Aboard"]].head())
print(Variable1[Variable1["Pclass"] == 1]["Age"].mean())
print(Variable1.groupby("Pclass")["Age"].mean())
print(Variable1.groupby(by = ["Pclass","Gender"])[["Age","Fare"]].mean())