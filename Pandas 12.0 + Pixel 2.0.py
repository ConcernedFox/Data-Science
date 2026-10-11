import pandas as pd
import plotly.express as pixel

Variable1 = pd.read_csv("/Users/puspendra/Data Science/Covid.csv")
Variable2 = pd.DataFrame(Variable1.groupby(["Country_Region"])["Recovered"].sum().sort_values(ascending = False).head(10))
Variable3 = pd.DataFrame(Variable1.groupby(["Country_Region"])["Deaths"].sum().sort_values(ascending = False).head(10))
Variable6 = pd.DataFrame(Variable1.groupby(["Country_Region"])["Confirmed"].sum().sort_values(ascending = False).head(10))

Variable4 = pixel.scatter(Variable2,x = Variable2.index, y = "Recovered", color = Variable2.index, size = "Recovered", size_max = 100)
Variable4.write_html("Darth_Vader", auto_open = True)
Variable4.show()
Variable5 = pixel.scatter(Variable3, x = Variable3.index, y = "Deaths", color = Variable3.index, size = "Deaths", size_max = 100)
Variable5.write_html("Obi-Wan Kenobi", auto_open = True)
Variable5.show()
Variable7 = pixel.scatter(Variable6, x = Variable6.index, y = "Confirmed", color = Variable6.index, size = "Confirmed", size_max = 100)
Variable7.write_html("Ahsoka Tano", auto_open = True)
Variable7.show()