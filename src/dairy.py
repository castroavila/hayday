#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : dairy.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .animals import milk, goat_milk
from .hayday import hayday

cream = hayday(
    name='cream',
    production_place='dairy',
    level=6,
    production_time=td(minutes=20),
    price_sell=50,
    img='/assets/items/Cream.png',
)
cream.add_component(milk, 1)
list_items.append(cream)

butter = hayday(
    name='butter',
    production_place='dairy',
    level=9,
    production_time=td(minutes=30),
    price_sell=82,
    img='/assets/items/Butter.png',
)
butter.add_component(milk, 2)
list_items.append(butter)

cheese = hayday(
    name='cheese',
    production_place='dairy',
    level=12,
    production_time=td(hours=1),
    price_sell=122,
    img='/assets/items/Cheese.png',
)
cheese.add_component(milk, 3)
list_items.append(cheese)

goat_cheese = hayday(
    name='goat cheese',
    production_place='dairy',
    level=33,
    production_time=td(hours=1, minutes=30),
    price_sell=162,
    img='/assets/items/Goat_Cheese.png',
)
goat_cheese.add_component(goat_milk, 2)
list_items.append(goat_cheese)
