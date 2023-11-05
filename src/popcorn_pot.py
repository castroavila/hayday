#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : popcorn_pot.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .crops import corn, sesame, chili_pepper, cacao
from .dairy import butter
from .animals import peanuts
from .honey_extractor import honey

popcorn = hayday(
    name='popcorn',
    production_place='popcorn pot',
    level=8,
    production_time=td(minutes=30),
    price_sell=32,
    img='/assets/items/Popcorn.png',
)
popcorn.add_component(corn, 2)
list_items.append(popcorn)

buttered_popcorn = hayday(
    name='buttered popcorn',
    production_place='popcorn pot',
    level=16,
    production_time=td(minutes=60),
    price_sell=126,
    img='/assets/items/Buttered_Popcorn.png',
)
buttered_popcorn.add_component(corn, 2)
buttered_popcorn.add_component(butter, 1)
list_items.append(buttered_popcorn)

chili_popcorn = hayday(
    name='chili popcorn',
    production_place='popcorn pot',
    level=25,
    production_time=td(hours=2),
    price_sell=122,
    img='/assets/items/Chili_Popcorn.png',
)
chili_popcorn.add_component(corn, 2)
chili_popcorn.add_component(chili_pepper, 2)
list_items.append(chili_popcorn)

honey_popcorn = hayday(
    name='honey popcorn',
    production_place='popcorn pot',
    level=40,
    production_time=td(hours=1, minutes=30),
    price_sell=360,
    img='/assets/items/Honey_Popcorn.png',
)
honey_popcorn.add_component(corn, 2)
honey_popcorn.add_component(honey, 2)
list_items.append(honey_popcorn)

chocolate_popcorn = hayday(
    name='chocolate popcorn',
    production_place='popcorn pot',
    level=44,
    production_time=td(hours=2, minutes=30),
    price_sell=248,
    img='/assets/items/Chocolate_Popcorn.png',
)
chocolate_popcorn.add_component(corn, 2)
chocolate_popcorn.add_component(cacao, 2)
list_items.append(chocolate_popcorn)

snack_mix = hayday(
    name='snack mix',
    production_place='popcorn pot',
    level=64,
    production_time=td(minutes=45),
    price_sell=309,
    img='/assets/items/Snack_Mix.png',
)
snack_mix.add_component(corn, 2)
snack_mix.add_component(sesame, 1)
snack_mix.add_component(peanuts, 1)
list_items.append(snack_mix)
