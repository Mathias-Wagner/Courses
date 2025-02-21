import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/iris.csv")

plot = px.histogram(data_frame=df,
                    x="sepal_length",
                    nbins=15,
                    title="Distribution of sepal length")

plot.show()