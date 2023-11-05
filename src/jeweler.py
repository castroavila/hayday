#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : jeweler.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .smelter import silver_bar, gold_bar, platinum_bar, iron_bar, refined_coal
from .crops import peony

bracelet = hayday(
    name='bracelet',
    production_place='jeweler',
    level=38,
    production_time=td(hours=2),
    price_sell=514,
    img='/assets/items/Bracelet.png',
)
bracelet.add_component(silver_bar, 2)
bracelet.add_component(gold_bar, 1)
list_items.append(bracelet)

necklace = hayday(
    name='necklace',
    production_place='jeweler',
    level=39,
    production_time=td(hours=3),
    price_sell=727,
    img='/assets/items/Necklace.png',
)
necklace.add_component(silver_bar, 2)
necklace.add_component(gold_bar, 1)
necklace.add_component(platinum_bar, 1)
list_items.append(necklace)

diamond_ring = hayday(
    name='diamond ring',
    production_place='jeweler',
    level=40,
    production_time=td(hours=4),
    price_sell=824,
    img='/assets/items/Diamond_Ring.png',
)
diamond_ring.add_component(platinum_bar, 2)
diamond_ring.add_component(gold_bar, 2)
# Diamond missing - no definition
list_items.append(diamond_ring)

iron_bracelet = hayday(
    name='iron bracelet',
    production_place='jeweler',
    level=41,
    production_time=td(hours=1, minutes=30),
    price_sell=658,
    img='/assets/items/Iron_Bracelet.png',
)
iron_bracelet.add_component(silver_bar, 1)
iron_bracelet.add_component(refined_coal, 2)
iron_bracelet.add_component(iron_bar, 2)
list_items.append(iron_bracelet)

flower_pendant = hayday(
    name='flower pendant',
    production_place='jeweler',
    level=98,
    production_time=td(hours=1),
    price_sell=698,
    img='/assets/items/Flower_Pendant.png',
)
flower_pendant.add_component(peony, 3)
flower_pendant.add_component(platinum_bar, 1)
flower_pendant.add_component(gold_bar, 2)
list_items.append(flower_pendant)
