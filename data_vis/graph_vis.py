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
                html.Img(
                    src='/assets/logo/Banner.png', style={'height': '200px'}
                )
            ],
            style={'textAlign': 'center'},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label('place:', style={'width': '6%'}),
                                dcc.Dropdown(
                                    id='place_from',
                                    options=[
                                        {'label': i, 'value': i}
                                        for i in df['place'].unique()
                                    ],
                                    value='bakery',
                                    multi=False,
                                    style={
                                        'width': '200px',
                                        'align-items': 'left',
                                        'margin-left': '30px',
                                    },
                                ),
                            ],
                            style={
                                'display': 'flex',
                                'width': '100%',
                                'align-items': 'center',
                            },
                        ),
                        html.Br(),
                        html.Div(
                            [
                                dcc.RadioItems(
                                    id='items_in_place',
                                    options=[],
                                    value='',
                                    labelStyle={'display': 'flex'},
                                    style={'height': '20%'},
                                )
                            ],
                            style={
                                'maxHeight': '400px',
                                'overflow': 'scroll',
                                'height': '300px',
                                'border': '2px black solid',
                                'margin-left': '0px',
                                'background-color': 'white',
                                'width': '350px',
                            },
                        ),
                        html.Br(),
                        html.Img(
                            id='image_place', src='', style={'width': '350px'}
                        ),
                    ],
                    style={'height': '600px'},
                ),
                html.Div(
                    [
                        cyto.Cytoscape(
                            id='graph',
                            layout={'name': 'preset', 'animate': True},
                            style={
                                'width': '100%',
                                'height': '600px',
                                'background-color': 'white',
                            },
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
                                    },
                                },
                                {
                                    'selector': 'edge',
                                    'style': {
                                        'label': 'data(label)',
                                        'color': 'green',
                                        'font-style': 'italic',
                                        'font-family': 'cursive',
                                        'font-size': 30,
                                        'curve-style': 'bezier',
                                        'control-point-step-size': 100,
                                        'control-point-weight': 0.5,
                                        'line-color': 'blue',
                                        'target-arrow-color': 'blue',
                                        'target-arrow-shape': 'triangle',
                                        'width': 1,
                                    },
                                },
                            ],
                            minZoom=0.6,
                            zoom=1,
                            # userPanningEnabled=False,
                            autolock=True,
                            zoomingEnabled=True,
                            userZoomingEnabled=False,
                        ),
                        html.Div(
                            [
                                html.Label(
                                    'zoom', style={'margin-left': '5px'}
                                ),
                                dcc.Slider(
                                    id='slider_zoom',
                                    min=1,
                                    max=2,
                                    step=0.1,
                                    value=1.0,
                                ),
                            ]
                        ),
                    ],
                    style={
                        'border': '2px black solid',
                        'width': '40%',
                        'heigth': '600px',
                        'margin-left': '10px',
                    },
                ),
                dcc.Graph(
                    id='price',
                    style={
                        'border': '2px black solid',
                        'margin-left': '10px',
                        'height': '600px',
                        'width': '40%',
                    },
                ),
            ],
            style={
                'widht': '20%',
                'display': 'flex',
                'align-items': 'center',
                'height': '10%',
            },
        ),
    ]
)


@app.callback(
    [Output('image_place', 'src'), Output('items_in_place', 'options')],
    Input('place_from', 'value'),
)
def update_option_list(place_from):
    items = list_products_at(place_from)
    options = {item.name: item.name for item in items}
    radio_items = []
    for item in items:
        radio_item = {
            'label': html.Div(
                [
                    html.Img(
                        src=item.img, height=50, style={'padding-left': 10}
                    ),
                    html.Div(
                        item.name,
                        style={
                            'font-size': 25,
                            'padding-left': 10,
                            'color': 'black',
                        },
                    ),
                ],
                style={
                    'display': 'flex',
                    'align-items': 'center',
                    'justify-content': 'center',
                },
            ),
            'value': item.name,
        }
        radio_items.append(radio_item)
    return mapper_places[place_from], radio_items


@app.callback(
    Output('graph', 'elements'),
    Input('items_in_place', 'value'),
    prevent_initial_call=True,
)
def update_graph(item):
    graph, positions = get_ancestor_nodes_and_position(item)
    elements = []

    for label, pos in positions.items():
        item = get_object(label)
        img = item.img
        element = {
            # 'classes': 'terminal',
            'data': {'id': label, 'label': label, 'url': img},
            'position': {'x': 2.0 * pos[0], 'y': -2.0 * pos[1]},
        }
        elements.append(element)

    # Edges
    for edge in list(graph.edges()):
        element = {
            'data': {
                'source': edge[0],
                'target': edge[1],
                'label': f'{get_quantity(edge[0], edge[1])}',
            }
        }
        elements.append(element)

    return elements


@app.callback(
    Output('graph', 'zoom'),
    Input('slider_zoom', 'value'),
    prevent_initial_call=True,
)
def update_zoom_graph(value):
    return value


@app.callback(Output('price', 'figure'), Input('place_from', 'value'))
def update_price_per_place(place):
    items_at_place = list_products_at(place)
    items_and_price = {}
    items_and_production_cost = {}
    for item in items_at_place:
        items_and_price[item.name] = item.price_sell
        items_and_production_cost[item.name] = item.get_production_price()

    items_and_price = dict(
        sorted(items_and_price.items(), key=lambda item: item[1], reverse=True)
    )

    # sort order
    items_and_production_cost = {
        key: items_and_production_cost[key] for key in items_and_price.keys()
    }
    bar_sell_price = px.bar(
        x=list(items_and_price.keys()),
        y=list(items_and_price.values()),
        color=np.array(list(items_and_price.values()))
        - np.array(list(items_and_production_cost.values())),
        # name='Sell',
        labels={'x': 'Item', 'y': 'selling price', 'color': 'sell - cost'},
    )
    bar_sell_price.update_traces(textfont_size=60)
    bar_cost_price = go.Bar(
        x=list(items_and_production_cost.keys()),
        y=list(items_and_production_cost.values()),
        name='Cost',
    )

    return bar_sell_price
