#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : soup_kitchen.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .fish import lobster_tail
from .crops import (
    tomato,
    chili_pepper,
    pumpkin,
    carrot,
    potato,
    cabbage,
    onion,
    bell_pepper,
    broccoli,
    mushroom,
    asparagus,
)
from .dairy import cream, goat_cheese, butter, milk, cheese
from .juice_press import tomato_juice
from .honey_extractor import honey
from .fish import fish_fillet
from .animals import bacon, egg
from .bakery import bread
from .pasta_maker import rice_noodles
from .sauce_maker import olive_oil

lobster_soup = hayday(
    name='lobster soup',
    production_place='soup kitchen',
    level=46,
    production_time=td(hours=2, minutes=30),
    price_sell=612,
    img='/assets/items/Lobster_Soup.png',
)
lobster_soup.add_component(lobster_tail, 2)
lobster_soup.add_component(tomato, 1)
lobster_soup.add_component(chili_pepper, 2)
lobster_soup.add_component(cream, 1)
list_items.append(lobster_soup)

tomato_soup = hayday(
    name='tomato soup',
    production_place='soup kitchen',
    level=47,
    production_time=td(hours=1, minutes=30),
    price_sell=478,
    img='/assets/items/Tomato_Soup.png',
)
tomato_soup.add_component(tomato, 2)
tomato_soup.add_component(tomato_juice, 1)
tomato_soup.add_component(chili_pepper, 1)
tomato_soup.add_component(goat_cheese, 1)
list_items.append(tomato_soup)


pumpkin_soup = hayday(
    name='pumpkin soup',
    production_place='soup kitchen',
    level=49,
    production_time=td(hours=2),
    price_sell=392,
    img='/assets/items/Pumpkin_Soup.png',
)
pumpkin_soup.add_component(pumpkin, 3)
pumpkin_soup.add_component(butter, 1)
pumpkin_soup.add_component(honey, 1)
pumpkin_soup.add_component(carrot, 2)
list_items.append(pumpkin_soup)

fish_soup = hayday(
    name='fish soup',
    production_place='soup kitchen',
    level=53,
    production_time=td(hours=3),
    price_sell=298,
    img='/assets/items/Fish_Soup.png',
)
fish_soup.add_component(potato, 3)
fish_soup.add_component(fish_fillet, 2)
fish_soup.add_component(milk, 1)
fish_soup.add_component(carrot, 1)
list_items.append(fish_soup)

cabbage_soup = hayday(
    name='cabbage soup',
    production_place='soup kitchen',
    level=65,
    production_time=td(hours=1, minutes=30),
    price_sell=270,
    img='/assets/items/Cabbage_Soup.png',
)
cabbage_soup.add_component(cabbage, 3)
cabbage_soup.add_component(bacon, 2)
cabbage_soup.add_component(potato, 2)
cabbage_soup.add_component(carrot, 2)
list_items.append(cabbage_soup)

onion_soup = hayday(
    name='onion soup',
    production_place='soup kitchen',
    level=72,
    production_time=td(hours=2, minutes=30),
    price_sell=327,
    img='/assets/items/Onion_Soup.png',
)
onion_soup.add_component(bread, 2)
onion_soup.add_component(cheese, 1)
onion_soup.add_component(onion, 3)
list_items.append(onion_soup)

noodle_soup = hayday(
    name='noodle soup',
    production_place='soup kitchen',
    level=73,
    production_time=td(hours=2),
    price_sell=432,
    img='/assets/items/Noodle_Soup.png',
)
noodle_soup.add_component(carrot, 2)
noodle_soup.add_component(chili_pepper, 1)
noodle_soup.add_component(egg, 2)
noodle_soup.add_component(rice_noodles, 3)
list_items.append(noodle_soup)

potato_soup = hayday(
    name='potato soup',
    production_place='soup kitchen',
    level=78,
    production_time=td(hours=2, minutes=30),
    price_sell=255,
    img='/assets/items/Potato_Soup.png',
)
potato_soup.add_component(potato, 3)
potato_soup.add_component(onion, 2)
potato_soup.add_component(milk, 1)
list_items.append(potato_soup)

bell_pepper_soup = hayday(
    name='bell pepper soup',
    production_place='soup kitchen',
    level=81,
    production_time=td(hours=1),
    price_sell=439,
    img='/assets/items/Bell_Pepper_Soup.png',
)
bell_pepper_soup.add_component(bread, 1)
bell_pepper_soup.add_component(olive_oil, 1)
bell_pepper_soup.add_component(chili_pepper, 1)
bell_pepper_soup.add_component(bell_pepper, 2)
list_items.append(bell_pepper_soup)

broccoli_soup = hayday(
    name='broccoli soup',
    production_place='soup kitchen',
    level=87,
    production_time=td(hours=1, minutes=30),
    price_sell=237,
    img='/assets/items/Broccoli_Soup.png',
)
broccoli_soup.add_component(broccoli, 3)
broccoli_soup.add_component(onion, 1)
broccoli_soup.add_component(potato, 3)
list_items.append(broccoli_soup)

mushroom_soup = hayday(
    name='mushroom soup',
    production_place='soup kitchen',
    level=104,
    production_time=td(hours=1, minutes=20),
    price_sell=176,
    img='/assets/items/Mushroom_Soup.png',
)
mushroom_soup.add_component(mushroom, 3)
mushroom_soup.add_component(milk, 1)
mushroom_soup.add_component(onion, 2)
list_items.append(mushroom_soup)

asparagus_soup = hayday(
    name='asparagus soup',
    production_place='soup kitchen',
    level=51,
    production_time=td(hours=1),
    price_sell=255,
    img='/assets/items/Asparagus_Soup.png',
)
asparagus_soup.add_component(asparagus, 3)
asparagus_soup.add_component(cream, 2)
list_items.append(asparagus_soup)
