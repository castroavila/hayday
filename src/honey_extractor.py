#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : honey_extractor.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .animals import honeycomb

honey = hayday(
    name='honey',
    production_place='honey extractor',
    level=39,
    production_time=td(minutes=20),
    price_sell=154,
    img='/assets/items/Honey.png',
)
honey.add_component(honeycomb, 2)
list_items.append(honey)

beeswax = hayday(
    name='beeswax',
    production_place='honey extractor',
    level=48,
    production_time=td(minutes=45),
    price_sell=234,
    img='/assets/items/Beeswax.png',
)
beeswax.add_component(honeycomb, 3)
list_items.append(beeswax)
