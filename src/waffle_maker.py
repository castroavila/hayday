#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : waffle_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .sugar_mill import white_sugar, syrup
from .animals import egg, bacon
from .crops import (
    wheat,
    raspberry,
    blackberry,
    cacao,
    strawberry,
    banana,
    asparagus,
)

plain_waffles = hayday(
    name='plain waffles',
    production_place='waffle maker',
    level=114,
    production_time=td(minutes=25),
    price_sell=198,
    img='/assets/items/Plain_Waffles.png',
)
plain_waffles.add_component(white_sugar, 2)
plain_waffles.add_component(egg, 3)
plain_waffles.add_component(wheat, 5)
list_items.append(plain_waffles)

berry_waffles = hayday(
    name='berry waffles',
    production_place='waffle maker',
    level=114,
    production_time=td(minutes=35),
    price_sell=604,
    img='/assets/items/Berry_Waffles.png',
)
berry_waffles.add_component(plain_waffles, 1)
berry_waffles.add_component(syrup, 1)
berry_waffles.add_component(raspberry, 3)
berry_waffles.add_component(blackberry, 2)
list_items.append(berry_waffles)

chocolate_waffles = hayday(
    name='chocolate waffles',
    production_place='waffle maker',
    level=117,
    production_time=td(minutes=40),
    price_sell=637,
    img='/assets/items/Chocolate_Waffles.png',
)
chocolate_waffles.add_component(plain_waffles, 1)
chocolate_waffles.add_component(cacao, 2)
chocolate_waffles.add_component(strawberry, 3)
chocolate_waffles.add_component(banana, 1)
list_items.append(chocolate_waffles)

breakfast_waffles = hayday(
    name='breakfast waffles',
    production_place='waffle maker',
    level=119,
    production_time=td(minutes=45),
    price_sell=424,
    img='/assets/items/Breakfast_Waffles.png',
)
breakfast_waffles.add_component(plain_waffles, 1)
breakfast_waffles.add_component(bacon, 2)
breakfast_waffles.add_component(egg, 1)
breakfast_waffles.add_component(asparagus, 2)
list_items.append(breakfast_waffles)
