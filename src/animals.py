#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : animals.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .animal_food import (
    chicken_food,
    cow_food,
    goat_food,
    pig_food,
    sheep_food,
)

egg = hayday(
    name='egg',
    production_place='farm',
    level=1,
    production_time=td(minutes=20),
    price_sell=18,
    img='/assets/items/Egg.png',
)
egg.add_component(chicken_food, 1)
list_items.append(egg)

milk = hayday(
    name='milk',
    production_place='farm',
    level=6,
    production_time=td(hours=1),
    price_sell=32,
    img='/assets/items/Milk.png',
)
milk.add_component(cow_food, 1)
list_items.append(milk)

goat_milk = hayday(
    name='goat milk',
    production_place='farm',
    level=32,
    production_time=td(hours=8),
    price_sell=64,
    img='/assets/items/Goat_Milk.png',
)
goat_milk.add_component(goat_food, 1)
list_items.append(goat_milk)

honeycomb = hayday(
    name='honeycomb',
    production_place='farm',
    level=39,
    production_time=td(minutes=35),
    price_sell=68,
    img='/assets/items/Honeycomb.png',
)
list_items.append(honeycomb)

bacon = hayday(
    name='bacon',
    production_place='farm',
    level=10,
    production_time=td(hours=4),
    price_sell=50,
    img='/assets/items/Bacon.png',
)
bacon.add_component(pig_food, 1)
list_items.append(bacon)

wool = hayday(
    name='wool',
    production_place='farm',
    level=16,
    production_time=td(hours=6),
    price_sell=54,
    img='/assets/items/Wool.png',
)
wool.add_component(sheep_food, 1)
list_items.append(wool)

peanuts = hayday(
    name='peanuts',
    production_place='farm',
    level=62,
    production_time=td(hours=5),
    price_sell=234,
    img='/assets/items/Peanuts.png',
)
list_items.append(peanuts)
