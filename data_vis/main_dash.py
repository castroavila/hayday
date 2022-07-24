#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file             : main_dash.py
# @created          : 23-Jul-2022
# @company          : Home
#

"""

"""
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
# import dash_core_components as dcc
# import dash_html_components as html
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State
import random
import sys
app = dash.Dash(__name__, assets_folder='../assets/')
