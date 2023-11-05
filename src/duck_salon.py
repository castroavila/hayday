#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : duck_salon.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from .main import list_items
from .hayday import hayday
from .fish import duck
from datetime import timedelta as td

duck_feather = hayday(
    name='duck feather',
    production_place='duck salon',
    level=50,
    production_time=td(hours=2),
    price_sell=140,
    img='/assets/items/Duck_Feather.png',
)
duck_feather.add_component(duck, 1)
list_items.append(duck_feather)
