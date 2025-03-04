#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : sewing_machine.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .loom import cotton_fabric
from .animals import wool
from .crops import raspberry, indigo, pumpkin, wheat, chamomile
from .duck_salon import duck_feather


cotton_shirt = hayday(
    name='cotton shirt',
    production_place='sewing machine',
    level=19,
    production_time=td(minutes=45),
    price_sell=241,
    img='/assets/items/Cotton_Shirt.png',
)
cotton_shirt.add_component(cotton_fabric, 2)
list_items.append(cotton_shirt)

wooly_chaps = hayday(
    name='wooly chaps',
    production_place='sewing machine',
    level=21,
    production_time=td(hours=1, minutes=30),
    price_sell=309,
    img='/assets/items/Wooly_Chaps.png',
)
wooly_chaps.add_component(cotton_fabric, 1)
wooly_chaps.add_component(wool, 3)
list_items.append(wooly_chaps)

violet_dress = hayday(
    name='violet dress',
    production_place='sewing machine',
    level=25,
    production_time=td(hours=2, minutes=15),
    price_sell=327,
    img='/assets/items/Violet_Dress.png',
)
violet_dress.add_component(cotton_fabric, 2)
violet_dress.add_component(raspberry, 1)
violet_dress.add_component(indigo, 1)
list_items.append(violet_dress)

pillow = hayday(
    name='pillow',
    production_place='sewing machine',
    level=51,
    production_time=td(hours=3),
    price_sell=676,
    img='/assets/items/Pillow.png',
)
pillow.add_component(cotton_fabric, 2)
pillow.add_component(duck_feather, 3)
list_items.append(pillow)


blanket = hayday(
    name='blanket',
    production_place='sewing machine',
    level=59,
    production_time=td(hours=3, minutes=30),
    price_sell=1098,
    img='/assets/items/Blanket.png',
)
blanket.add_component(cotton_fabric, 3)
blanket.add_component(duck_feather, 5)
blanket.add_component(pumpkin, 1)
list_items.append(blanket)

soothing_pad = hayday(
    name='soothing pad',
    production_place='sewing machine',
    level=45,
    production_time=td(hours=1),
    price_sell=324,
    img='/assets/items/Soothing_Pad.png',
)
soothing_pad.add_component(cotton_fabric, 2)
soothing_pad.add_component(wheat, 5)
soothing_pad.add_component(chamomile, 5)
list_items.append(soothing_pad)
