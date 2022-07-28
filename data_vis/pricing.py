#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file             : pricing.py
# @created          : 23-Jul-2022
# @company          : Home
#

"""

"""
from data_vis.main_dash import *


tab_pricing = html.Div([
    html.Div(
        [
            html.Label('place:',
                       style={'width': '8%'}),
            dcc.Dropdown(
                id='place',
                options = [{'label': i, 'value':i} for i in df['place'].unique()],
                value=['bakery'],
                multi=True,
                style = {'width':'80%'}
            ),
            html.Button('Update', id='button',
                        style={'align-items':'left'}        )
        ],
        style = {'widht': '100%', 'display':'flex', 'align-items': 'center'}
    ),
    html.Br(),
    html.Br(),
    html.Div(
        [
            dcc.Checklist(
                id='options',
                options=[
                    {'label': 'Every place', 'value': 'everyplace'}
                ],
                value = []
            )
        ]
    ),
    #dcc.Graph(figure=cases), dcc.Graph(figure=deads)
    dcc.Graph(id='plot_place', figure={}),
    html.Div(
        [
            html.Img(id='image_item', src='',
                  style={'width': '25%', 'height':'50%'}
                  ),
            html.Pre(id='message', children=[], style={'margin-left': '10%',
                                                       'margin-top': '5%'})
        ],
        style={'width': '100%', 'display': 'flex'}
    )
])


@app.callback(
    Output('plot_place', 'figure'),
    [
    Input('button', 'n_clicks')
    ],
    State('place', 'value')
)
def update_plot(button, places):


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

@app.callback(
    [
    Output('image_item', 'src'),
    Output('message', 'children')
    ],
    Input('plot_place', 'clickData'),
    prevent_initial_call=True
)
def click_on(clickData):
    if clickData is not None:
        # {'points': [{'curveNumber': 1, 'pointNumber': 0, 'pointIndex': 0, 'x':
        #              109, 'y': 80, 'text': 'plain donut'}]}
        item_name = clickData['points'][0]['text']
        item = get_object(item_name)
        item_img = item.img

        message = f'Name: {item.name} \n'
        message += f'sell. price: {item.price_sell} \n'
        message += f'time prod.: {item.production_time.seconds/3600} h\n'
        message += f'prod. cost: {item.get_production_price()} \n'
        message += '.......COMPONENTS......... \n'
        for component in item.components:
            message +=  f'{component[0].name}: {component[0].price_sell} x{component[1]} \n'

        return item_img, [message]


@app.callback(
    Output('place', 'value'),
    Input('options', 'value')
)
def check_options(options):
    if 'everyplace' in options:
        return  list(list_places())
    else:
        return ['bakery']
