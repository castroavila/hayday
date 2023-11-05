#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : stew_pot.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    coconut,
    tomato,
    chickpea,
    chili_pepper,
    onion,
    potato,
    mushroom,
)
from .animals import bacon
from .dairy import cream

chickpea_stew = hayday(
    name='chickpea stew',
    production_place='stew pot',
    level=106,
    production_time=td(hours=1, minutes=30),
    price_sell=284,
    img='/assets/items/Chickpea_Stew.png',
)
chickpea_stew.add_component(coconut, 1)
chickpea_stew.add_component(tomato, 2)
chickpea_stew.add_component(chickpea, 3)
list_items.append(chickpea_stew)

chili_stew = hayday(
    name='chili stew',
    production_place='stew pot',
    level=109,
    production_time=td(hours=2),
    price_sell=370,
    img='/assets/items/Chili_Stew.png',
)
chili_stew.add_component(chili_pepper, 3)
chili_stew.add_component(bacon, 2)
chili_stew.add_component(onion, 2)
chili_stew.add_component(cream, 1)
list_items.append(chili_stew)

winter_stew = hayday(
    name='winter stew',
    production_place='stew pot',
    level=112,
    production_time=td(hours=2, minutes=20),
    price_sell=295,
    img='/assets/items/Winter_Stew.png',
)
winter_stew.add_component(bacon, 1)
winter_stew.add_component(potato, 3)
winter_stew.add_component(onion, 2)
winter_stew.add_component(mushroom, 2)
list_items.append(winter_stew)
