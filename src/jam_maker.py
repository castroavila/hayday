#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : jam_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    apple,
    raspberry,
    blackberry,
    cherry,
    strawberry,
    orange,
    peach,
    grapes,
    plum,
    passion_fruit
)

apple_jam = hayday(
    name='apple jam',
    production_place='jam maker',
    level=35,
    production_time=td(hours=6),
    price_sell=219,
    img='/assets/items/Apple_Jam.png',
)
apple_jam.add_component(apple, 3)
list_items.append(apple_jam)

raspberry_jam = hayday(
    name='raspberry jam',
    production_place='jam maker',
    level=36,
    production_time=td(hours=7),
    price_sell=252,
    img='/assets/items/Raspberry_Jam.png',
)
raspberry_jam.add_component(raspberry, 3)
list_items.append(raspberry_jam)

blackberry_jam = hayday(
    name='blackberry jam',
    production_place='jam maker',
    level=37,
    production_time=td(hours=8),
    price_sell=388,
    img='/assets/items/Blackberry_Jam.png',
)
blackberry_jam.add_component(blackberry, 3)
list_items.append(blackberry_jam)

cherry_jam = hayday(
    name='cherry jam',
    production_place='jam maker',
    level=38,
    production_time=td(hours=7),
    price_sell=334,
    img='/assets/items/Cherry_Jam.png',
)
cherry_jam.add_component(cherry, 3)
list_items.append(cherry_jam)

strawberry_jam = hayday(
    name='strawberry jam',
    production_place='jam maker',
    level=50,
    production_time=td(hours=7, minutes=30),
    price_sell=270,
    img='/assets/items/Strawberry_Jam.png',
)
strawberry_jam.add_component(strawberry, 3)
list_items.append(strawberry_jam)

marmalade = hayday(
    name='marmalade',
    production_place='jam maker',
    level=74,
    production_time=td(hours=8, minutes=30),
    price_sell=457,
    img='/assets/items/Marmalade.png',
)
marmalade.add_component(orange, 3)
list_items.append(marmalade)

peach_jam = hayday(
    name='peach jam',
    production_place='jam maker',
    level=79,
    production_time=td(hours=8),
    price_sell=464,
    img='/assets/items/Peach_Jam.png',
)
peach_jam.add_component(peach, 3)
list_items.append(peach_jam)

grape_jam = hayday(
    name='grape jam',
    production_place='jam maker',
    level=85,
    production_time=td(hours=6, minutes=30),
    price_sell=162,
    img='/assets/items/Grape_Jam.png',
)
grape_jam.add_component(grapes, 3)
list_items.append(grape_jam)

plum_jam = hayday(
    name='plum jam',
    production_place='jam maker',
    level=94,
    production_time=td(hours=5),
    price_sell=385,
    img='/assets/items/Plum_Jam.png',
)
plum_jam.add_component(plum, 3)
list_items.append(plum_jam)

passion_fruit_jam = hayday(
    name='passion fruit jam',
    production_place='jam maker',
    level=96,
    production_time=td(hours=3, minutes=20),
    price_sell=118,
    img='/assets/items/Passion_Fruit_Jam.png',
)
passion_fruit_jam.add_component(passion_fruit, 3)
list_items.append(passion_fruit_jam)
