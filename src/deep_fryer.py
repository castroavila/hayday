#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : deep_fryer.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .animals import bacon, egg, peanuts
from .crops import chili_pepper, potato, garlic, wheat, chickpea, onion, cacao
from .jam_maker import apple_jam
from .dairy import cheese
from .bakery import cookie


bacon_fries = hayday(
    name='bacon fries',
    production_place='deep fryer',
    level=87,
    production_time=td(minutes=25),
    price_sell=302,
    img='/assets/items/Bacon_Fries.png',
)
bacon_fries.add_component(chili_pepper, 1)
bacon_fries.add_component(bacon, 2)
bacon_fries.add_component(potato, 4)
bacon_fries.add_component(garlic, 1)
list_items.append(bacon_fries)

hand_pies = hayday(
    name='hand pies',
    production_place='deep fryer',
    level=91,
    production_time=td(minutes=20),
    price_sell=295,
    img='/assets/items/Hand_Pies.png',
)
hand_pies.add_component(apple_jam, 1)
hand_pies.add_component(egg, 2)
hand_pies.add_component(wheat, 5)
list_items.append(hand_pies)

chili_poppers = hayday(
    name='chili poppers',
    production_place='deep fryer',
    level=98,
    production_time=td(minutes=40),
    price_sell=406,
    img='/assets/items/Chili_Poppers.png',
)
chili_poppers.add_component(chili_pepper, 3)
chili_poppers.add_component(wheat, 1)
chili_poppers.add_component(bacon, 3)
chili_poppers.add_component(cheese, 1)
list_items.append(chili_poppers)

falafel = hayday(
    name='falafel',
    production_place='deep fryer',
    level=98,
    production_time=td(minutes=55),
    price_sell=226,
    img='/assets/items/Falafel.png',
)
falafel.add_component(chickpea, 3)
falafel.add_component(onion, 2)
falafel.add_component(garlic, 2)
falafel.add_component(chili_pepper, 1)
list_items.append(falafel)

fried_candy_bar = hayday(
    name='fried candy bar',
    production_place='deep fryer',
    level=100,
    production_time=td(minutes=15),
    price_sell=658,
    img='/assets/items/Fried_Candy_Bar.png',
)
fried_candy_bar.add_component(cacao, 3)
fried_candy_bar.add_component(cookie, 1)
fried_candy_bar.add_component(peanuts, 1)
list_items.append(fried_candy_bar)

samosa = hayday(
    name='samosa',
    production_place='deep fryer',
    level=103,
    production_time=td(hours=1, minutes=15),
    price_sell=223,
    img='/assets/items/Samosa.png',
)
samosa.add_component(chickpea, 2)
samosa.add_component(wheat, 4)
samosa.add_component(potato, 3)
samosa.add_component(chili_pepper, 1)
list_items.append(samosa)
