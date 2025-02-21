import pandas as pd
import plotly.express as px

df = pd.read_csv("../Materials/tips.csv")

plot = px.pie(data_frame=df,
              values="tip",
              names="sex",
              facet_col="smoker",
              hole=0.6,
              title="Pie Chart")

plot.show()