#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : preservation_station.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    cucumber,
    onion,
    lemon,
    chili_pepper,
    cabbage,
    ginger,
    garlic,
    grapes,
    raspberry,
    strawberry,
    orange,
    guava,
    lemon,
)
from .fish import fish_fillet
from .sauce_maker import olive_oil
from .sugar_mill import white_sugar


pickles = hayday(
    name='pickles',
    production_place='preservation station',
    level=91,
    production_time=td(hours=4),
    price_sell=270,
    img='/assets/items/Pickles.png',
)
pickles.add_component(cucumber, 3)
pickles.add_component(onion, 2)
pickles.add_component(lemon, 1)
list_items.append(pickles)

canned_fish = hayday(
    name='canned fish',
    production_place='preservation station',
    level=95,
    production_time=td(hours=3, minutes=40),
    price_sell=471,
    img='/assets/items/Canned_Fish.png',
)
canned_fish.add_component(fish_fillet, 2)
canned_fish.add_component(chili_pepper, 1)
canned_fish.add_component(olive_oil, 1)
list_items.append(canned_fish)

kimchi = hayday(
    name='kimchi',
    production_place='preservation station',
    level=98,
    production_time=td(hours=5),
    price_sell=219,
    img='/assets/items/Kimchi.png',
)
kimchi.add_component(cabbage, 5)
kimchi.add_component(ginger, 1)
kimchi.add_component(chili_pepper, 1)
kimchi.add_component(garlic, 1)
list_items.append(kimchi)

dried_fruit = hayday(
    name='dried fruit',
    production_place='preservation station',
    level=102,
    production_time=td(hours=3),
    price_sell=266,
    img='/assets/items/Dried_Fruit.png',
)
dried_fruit.add_component(grapes, 1)
dried_fruit.add_component(raspberry, 1)
dried_fruit.add_component(strawberry, 1)
dried_fruit.add_component(orange, 1)
list_items.append(dried_fruit)

guava_compote = hayday(
    name='guava compote',
    production_place='preservation station',
    level=104,
    production_time=td(hours=4, minutes=20),
    price_sell=421,
    img='/assets/items/Guava_Compote.png',
)
guava_compote.add_component(guava, 2)
guava_compote.add_component(lemon, 1)
guava_compote.add_component(white_sugar, 1)
list_items.append(guava_compote)
