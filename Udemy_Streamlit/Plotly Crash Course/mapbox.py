import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/us-cities-top-1k.csv")

plot = px.scatter_mapbox(data_frame=df,
                         lat="lat",
                         lon="lon",
                         hover_name="City",
                         size="Population",
                         zoom=4,
                         title="Popluation across different cities",
                         mapbox_style="open-street-map")

plot.show()