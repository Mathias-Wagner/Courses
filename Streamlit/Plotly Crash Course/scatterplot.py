import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/iris.csv")

plotly_templates = ["ggplot2",
                    "seaborn",
                    "simple_white",
                    "plotly",
                    "plotly_white",
                    "plotly_dark",
                    "presentation",
                    "xgridoff",
                    "ygriddoff",
                    "gridon",
                    "none"]

plot = px.scatter(
    data_frame=df,
    x="sepal_length",
    y="petal_length",
    color="species",
    size="sepal_width",
    template="presentation",
    title="Plot of Sepal length vs Petal length"
)

plot.show()