#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : visualization.py
# @created          : 24-Aug-2020
# @company          : Home
#

"""

"""
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots


from functions import  *
df = generate_df()


#Columns
#['production_time', 'profit', 'item_name', 'price_sell', 'profit_per_hour',
# 'prod_cost', 'place']


#plot = go.Scatter(
#    x = df['prod_cost'],
#    y = df['profit_per_hour'],
#    mode = 'markers',
#    marker = dict(color=df ['place'])
#
#)

#fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                 size='petal_length', hover_data=['petal_width'])
fig = px.scatter(df, x='prod_cost',
                 y = 'profit_per_hour',
                 color ='place',
                 hover_name = 'item_name',
                 hover_data = ['production_time', 'price_sell']

                 )

fig.update_layout(title='Hay day')
#fig.show()



#Save html
#figure.write_html('first_figure.html', auto_open=True)
app = dash.Dash()
app.layout = html.Div([
    #dcc.Graph(figure=cases), dcc.Graph(figure=deads)
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
