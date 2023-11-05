#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : sugar_mill.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .crops import sugarcane

brown_sugar = hayday(
    name='brown sugar',
    production_place='sugar mill',
    level=7,
    production_time=td(minutes=20),
    price_sell=32,
    img='/assets/items/Brown_Sugar.png',
)
brown_sugar.add_component(sugarcane, 1)
list_items.append(brown_sugar)

white_sugar = hayday(
    name='white sugar',
    production_place='sugar mill',
    level=13,
    production_time=td(minutes=40),
    price_sell=50,
    img='/assets/items/White_Sugar.png',
)
white_sugar.add_component(sugarcane, 2)
list_items.append(white_sugar)

syrup = hayday(
    name='syrup',
    production_place='sugar mill',
    level=18,
    production_time=td(hours=1, minutes=30),
    price_sell=90,
    img='/assets/items/Syrup.png',
)
syrup.add_component(sugarcane, 4)
list_items.append(syrup)
