import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/iris.csv")

# plot = px.box(
#     data_frame=df,
#     x="species",
#     y="sepal_width",
#     color="species",
#     title="Boxplot of Sepal width across different species"
# )

# plot.show()

plot1 = px.violin(
    data_frame=df,
    x="species",
    y="sepal_width",
    color="species",
    title="Boxplot of Sepal width across different species"
)

plot1.show()