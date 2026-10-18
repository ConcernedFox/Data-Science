import pandas as pd
import plotly.graph_objects as pixel

Variable1 = pd.read_csv("/Users/puspendra/Desktop/Data Science/WHO-COVID-19-global-data.csv")

Variable1["DateReported"] = pd.to_datetime(Variable1["DateReported"])
Variable2 = (Variable1.groupby(["DateReported"])["New_cases"].sum())
Variable3 = (Variable1.groupby(["DateReported"])["Cumulative_cases"].sum())
Variable4 = (Variable1.groupby(["DateReported"])["New_deaths"].sum())
Variable5 = (Variable1.groupby(["DateReported"])["Cumulative_deaths"].sum())

FIGURE = pixel.Figure()
FIGURE.add_trace(pixel.Scatter(x = Variable2.index, y = Variable2.values))
FIGURE.update_layout(title = "New Cases")
FIGURE.write_html("HAN", auto_open = True)
FIGURE2 = pixel.Figure()
FIGURE2.add_trace(pixel.Scatter(x = Variable3.index, y = Variable3.values))
FIGURE2.update_layout(title = "Cumulative Cases")
FIGURE2.write_html("LUKE", auto_open = True)
FIGURE3 = pixel.Figure()
FIGURE3.add_trace(pixel.Scatter(x = Variable4.index, y = Variable4.values))
FIGURE3.update_layout(title = "New Deaths")
FIGURE3.write_html("LEIA", auto_open = True)
FIGURE4 = pixel.Figure()
FIGURE4.add_trace(pixel.Scatter(x = Variable5.index, y = Variable5.values))
FIGURE4.update_layout(title = "Cumulative Deaths")
FIGURE4.write_html("MANDALORIAN", auto_open = True)
FIGURE.show()
FIGURE2.show()
FIGURE3.show()
FIGURE4.show()

