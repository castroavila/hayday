#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : fondue_pot.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    strawberry,
    broccoli,
    bell_pepper,
    mushroom,
    tomato,
    pineapple,
    mango,
)
from .candine_machine import chocolate
from .animals import bacon
from .sauce_maker import olive_oil
from .bakery import potato_bread
from .dairy import cheese, cream
from .sugar_mill import white_sugar

chocolate_fondue = hayday(
    name='chocolate fondue',
    production_place='fondue pot',
    level=81,
    production_time=td(minutes=25),
    price_sell=626,
    img='/assets/items/Chocolate_Fondue.png',
)
chocolate_fondue.add_component(chocolate, 1)
chocolate_fondue.add_component(strawberry, 3)
list_items.append(chocolate_fondue)

bacon_fondue = hayday(
    name='bacon fondue',
    production_place='fondue pot',
    level=86,
    production_time=td(minutes=30),
    price_sell=507,
    img='/assets/items/Bacon_Fondue.png',
)
bacon_fondue.add_component(bacon, 3)
bacon_fondue.add_component(broccoli, 1)
bacon_fondue.add_component(bell_pepper, 1)
bacon_fondue.add_component(olive_oil, 1)
list_items.append(bacon_fondue)

cheese_fondue = hayday(
    name='cheese fondue',
    production_place='fondue pot',
    level=91,
    production_time=td(minutes=20),
    price_sell=493,
    img='/assets/items/Cheese_Fondue.png',
)
cheese_fondue.add_component(potato_bread, 1)
cheese_fondue.add_component(cheese, 1)
cheese_fondue.add_component(mushroom, 2)
cheese_fondue.add_component(tomato, 1)
list_items.append(cheese_fondue)

tropical_fondue = hayday(
    name='tropical fondue',
    production_place='fondue pot',
    level=100,
    production_time=td(minutes=35),
    price_sell=417,
    img='/assets/items/Tropical_Fondue.png',
)
tropical_fondue.add_component(white_sugar, 1)
tropical_fondue.add_component(cream, 2)
tropical_fondue.add_component(pineapple, 3)
tropical_fondue.add_component(mango, 2)
list_items.append(tropical_fondue)
