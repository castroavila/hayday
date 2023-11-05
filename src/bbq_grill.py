#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : bbq_grill.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .animals import egg, bacon
from .sugar_mill import brown_sugar
from .bakery import bread
from .fish import fish_fillet, lobster_tail
from .crops import (
    tomato,
    chili_pepper,
    potato,
    garlic,
    onion,
    beetroot,
    carrot,
    pumpkin,
    eggplant,
    mushroom,
    ginger,
    sesame,
    lemon,
    asparagus,
    bell_pepper,
    rice,
    banana,
    blackberry,
    wheat,
)
from .dairy import cream, cheese, butter
from .sauce_maker import salsa
from .honey_extractor import honey

pancake = hayday(
    name='pancake',
    production_place='bbq grill',
    level=9,
    production_time=td(minutes=30),
    price_sell=108,
    img='/assets/items/Pancake.png',
)
pancake.add_component(egg, 3)
pancake.add_component(brown_sugar, 1)
list_items.append(pancake)

bacon_and_eggs = hayday(
    name='bakon and eggs',
    production_place='bbq grill',
    level=11,
    production_time=td(minutes=60),
    price_sell=201,
    img='/assets/items/Bacon_and_Eggs.png',
)
bacon_and_eggs.add_component(egg, 4)
bacon_and_eggs.add_component(bacon, 2)
list_items.append(bacon_and_eggs)

hamburger = hayday(
    name='hamburger',
    production_place='bbq grill',
    level=18,
    production_time=td(hours=2),
    price_sell=180,
    img='/assets/items/Hamburger.png',
)
hamburger.add_component(bread, 2)
hamburger.add_component(bacon, 2)
list_items.append(hamburger)

fish_burger = hayday(
    name='fish burger',
    production_place='bbq grill',
    level=27,
    production_time=td(hours=2),
    price_sell=226,
    img='/assets/items/Fish_Burger.png',
)
fish_burger.add_component(fish_fillet, 2)
fish_burger.add_component(bread, 2)
fish_burger.add_component(chili_pepper, 1)
list_items.append(fish_burger)

roasted_tomatoes = hayday(
    name='roasted tomatoes',
    production_place='bbq grill',
    level=30,
    production_time=td(hours=1, minutes=30),
    price_sell=118,
    img='/assets/items/Roasted_Tomatoes.png',
)
roasted_tomatoes.add_component(tomato, 2)
list_items.append(roasted_tomatoes)

baked_potato = hayday(
    name='baked potato',
    production_place='bbq grill',
    level=35,
    production_time=td(minutes=35),
    price_sell=298,
    img='/assets/items/Baked_Potato.png',
)
baked_potato.add_component(potato, 2)
baked_potato.add_component(chili_pepper, 1)
baked_potato.add_component(cream, 1)
baked_potato.add_component(cheese, 1)
list_items.append(baked_potato)

fish_and_chips = hayday(
    name='fish and chips',
    production_place='bbq grill',
    level=41,
    production_time=td(hours=1, minutes=30),
    price_sell=244,
    img='/assets/items/Fish_and_Chips.png',
)
fish_and_chips.add_component(fish_fillet, 2)
fish_and_chips.add_component(potato, 3)
list_items.append(fish_and_chips)

lobster_skewer = hayday(
    name='lobster skewer',
    production_place='bbq grill',
    level=48,
    production_time=td(minutes=40),
    price_sell=417,
    img='/assets/items/Lobster_Skewer.png',
)
lobster_skewer.add_component(lobster_tail, 1)
lobster_skewer.add_component(chili_pepper, 1)
lobster_skewer.add_component(honey, 1)
list_items.append(lobster_skewer)

garlic_bread = hayday(
    name='garlic bread',
    production_place='bbq grill',
    level=60,
    production_time=td(minutes=15),
    price_sell=198,
    img='/assets/items/Garlic_Bread.png',
)
garlic_bread.add_component(bread, 2)
garlic_bread.add_component(butter, 1)
garlic_bread.add_component(garlic, 4)
list_items.append(garlic_bread)


grilled_onion = hayday(
    name='grilled onion',
    production_place='bbq grill',
    level=68,
    production_time=td(hours=1),
    price_sell=190,
    img='/assets/items/Grilled_Onion.png',
)
grilled_onion.add_component(butter, 1)
grilled_onion.add_component(onion, 2)
list_items.append(grilled_onion)

winter_veggies = hayday(
    name='winter veggies',
    production_place='bbq grill',
    level=72,
    production_time=td(minutes=25),
    price_sell=198,
    img='/assets/items/Winter_Veggies.png',
)
winter_veggies.add_component(beetroot, 2)
winter_veggies.add_component(carrot, 2)
winter_veggies.add_component(potato, 2)
winter_veggies.add_component(pumpkin, 2)
list_items.append(winter_veggies)

stuffed_peppers = hayday(
    name='stuffed peppers',
    production_place='bbq grill',
    level=80,
    production_time=td(minutes=20),
    price_sell=352,
    img='/assets/items/Stuffed_Peppers.png',
)
stuffed_peppers.add_component(bell_pepper, 3)
stuffed_peppers.add_component(bacon, 1)
stuffed_peppers.add_component(rice, 3)
stuffed_peppers.add_component(cheese, 1)
list_items.append(stuffed_peppers)

grilled_eggplant = hayday(
    name='grilled eggplant',
    production_place='bbq grill',
    level=90,
    production_time=td(minutes=40),
    price_sell=324,
    img='/assets/items/Grilled_Eggplant.png',
)
grilled_eggplant.add_component(eggplant, 3)
grilled_eggplant.add_component(salsa, 1)
list_items.append(grilled_eggplant)

banana_pancakes = hayday(
    name='banana pancakes',
    production_place='bbq grill',
    level=94,
    production_time=td(hours=1),
    price_sell=352,
    img='/assets/items/Banana_Pancakes.png',
)
banana_pancakes.add_component(banana, 1)
banana_pancakes.add_component(blackberry, 2)
banana_pancakes.add_component(wheat, 3)
banana_pancakes.add_component(cream, 1)
list_items.append(banana_pancakes)

fish_skewer = hayday(
    name='fish skewer',
    production_place='bbq grill',
    level=96,
    production_time=td(minutes=30),
    price_sell=176,
    img='/assets/items/Fish_Skewer.png',
)
fish_skewer.add_component(fish_fillet, 1)
fish_skewer.add_component(mushroom, 3)
fish_skewer.add_component(ginger, 1)
fish_skewer.add_component(sesame, 2)
list_items.append(fish_skewer)

grilled_asparagus = hayday(
    name='grilled asparagus',
    production_place='bbq grill',
    level=67,
    production_time=td(hours=1, minutes=15),
    price_sell=486,
    img='/assets/items/Grilled_Asparagus.png',
)
grilled_asparagus.add_component(asparagus, 5)
grilled_asparagus.add_component(bacon, 3)
grilled_asparagus.add_component(lemon, 1)
list_items.append(grilled_asparagus)
