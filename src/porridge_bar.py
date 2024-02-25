#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : porridge_bar.py
# @created          : 05-Nov-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import oats, apple, peach, pomegranate, mint, coconut
from .jam_maker import apple_jam
from .honey_extractor import honey

apple_porridge = hayday(
    name='apple porridge',
    production_place='porridge bar',
    level=119,
    production_time=td(minutes=20),
    price_sell=522,
    img='/assets/items/Apple_Porridge.png',
)
apple_porridge.add_component(apple, 1)
apple_porridge.add_component(apple_jam, 2)
apple_porridge.add_component(oats, 4)
list_items.append(apple_porridge)

sweet_porridge = hayday(
    name='sweet porridge',
    production_place='porridge bar',
    level=120,
    production_time=td(minutes=45),
    price_sell=466,
    img='/assets/items/Sweet_Porridge.png',
)
sweet_porridge.add_component(peach, 1)
sweet_porridge.add_component(honey, 2)
sweet_porridge.add_component(oats, 3)
list_items.append(sweet_porridge)

fresh_porridge = hayday(
    name='fresh porridge',
    production_place='porridge bar',
    level=122,
    production_time=td(minutes=35),
    price_sell=435,
    img='/assets/items/Fresh_Porridge.png',
)
fresh_porridge.add_component(pomegranate, 1)
fresh_porridge.add_component(mint, 2)
fresh_porridge.add_component(coconut, 2)
fresh_porridge.add_component(oats, 3)
list_items.append(fresh_porridge)
