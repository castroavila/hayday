#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : animal_food.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .crops import wheat, corn, soybean, carrot

chicken_food = hayday(
    name='chicken food',
    production_place='feed mill',
    level=3,
    production_time=td(minutes=5),
    price_sell=7.0,
    img='/assets/items/Chicken_Feed.png',
)
chicken_food.add_component(wheat, 2)
chicken_food.add_component(corn, 1)
list_items.append(chicken_food)

cow_food = hayday(
    name='cow food',
    production_place='feed mill',
    level=6,
    production_time=td(minutes=10),
    price_sell=14,
    img='/assets/items/Cow_Feed.png',
)
cow_food.add_component(soybean, 2)
cow_food.add_component(corn, 1)
list_items.append(cow_food)

# TODO
pig_food = hayday(
    name='pig food',
    production_place='feed mill',
    level=10,
    production_time=td(minutes=20),
    price_sell=14,
    img='/assets/items/Pig_Feed.png',
)
pig_food.add_component(soybean, 1)
pig_food.add_component(carrot, 2)
list_items.append(pig_food)

# TODO
sheep_food = hayday(
    name='sheep food',
    production_place='feed mill',
    level=16,
    production_time=td(minutes=30),
    price_sell=14,
    img='/assets/items/Sheep_Feed.png',
)
sheep_food.add_component(soybean, 1)
sheep_food.add_component(wheat, 3)
list_items.append(sheep_food)

# TODO
goat_food = hayday(
    name='goat food',
    production_place='feed mill',
    level=32,
    production_time=td(minutes=40),
    price_sell=14,
    img='/assets/items/Goat_Feed.png',
)
goat_food.add_component(wheat, 1)
goat_food.add_component(corn, 1)
goat_food.add_component(carrot, 2)
list_items.append(goat_food)
