#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : smelter.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .mine import silver_ore, platinum_ore, coal, iron_ore, gold_ore

silver_bar = hayday(
    name='silver bar',
    production_place='smelter',
    level=24,
    production_time=td(hours=8),
    price_sell=147,
    img='/assets/items/Silver_Bar.png',
)
silver_bar.add_component(silver_ore, 3)
list_items.append(silver_bar)

gold_bar = hayday(
    name='gold bar',
    production_place='smelter',
    level=25,
    production_time=td(hours=12),
    price_sell=180,
    img='/assets/items/Gold_Bar.png',
)
gold_bar.add_component(gold_ore, 3)
list_items.append(gold_bar)

platinum_bar = hayday(
    name='platinum  bar',
    production_place='smelter',
    level=25,
    production_time=td(hours=16),
    price_sell=205,
    img='/assets/items/Platinum_Bar.png',
)
platinum_bar.add_component(platinum_ore, 3)
list_items.append(platinum_bar)

refined_coal = hayday(
    name='refined coal',
    production_place='smelter',
    level=33,
    production_time=td(hours=6),
    price_sell=108,
    img='/assets/items/Refined_Coal.png',
)
refined_coal.add_component(coal, 3)
list_items.append(refined_coal)

iron_bar = hayday(
    name='iron bar',
    production_place='smelter',
    level=34,
    production_time=td(hours=7),
    price_sell=129,
    img='/assets/items/Iron_Bar.png',
)
iron_bar.add_component(iron_ore, 3)
list_items.append(iron_bar)
