#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : yogurt_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .dairy import cream, milk
from .jam_maker import strawberry_jam
from .crops import raspberry, passion_fruit, mango


plain_yogurt = hayday(
    name='plain yogurt',
    production_place='yogurt maker',
    level=103,
    production_time=td(hours=2),
    price_sell=234,
    img='/assets/items/Plain_Yogurt.png',
)
plain_yogurt.add_component(cream, 2)
plain_yogurt.add_component(milk, 3)
list_items.append(plain_yogurt)

strawberry_yogurt = hayday(
    name='strawbery yogurt',
    production_place='yogurt maker',
    level=105,
    production_time=td(minutes=40),
    price_sell=529,
    img='/assets/items/Strawberry_Yogurt.png',
)
strawberry_yogurt.add_component(plain_yogurt, 1)
strawberry_yogurt.add_component(strawberry_jam, 1)
list_items.append(strawberry_yogurt)

tropical_yogurt = hayday(
    name='tropical yogurt',
    production_place='yogurt maker',
    level=109,
    production_time=td(hours=1),
    price_sell=457,
    img='/assets/items/Tropical_Yogurt.png',
)
tropical_yogurt.add_component(plain_yogurt, 1)
tropical_yogurt.add_component(raspberry, 4)
tropical_yogurt.add_component(passion_fruit, 1)
tropical_yogurt.add_component(mango, 2)
list_items.append(tropical_yogurt)
