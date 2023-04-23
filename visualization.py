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
# import dash_core_components as dcc
# import dash_html_components as html
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State
import random
import sys


# from dash import dcc
# from dash import html
# import dash_bootstrap_components as dbc
# from data_vis.main_dash import *
# from data_vis.pricing import *
from data_vis.graph_vis import tab_graph
from data_vis.main_dash import app

#Columns
#['production_time', 'profit', 'item_name', 'price_sell', 'profit_per_hour',
# 'prod_cost', 'place']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = tab_graph


app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
