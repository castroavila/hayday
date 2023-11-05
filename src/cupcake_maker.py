#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : cupcake_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .dairy import milk, cream
from .animals import egg
from .sugar_mill import white_sugar
from .crops import wheat, guava, pineapple, coconut, cacao
from .bakery import cookie


plain_cupcake = hayday(
    name='plain cupcake',
    production_place='cupcake maker',
    level=109,
    production_time=td(minutes=40),
    price_sell=280,
    img='/assets/items/Plain_Cupcake.png',
)
plain_cupcake.add_component(milk, 2)
plain_cupcake.add_component(white_sugar, 3)
plain_cupcake.add_component(egg, 1)
plain_cupcake.add_component(wheat, 5)
list_items.append(plain_cupcake)

guava_cupcake = hayday(
    name='guava cupcake',
    production_place='cupcake maker',
    level=109,
    production_time=td(hours=1, minutes=10),
    price_sell=583,
    img='/assets/items/Guava_Cupcake.png',
)
guava_cupcake.add_component(plain_cupcake, 1)
guava_cupcake.add_component(guava, 2)
guava_cupcake.add_component(cream, 1)
list_items.append(guava_cupcake)

tropical_cupcake = hayday(
    name='tropical cupcake',
    production_place='cupcake maker',
    level=112,
    production_time=td(hours=1, minutes=30),
    price_sell=572,
    img='/assets/items/Tropical_Cupcake.png',
)
tropical_cupcake.add_component(plain_cupcake, 1)
tropical_cupcake.add_component(pineapple, 3)
tropical_cupcake.add_component(coconut, 2)
list_items.append(tropical_cupcake)

cookie_cupcake = hayday(
    name='cookie cupcake',
    production_place='cupcake maker',
    level=114,
    production_time=td(hours=2),
    price_sell=712,
    img='/assets/items/Cookie_Cupcake.png',
)
cookie_cupcake.add_component(plain_cupcake, 1)
cookie_cupcake.add_component(cream, 2)
cookie_cupcake.add_component(cookie, 2)
cookie_cupcake.add_component(cacao, 1)
list_items.append(cookie_cupcake)
