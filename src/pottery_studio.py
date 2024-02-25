#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : pottery_studio.py
# @created          : 05-Nov-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import clay, coffee_bean, sunflower, indigo, peony
from .mine import gold_ore

tea_pot = hayday(
    name='tea pot',
    production_place='pottery studio',
    level=94,
    production_time=td(hours=3, minutes=40),
    price_sell=219,
    img='/assets/items/Tea_Pot.png',
)
tea_pot.add_component(clay, 3)
tea_pot.add_component(coffee_bean, 1)
tea_pot.add_component(gold_ore, 1)
list_items.append(tea_pot)

potted_plant = hayday(
    name='potted plant',
    production_place='pottery studio',
    level=96,
    production_time=td(hours=3, minutes=40),
    price_sell=151,
    img='/assets/items/Potted_Plant.png',
)
potted_plant.add_component(clay, 3)
potted_plant.add_component(sunflower, 1)
list_items.append(potted_plant)
clay_mug = hayday(
    name='clay mug',
    production_place='pottery studio',
    level=99,
    production_time=td(hours=3, minutes=20),
    price_sell=212,
    img='/assets/items/Clay_Mug.png',
)
clay_mug.add_component(clay, 3)
clay_mug.add_component(indigo, 2)
clay_mug.add_component(peony, 1)
list_items.append(clay_mug)
