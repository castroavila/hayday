#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : sandwich_bar.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .bakery import bread, corn_bread
from .crops import tomato, lettuce, cucumber, onion, grapes
from .sauce_maker import mayonnaise, olive_oil, hummus
from .animals import egg, bacon, peanuts
from .dairy import milk, cheese, goat_cheese
from .honey_extractor import honey
from .jam_maker import raspberry_jam

veggie_bagel = hayday(
    name='veggie bagel',
    production_place='sandwich bar',
    level=61,
    production_time=td(minutes=40),
    price_sell=532,
    img='/assets/items/Veggie_Bagel.png',
)
veggie_bagel.add_component(bread, 2)
veggie_bagel.add_component(tomato, 2)
veggie_bagel.add_component(lettuce, 3)
veggie_bagel.add_component(olive_oil, 1)
list_items.append(veggie_bagel)

bacon_toast = hayday(
    name='bacon toast',
    production_place='sandwich bar',
    level=65,
    production_time=td(hours=1, minutes=40),
    price_sell=648,
    img='/assets/items/Bacon_Toast.png',
)
bacon_toast.add_component(bread, 2)
bacon_toast.add_component(bacon, 2)
bacon_toast.add_component(lettuce, 3)
bacon_toast.add_component(mayonnaise, 1)
list_items.append(bacon_toast)

egg_sandwich = hayday(
    name='egg sandwich',
    production_place='sandwich bar',
    level=66,
    production_time=td(hours=1, minutes=20),
    price_sell=583,
    img='/assets/items/Egg_Sandwich.png',
)
egg_sandwich.add_component(bread, 2)
egg_sandwich.add_component(egg, 2)
egg_sandwich.add_component(lettuce, 3)
egg_sandwich.add_component(mayonnaise, 1)
list_items.append(egg_sandwich)

honey_toast = hayday(
    name='honey toast',
    production_place='sandwich bar',
    level=69,
    production_time=td(hours=1),
    price_sell=255,
    img='/assets/items/Honey_Toast.png',
)
honey_toast.add_component(bread, 1)
honey_toast.add_component(egg, 1)
honey_toast.add_component(milk, 1)
honey_toast.add_component(honey, 1)
list_items.append(honey_toast)

peanut_butter_and_jelly_sandwich = hayday(
    name='peanut butter and jelly sandwich',
    production_place='sandwich bar',
    level=71,
    production_time=td(minutes=25),
    price_sell=601,
    img='/assets/items/Peanut_Butter_and_Jelly_Sandwich.png',
)
peanut_butter_and_jelly_sandwich.add_component(bread, 2)
peanut_butter_and_jelly_sandwich.add_component(raspberry_jam, 1)
peanut_butter_and_jelly_sandwich.add_component(peanuts, 1)
list_items.append(peanut_butter_and_jelly_sandwich)

cucumber_sandwich = hayday(
    name='cucumber sandwich',
    production_place='sandwich bar',
    level=79,
    production_time=td(minutes=35),
    price_sell=464,
    img='/assets/items/Cucumber_Sandwich.png',
)
cucumber_sandwich.add_component(cucumber, 2)
cucumber_sandwich.add_component(mayonnaise, 1)
cucumber_sandwich.add_component(bread, 2)
list_items.append(cucumber_sandwich)

onion_melt = hayday(
    name='onion melt',
    production_place='sandwich bar',
    level=84,
    production_time=td(hours=1, minutes=30),
    price_sell=417,
    img='/assets/items/Onion_Melt.png',
)
onion_melt.add_component(corn_bread, 2)
onion_melt.add_component(onion, 3)
onion_melt.add_component(cheese, 1)
list_items.append(onion_melt)


goat_cheese_toast = hayday(
    name='goat cheese toast',
    production_place='sandwich bar',
    level=92,
    production_time=td(minutes=50),
    price_sell=302,
    img='/assets/items/Goat_Cheese_Toast.png',
)
goat_cheese_toast.add_component(grapes, 3)
goat_cheese_toast.add_component(goat_cheese, 1)
goat_cheese_toast.add_component(bread, 1)
list_items.append(goat_cheese_toast)

hummus_wrap = hayday(
    name='hummus wrap',
    production_place='sandwich bar',
    level=109,
    production_time=td(minutes=30),
    price_sell=374,
    img='/assets/items/Hummus_Wrap.png',
)
hummus_wrap.add_component(hummus, 1)
hummus_wrap.add_component(bread, 1)
hummus_wrap.add_component(lettuce, 1)
list_items.append(hummus_wrap)
