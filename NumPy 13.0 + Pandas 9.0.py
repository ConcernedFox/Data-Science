import numpy as np
import pandas as pd
Variable1 = pd.read_csv("/Users/puspendra/Data Science/Data.csv") 
Variable1.info()
print(Variable1.isnull().sum())
six = Variable1["Age"].mean()
four = Variable1["Salary"].mean()
Variable1["Age"] = Variable1["Age"].fillna(value = six)
Variable1["Salary"] = Variable1["Salary"].fillna(value = four)
print(Variable1.isnull().sum())
#Variable1.dropna(inplace = True)
#print(Variable1.isnull())
