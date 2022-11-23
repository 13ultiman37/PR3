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
fig.add_trace(go.Box(y=years, x=name))

fig.show()
