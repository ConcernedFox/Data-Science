import numpy as np
import pandas as pd
Variable1 = pd.read_csv("/Users/puspendra/Data Science/titanic.csv")
Variable1.info()
Age = Variable1["Age"].mean()
Cabin = ("C" + str(np.random.randint(1, 100, 1)))
Embarked = Variable1["Embarked"].mode()[0]
Variable1["Age"] = Variable1["Age"].fillna(value = Age)
Variable1["Cabin"] = Variable1["Cabin"].fillna(value = Cabin)
Variable1["Embarked"] = Variable1["Embarked"].fillna(value = Embarked)
Variable1.info()
print(Variable1.isnull().sum())