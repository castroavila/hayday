#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : graph_vis.py
# @created          : 24-Jul-2022
# @company          : Home
#

"""

"""
from data_vis.main_dash import *


tab_graph = html.Div(
    [
        html.Div(
            [
                html.Label('place:',
                           style={'width': '3%'}),
                dcc.Dropdown(
                    id='place_from',
                    options = [{'label': i, 'value':i} for i in df['place'].unique()],
                    value='bakery',
                    multi=False,
                    style = {'width':'200px', 'align-items': 'left'}
                ),
                html.Div(
                    [
                        dcc.RadioItems(
                            id='items_in_place',
                            options=[],
                            value='',
                            labelStyle ={'display': 'flex'},
                            style={'height': '20%'}
                        ),
                    ],
                    style={'maxHeight': '200px', 'overflow': 'scroll',
                           'height': '200px'}

                )

            ],
            style = {'widht': '20%', 'display':'flex', 'align-items': 'center',
                     'height': '10%'}
        ),
        html.Br(),
        html.Img(id='image_place',
                 src='',
                 style={'width': '25%', 'height':'50%'}
                 )
    ]
)

@app.callback(
    [
        Output('image_place', 'src'),
        Output('items_in_place', 'options')
    ],
    Input('place_from', 'value')
)
def update_graph(place_from):
    items = list_products_at(place_from)
    options = {item.name: item.name for item in items}
    radio_items = []
    for item in items:
        radio_item = {
            'label': html.Div(
                [
                    html.Img(src=item.img, height=50,
                             style={'padding-left':10}
                             ),
                    html.Div(item.name,
                             style={'font-size':25, 'padding-left':10}
                             )
                ],
                style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
            ),
            'value': item.name,
        }
        radio_items.append(radio_item)
    return mapper_places[place_from], radio_items

