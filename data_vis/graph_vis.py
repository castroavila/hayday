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
from build_graph import *


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
                           'height': '200px', 'border':'2px black solid',
                           'margin-left': '20px'}

                ),
                html.Div(
                    [
                        cyto.Cytoscape(
                            id='graph',
                            layout={'name': 'preset'},
                            style={'width': '100%', 'height': '400px'},
                            stylesheet=[
                                {
                                    'selector': 'node',
                                    'style': {
                                        'content': 'data(label)',
                                        'width': '100px',
                                        'height': '100px',
                                        # 'background-image-opacity': 0.,
                                        'background-color': 'white',
                                        'background-fit': 'cover',
                                        'background-image': 'data(url)',
                                        # 'background-width': '20%'
                                    }
                                },
                                {
                                    'selector': 'edge',
                                    'style': {
                                        'curve-style': 'bezier',
                                        'control-point-step-size': 100,
                                        'control-point-weight': 0.5,
                                        'line-color': 'blue',
                                        'target-arrow-color': 'blue',
                                        'target-arrow-shape': 'triangle',
                                        'width': 1
                                    }
                                },
                            ],
                        )
                    ],
                    style={'border':'2px black solid', 'width': '40%',
                           'heigth': '400px', 'margin-left': '10px'}
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
def update_option_list(place_from):
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

@app.callback(
    Output('graph', 'elements'),
    Input('items_in_place', 'value'),
    prevent_initial_call=True
)
def update_graph(item):

    graph, positions  = get_ancestor_nodes_and_position(item)
    elements = []

    for label, pos in positions.items():
        item = get_object(label)
        img = item.img
        element = {
            # 'classes': 'terminal',
            'data': {'id': label,
                     'label': label,
                     'url': img
                     },
            'position': {'x': 2.*pos[0], 'y': -2.*pos[1]},
        }
        elements.append(element)

    # Edges
    for edge in list(graph.edges()):
        element = {
            'data': {'source': edge[0], 'target': edge[1]}
        }
        elements.append(element)

    return elements

