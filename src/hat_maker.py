#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : hat_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .loom import cotton_fabric
from .smelter import refined_coal
from .duck_salon import duck_feather
from .animals import wool
from .crops import indigo, raspberry, peony, cotton, strawberry


cloche_hat = hayday(
    name='cloche hat',
    production_place='hat maker',
    level=70,
    production_time=td(hours=2),
    price_sell=468,
    img='/assets/items/Cloche_Hat.png',
)
cloche_hat.add_component(strawberry, 2)
cloche_hat.add_component(wool, 6)
list_items.append(cloche_hat)

top_hat = hayday(
    name='top hat',
    production_place='hat maker',
    level=72,
    production_time=td(hours=3, minutes=30),
    price_sell=619,
    img='/assets/items/Top_Hat.png',
)
top_hat.add_component(cotton_fabric, 3)
top_hat.add_component(refined_coal, 1)
top_hat.add_component(duck_feather, 1)
list_items.append(top_hat)

sun_hat = hayday(
    name='sun hat',
    production_place='hat maker',
    level=74,
    production_time=td(hours=2, minutes=30),
    price_sell=558,
    img='/assets/items/Sun_Hat.png',
)
sun_hat.add_component(wool, 3)
sun_hat.add_component(indigo, 1)
sun_hat.add_component(duck_feather, 2)
sun_hat.add_component(raspberry, 1)
list_items.append(sun_hat)

flower_crown = hayday(
    name='flower crown',
    production_place='hat maker',
    level=86,
    production_time=td(hours=2),
    price_sell=331,
    img='/assets/items/Flower_Crown.png',
)
flower_crown.add_component(peony, 5)
flower_crown.add_component(cotton, 4)
list_items.append(flower_crown)
