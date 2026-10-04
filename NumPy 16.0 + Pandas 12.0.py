import numpy as np
import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/Covid.csv")
Variable2 = Variable1[["Country_Region","Confirmed", "Active", "Deaths", "Recovered"]]

print(Variable2["Confirmed"].sum())
print(Variable2["Active"].sum())
print(Variable2["Deaths"].sum())
print(Variable2["Recovered"].sum())
Darth_Vader = Variable2.groupby(["Country_Region"])[["Deaths", "Recovered"]].sum()
Darth_Vader = Darth_Vader[Darth_Vader["Deaths"] > Darth_Vader["Recovered"]]
print(Darth_Vader)
print(Variable2["Confirmed"].mean())

