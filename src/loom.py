#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : loom.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .animals import wool
from .crops import cotton, indigo, strawberry, blackberry, sunflower

sweater = hayday(
    name='sweater',
    production_place='loom',
    level=17,
    production_time=td(hours=2),
    price_sell=151,
    img='/assets/items/Sweater.png',
)
sweater.add_component(wool, 2)
list_items.append(sweater)

cotton_fabric = hayday(
    name='cotton fabric',
    production_place='loom',
    level=18,
    production_time=td(minutes=30),
    price_sell=108,
    img='/assets/items/Cotton_Fabric.png',
)
cotton_fabric.add_component(cotton, 3)
list_items.append(cotton_fabric)

blue_woolly_hat = hayday(
    name='blue woolly hat',
    production_place='loom',
    level=19,
    production_time=td(hours=1),
    price_sell=111,
    img='/assets/items/Blue_Woolly_Hat.png',
)
blue_woolly_hat.add_component(wool, 1)
blue_woolly_hat.add_component(indigo, 1)
list_items.append(blue_woolly_hat)

blue_sweater = hayday(
    name='blue sweater',
    production_place='loom',
    level=20,
    production_time=td(hours=3),
    price_sell=208,
    img='/assets/items/Blue_Sweater.png',
)
blue_sweater.add_component(wool, 2)
blue_sweater.add_component(indigo, 2)
list_items.append(blue_sweater)

red_scarf = hayday(
    name='red scarf',
    production_place='loom',
    level=48,
    production_time=td(hours=2, minutes=30),
    price_sell=288,
    img='/assets/items/Red_Scarf.png',
)
red_scarf.add_component(wool, 2)
red_scarf.add_component(strawberry, 2)
list_items.append(red_scarf)

flower_shawl = hayday(
    name='flower shawl',
    production_place='loom',
    level=71,
    production_time=td(hours=1, minutes=30),
    price_sell=295,
    img='/assets/items/Flower_Shawl.png',
)
flower_shawl.add_component(wool, 2)
flower_shawl.add_component(blackberry, 1)
flower_shawl.add_component(sunflower, 3)
list_items.append(flower_shawl)
