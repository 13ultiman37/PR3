import matplotlib
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

matplotlib.use('TkAgg')

import pandas as pd

df = pd.read_csv("Avocado.csv", delimiter=',')
year2015 = df.loc[(df.year == 2015)]
avg2015Price = year2015['AveragePrice'].mean()

year2016 = df.loc[(df.year == 2016)]
avg2016Price = year2016['AveragePrice'].mean()

year2017 = df.loc[(df.year == 2017)]
avg2017Price = year2017['AveragePrice'].mean()

year2018 = df.loc[(df.year == 2018)]
avg2018Price = year2018['AveragePrice'].mean()

years = [avg2015Price, avg2016Price, avg2017Price, avg2018Price]
name = ['2015', '2016', '2017', '2018']

fig = go.Figure()
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightBlue')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightBlue')
fig.add_trace(go.Scatter(x=name, y=years, line_color="crimson",
                         marker=dict(color='darkblue', line=dict(color='black', width=2))))
fig.update_layout(title={'text': 'Диаграмма средней цены на авокадо', 'font_size': 20}, title_x=0.5,
                  xaxis_title={'text': 'Год', 'font_size': 16},
                  yaxis_title={'text': 'USD', 'font_size': 16},
                  xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_tickangle=270,
                  margin=dict(l=100, r=100, t=100, b=100),
                  showlegend=True,
                  legend=dict(yanchor="bottom", xanchor="left", x=0, y=0))

fig.show()
