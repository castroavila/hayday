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
from dash.dependencies import Input, Output, State
import random

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
# fig = px.scatter(df, x='prod_cost',
#                  y = 'profit_per_hour',
#                  color ='place',
#                  hover_name = 'item_name',
#                  hover_data = ['production_time', 'price_sell']

#                  )

# fig.update_layout(title='Hay day')
#fig.show()



#Save html
#figure.write_html('first_figure.html', auto_open=True)
app = dash.Dash(assets_folder='images')
app.layout = html.Div([
    html.Div(
        [
            html.Label('place:',
                       style={'width': '8%'}),
            dcc.Dropdown(
                id='place',
                options = [{'label': i, 'value':i} for i in df['place'].unique()],
                value=['bakery'],
                multi=True,
                style = {'width':'50%'}
            ),
            html.Button('Update', id='button',
                        style={'align-items':'left'}        )
        ],
        style = {'widht': '50%', 'display':'flex', 'align-items': 'center'}
    ),
    #dcc.Graph(figure=cases), dcc.Graph(figure=deads)
    dcc.Graph(id='plot_place', figure={})
])

@app.callback(
    Output('plot_place', 'figure'),
    [
    Input('button', 'n_clicks'),
    Input('plot_place', 'clickData'),
    ],
    State('place', 'value')
)
def update_plot(button, clickData, places):


    if clickData is not None:
        # {'points': [{'curveNumber': 1, 'pointNumber': 0, 'pointIndex': 0, 'x':
        #              109, 'y': 80, 'text': 'plain donut'}]}
        print(clickData['points'][0]['text'])
    figure = make_subplots(rows=1, cols=1)
    random.seed(0)

    for place in places:
        df_place = df[df['place'] == place]

        tracer = go.Scatter(x=df_place['prod_cost'], y=df_place['profit_per_hour'],
                            name=place,
                            # customdata=[f'name: {name}<br>price sell: {price_sell}<br>prod. time: {prod_time}'
                            #             for  name, price_sell,  prod_time in
                            #             zip(df_place['item_name'], df_place['price_sell'],
                            #                 df_place['production_time']) ],
                            # customdata=df_place['item_name'].values,
                            text=df_place['item_name'],
                            hovertemplate= '%{text} <br>' +
                            'prod.cost: %{x:0.2f}<br>' +
                            'per_hour:%{y:0.2f} <br>',
                            # +  'name: %{customdata}',
                            # + [f'name: {i}' for i in df_place["item_name"].values],
                            # + '%{customdata}',
                            showlegend=True,
                            mode = 'markers',
                            marker= dict(color=generate_color())

                        )
        figure.add_trace(tracer)

    figure.update_layout(title='Hay day')
    figure.update_yaxes(title_text = 'Profit per hour')
    figure.update_xaxes(title_text= 'production cost')
    #figure.update_layout(hovermode='x unified')
    return figure

def generate_color():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color

# @app.callback(
#     Input('plot_place', 'clickData')
# )
# def click_on(clickData):
#     print(clickData)


app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
