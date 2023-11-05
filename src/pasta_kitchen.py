#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : pasta_kitchen.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    potato,
    tomato,
    wheat,
    carrot,
    broccoli,
    chili_pepper,
    onion,
    mushroom,
)
from .dairy import butter, cheese, cream, goat_milk
from .sauce_maker import tomato_sauce
from .pasta_maker import fresh_pasta
from .fish import lobster_tail
from .animals import bacon, egg

gnocchi = hayday(
    name='gnocchi',
    production_place='pasta kitchen',
    level=72,
    production_time=td(hours=1, minutes=20),
    price_sell=475,
    img='/assets/items/Gnocchi.png',
)
gnocchi.add_component(potato, 4)
gnocchi.add_component(tomato, 3)
gnocchi.add_component(wheat, 2)
gnocchi.add_component(butter, 2)
list_items.append(gnocchi)

veggie_lasagna = hayday(
    name='veggie lasagna',
    production_place='pasta kitchen',
    level=74,
    production_time=td(hours=1, minutes=40),
    price_sell=532,
    img='/assets/items/Veggie_Lasagna.png',
)
veggie_lasagna.add_component(carrot, 1)
veggie_lasagna.add_component(cheese, 1)
veggie_lasagna.add_component(tomato_sauce, 1)
veggie_lasagna.add_component(fresh_pasta, 3)
list_items.append(veggie_lasagna)

lobster_pasta = hayday(
    name='lobster pasta',
    production_place='pasta kitchen',
    level=79,
    production_time=td(hours=2),
    price_sell=637,
    img='/assets/items/Lobster_Pasta.png',
)
lobster_pasta.add_component(lobster_tail, 1)
lobster_pasta.add_component(cream, 2)
lobster_pasta.add_component(fresh_pasta, 3)
lobster_pasta.add_component(tomato, 4)
list_items.append(lobster_pasta)

pasta_carbonara = hayday(
    name='pasta carbonara',
    production_place='pasta kitchen',
    level=83,
    production_time=td(hours=2, minutes=30),
    price_sell=410,
    img='/assets/items/Pasta_Carbonara.png',
)
pasta_carbonara.add_component(fresh_pasta, 3)
pasta_carbonara.add_component(bacon, 2)
pasta_carbonara.add_component(egg, 1)
pasta_carbonara.add_component(cheese, 1)
list_items.append(pasta_carbonara)

broccoli_pasta = hayday(
    name='broccoli pasta',
    production_place='pasta kitchen',
    level=83,
    production_time=td(hours=1),
    price_sell=345,
    img='/assets/items/Broccoli_Pasta.png',
)
broccoli_pasta.add_component(broccoli, 3)
broccoli_pasta.add_component(cheese, 1)
broccoli_pasta.add_component(fresh_pasta, 3)
list_items.append(broccoli_pasta)

spicy_pasta = hayday(
    name='spicy pasta',
    production_place='pasta kitchen',
    level=87,
    production_time=td(hours=1, minutes=30),
    price_sell=576,
    img='/assets/items/Spicy_Pasta.png',
)
spicy_pasta.add_component(fresh_pasta, 3)
spicy_pasta.add_component(tomato_sauce, 1)
spicy_pasta.add_component(chili_pepper, 3)
spicy_pasta.add_component(onion, 2)
list_items.append(spicy_pasta)

mushroom_pasta = hayday(
    name='mushroom pasta',
    production_place='pasta kitchen',
    level=101,
    production_time=td(hours=1, minutes=15),
    price_sell=280,
    img='/assets/items/Mushroom_Pasta.png',
)
mushroom_pasta.add_component(mushroom, 5)
mushroom_pasta.add_component(fresh_pasta, 3)
mushroom_pasta.add_component(goat_milk, 1)
list_items.append(mushroom_pasta)
