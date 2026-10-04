import numpy as np
import pandas as pd

Variable1 = pd.read_csv("/Users/puspendra/Data Science/Covid.csv")
Variable2 = Variable1[["Country_Region","Confirmed", "Recovered", "Deaths", "Active"]]
Variable2.info()
print(Variable2[Variable2["Country_Region"] == "India"].sum())
Luke_Skywalker = pd.DataFrame(Variable2.groupby(["Country_Region"])["Confirmed"].sum().sort_values(ascending = False).head(10))
# print(Variable2.groupby(["Country_Region"])["Recovered"].sum().sort_values(ascending = False).head(10))
# print(Variable2.groupby(["Country_Region"])["Deaths"].sum().sort_values(ascending = False).head(10))
# print(Variable2.groupby(["Country_Region"])["Active"].sum().sort_values(ascending = False).head(10))
print(Luke_Skywalker)
import plotly.express as pixel
Obi_Wan_Kenobi = pixel.scatter(Luke_Skywalker,x = Luke_Skywalker.index, y = ["Confirmed"], color = Luke_Skywalker.index)
Obi_Wan_Kenobi.write_html("Darth_Vader", auto_open = True)
Obi_Wan_Kenobi.show()
