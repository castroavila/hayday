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

from data_vis.pricing import *

#Columns
#['production_time', 'profit', 'item_name', 'price_sell', 'profit_per_hour',
# 'prod_cost', 'place']

app.layout = tab_pricing

app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
