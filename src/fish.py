#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : fish.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from .main import list_items
from .hayday import hayday
from datetime import timedelta as td

fish_fillet = hayday(
    name='fish fillet',
    production_place='fishing lake',
    level=27,
    production_time=td(hours=7),
    price_sell=54,
    img='/assets/items/Fish_Fillet.png',
)
list_items.append(fish_fillet)

lobster_tail = hayday(
    name='lobster tail',
    production_place='fishing lake',
    level=44,
    production_time=td(hours=6),
    price_sell=201,
    img='/assets/items/Lobster_Tail.png',
)
list_items.append(lobster_tail)

duck = hayday(
    name='duck',
    production_place='fishing lake',
    level=50,
    production_time=td(hours=2),
    price_sell=1,
    img='/assets/animals/Duck.png',
)
list_items.append(duck)
