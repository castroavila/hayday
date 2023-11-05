#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : hot_dog_stand.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .animals import bacon
from .bakery import bread
from .sauce_maker import tomato_sauce, olive_oil
from .crops import lettuce, soybean, tomato, corn, chili_pepper, onion

hot_dog = hayday(
    name='hot dog',
    production_place='hot dog stand',
    level=75,
    production_time=td(minutes=30),
    price_sell=370,
    img='/assets/items/Hot_Dog.png',
)
hot_dog.add_component(bacon, 2)
hot_dog.add_component(bread, 1)
hot_dog.add_component(tomato_sauce, 1)
list_items.append(hot_dog)

tofu_dog = hayday(
    name='tofu dog',
    production_place='hot dog stand',
    level=76,
    production_time=td(minutes=45),
    price_sell=367,
    img='/assets/items/Tofu_Dog.png',
)
tofu_dog.add_component(lettuce, 3)
tofu_dog.add_component(soybean, 6)
tofu_dog.add_component(tomato, 4)
list_items.append(tofu_dog)

corn_dog = hayday(
    name='corn dog',
    production_place='hot dog stand',
    level=78,
    production_time=td(hours=1),
    price_sell=529,
    img='/assets/items/Corn_Dog.png',
)
corn_dog.add_component(bacon, 4)
corn_dog.add_component(corn, 4)
corn_dog.add_component(olive_oil, 1)
list_items.append(corn_dog)

onion_dog = hayday(
    name='onion dog',
    production_place='hot dog stand',
    level=80,
    production_time=td(hours=1, minutes=15),
    price_sell=306,
    img='/assets/items/Onion_Dog.png',
)
onion_dog.add_component(bacon, 2)
onion_dog.add_component(bread, 1)
onion_dog.add_component(chili_pepper, 1)
onion_dog.add_component(onion, 3)
list_items.append(onion_dog)
