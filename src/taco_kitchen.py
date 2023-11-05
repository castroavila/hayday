#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : taco_kitchen.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .bakery import corn_bread
from .animals import bacon
from .sauce_maker import salsa
from .crops import chili_pepper, lemon, wheat, corn
from .fish import fish_fillet
from .dairy import cheese

taco = hayday(
    name='taco',
    production_place='taco kitchen',
    level=77,
    production_time=td(minutes=45),
    price_sell=396,
    img='/assets/items/Taco.png',
)
taco.add_component(corn_bread, 1)
taco.add_component(bacon, 1)
taco.add_component(salsa, 1)
list_items.append(taco)

fish_taco = hayday(
    name='fish taco',
    production_place='taco kitchen',
    level=79,
    production_time=td(hours=1, minutes=30),
    price_sell=392,
    img='/assets/items/Fish_Taco.png',
)
fish_taco.add_component(chili_pepper, 2)
fish_taco.add_component(corn_bread, 2)
fish_taco.add_component(fish_fillet, 1)
fish_taco.add_component(lemon, 1)
list_items.append(fish_taco)

quesadillas = hayday(
    name='quesadillas',
    production_place='taco kitchen',
    level=82,
    production_time=td(hours=1),
    price_sell=241,
    img='/assets/items/Quesadilla.png',
)
quesadillas.add_component(cheese, 1)
quesadillas.add_component(chili_pepper, 2)
quesadillas.add_component(wheat, 4)
list_items.append(quesadillas)

nachos = hayday(
    name='nachos',
    production_place='taco kitchen',
    level=87,
    production_time=td(hours=1, minutes=15),
    price_sell=432,
    img='/assets/items/Nachos.png',
)
nachos.add_component(cheese, 1)
nachos.add_component(corn, 4)
nachos.add_component(salsa, 1)
list_items.append(nachos)
