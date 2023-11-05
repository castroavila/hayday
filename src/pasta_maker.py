#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : pasta_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import wheat, rice
from .animals import egg

fresh_pasta = hayday(
    name='fresh pasta',
    production_place='pasta maker',
    level=67,
    production_time=td(minutes=15),
    price_sell=43,
    img='/assets/items/Fresh_Pasta.png',
)
fresh_pasta.add_component(wheat, 2)
fresh_pasta.add_component(egg, 1)
list_items.append(fresh_pasta)

rice_noodles = hayday(
    name='rice noddles',
    production_place='pasta maker',
    level=73,
    production_time=td(minutes=20),
    price_sell=100,
    img='/assets/items/Rice_Noodles.png',
)
rice_noodles.add_component(rice, 5)
list_items.append(rice_noodles)
