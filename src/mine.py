#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : mine.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items

silver_ore = hayday(
    name='silver ore',
    production_place='mine',
    level=24,
    production_time=td(minutes=1),
    price_sell=18,
    img='/assets/items/Silver_Ore.png',
)
list_items.append(silver_ore)

gold_ore = hayday(
    name='gold ore',
    production_place='mine',
    level=24,
    production_time=td(minutes=1),
    price_sell=21,
    img='/assets/items/Gold_Ore.png',
)
list_items.append(gold_ore)

platinum_ore = hayday(
    name='platinum ore',
    production_place='mine',
    level=25,
    production_time=td(minutes=1),
    price_sell=32,
    img='/assets/items/Platinum_Ore.png',
)
list_items.append(platinum_ore)

coal = hayday(
    name='coal',
    production_place='mine',
    level=33,
    production_time=td(minutes=1),
    price_sell=10,
    img='/assets/items/Coal.png',
)
list_items.append(coal)

iron_ore = hayday(
    name='iron ore',
    production_place='mine',
    level=34,
    production_time=td(minutes=1),
    price_sell=14,
    img='/assets/items/Iron_Ore.png',
)
list_items.append(iron_ore)

