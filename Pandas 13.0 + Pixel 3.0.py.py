import pandas as pd
import plotly.graph_objects as pixel

CSV_File = pd.read_csv("/Users/puspendra/Desktop/Data Science/WHO-COVID-19-global-data.csv")
CSV_File.info()
CSV_File["DateReported"] = pd.to_datetime(CSV_File["DateReported"])
CSV_File.info()
NEWCASE = (CSV_File.groupby(["DateReported"])["New_cases"].sum())
print(NEWCASE)
FIGURE = pixel.Figure()
FIGURE.add_trace(pixel.Scatter(x = NEWCASE.index, y = NEWCASE.values))
FIGURE.update_layout(title = "YODA")
FIGURE.write_html("YODA", auto_open = True)
FIGURE.show()