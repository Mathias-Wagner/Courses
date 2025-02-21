import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/iris.csv")
df1 = (df
       .groupby(by=["species"])
       .mean()
       .reset_index())

plot = px.bar(
    data_frame=df1,
    x="species",
    y="petal_width",
    title="Bar chart showing average petal width across species"
)

plot.show()