#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : ice_cream_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .dairy import milk, cream
from .sugar_mill import syrup, white_sugar, brown_sugar
from .juice_press import cherry_juice
from .crops import (
    strawberry,
    cacao,
    sesame,
    orange,
    peach,
    mint,
    banana,
    cherry,
    coconut,
    guava,
    passion_fruit,
    mango,
)
from .animals import peanuts
from .honey_extractor import honey
from .coffee_kiosk import espresso

vanilla_ice_cream = hayday(
    name='vanilla ice cream',
    production_place='ice cream maker',
    level=29,
    production_time=td(hours=2),
    price_sell=172,
    img='/assets/items/Vanilla_Ice_Cream.png',
)
vanilla_ice_cream.add_component(milk, 1)
vanilla_ice_cream.add_component(cream, 1)
vanilla_ice_cream.add_component(white_sugar, 1)
list_items.append(vanilla_ice_cream)

cherry_popsicle = hayday(
    name='cherry popsicle',
    production_place='ice cream maker',
    level=33,
    production_time=td(hours=3),
    price_sell=352,
    img='/assets/items/Cherry_Popsicle.png',
)
cherry_popsicle.add_component(syrup, 1)
cherry_popsicle.add_component(cherry_juice, 1)
list_items.append(cherry_popsicle)

strawberry_ice_cream = hayday(
    name='strawberry ice cream',
    production_place='ice cream maker',
    level=34,
    production_time=td(hours=4),
    price_sell=331,
    img='/assets/items/Strawberry_Ice_Cream.png',
)
strawberry_ice_cream.add_component(milk, 1)
strawberry_ice_cream.add_component(cream, 1)
strawberry_ice_cream.add_component(white_sugar, 1)
strawberry_ice_cream.add_component(strawberry, 3)
list_items.append(strawberry_ice_cream)

chocolate_ice_cream = hayday(
    name='chocolate ice cream',
    production_place='ice cream maker',
    level=39,
    production_time=td(hours=2, minutes=30),
    price_sell=342,
    img='/assets/items/Chocolate_Ice_Cream.png',
)
chocolate_ice_cream.add_component(milk, 1)
chocolate_ice_cream.add_component(cream, 1)
chocolate_ice_cream.add_component(white_sugar, 1)
chocolate_ice_cream.add_component(cacao, 2)
list_items.append(chocolate_ice_cream)

sesame_ice_cream = hayday(
    name='sesame ice cream',
    production_place='ice cream maker',
    level=50,
    production_time=td(hours=2),
    price_sell=176,
    img='/assets/items/Sesame_Ice_Cream.png',
)
sesame_ice_cream.add_component(cream, 1)
sesame_ice_cream.add_component(brown_sugar, 1)
sesame_ice_cream.add_component(sesame, 3)
list_items.append(sesame_ice_cream)

peanut_butter_milkshake = hayday(
    name='peanut butter milkshake',
    production_place='ice cream maker',
    level=68,
    production_time=td(hours=1, minutes=40),
    price_sell=619,
    img='/assets/items/Peanut_Butter_Milkshake.png',
)
peanut_butter_milkshake.add_component(peanuts, 1)
peanut_butter_milkshake.add_component(milk, 1)
peanut_butter_milkshake.add_component(cream, 1)
peanut_butter_milkshake.add_component(cacao, 3)
list_items.append(peanut_butter_milkshake)

orange_sorbet = hayday(
    name='orange sorbet',
    production_place='ice cream maker',
    level=78,
    production_time=td(hours=3, minutes=30),
    price_sell=399,
    img='/assets/items/Orange_Sorbet.png',
)
orange_sorbet.add_component(honey, 1)
orange_sorbet.add_component(orange, 2)
list_items.append(orange_sorbet)

affogato = hayday(
    name='affogato',
    production_place='ice cream maker',
    level=78,
    production_time=td(minutes=20),
    price_sell=435,
    img='/assets/items/Affogato.png',
)
affogato.add_component(vanilla_ice_cream, 1)
affogato.add_component(espresso, 1)
list_items.append(affogato)

peach_ice_cream = hayday(
    name='peach ice cream',
    production_place='ice cream maker',
    level=83,
    production_time=td(hours=3),
    price_sell=450,
    img='/assets/items/Peach_Ice_Cream.png',
)
peach_ice_cream.add_component(cream, 1)
peach_ice_cream.add_component(honey, 1)
peach_ice_cream.add_component(peach, 2)
list_items.append(peach_ice_cream)


mint_ice_cream = hayday(
    name='mint ice cream',
    production_place='ice cream maker',
    level=85,
    production_time=td(hours=2, minutes=15),
    price_sell=288,
    img='/assets/items/Mint_Ice_Cream.png',
)
mint_ice_cream.add_component(cream, 1)
mint_ice_cream.add_component(white_sugar, 1)
mint_ice_cream.add_component(mint, 2)
mint_ice_cream.add_component(cacao, 1)
list_items.append(mint_ice_cream)

banana_split = hayday(
    name='banana split',
    production_place='ice cream maker',
    level=96,
    production_time=td(hours=3, minutes=30),
    price_sell=403,
    img='/assets/items/Banana_Split.png',
)
banana_split.add_component(banana, 1)
banana_split.add_component(cream, 1)
banana_split.add_component(cherry, 3)
list_items.append(banana_split)

coconut_ice_cream = hayday(
    name='coconut ice cream',
    production_place='ice cream maker',
    level=102,
    production_time=td(minutes=15),
    price_sell=320,
    img='/assets/items/Coconut_Ice_Cream.png',
)
coconut_ice_cream.add_component(coconut, 2)
coconut_ice_cream.add_component(syrup, 1)
list_items.append(coconut_ice_cream)

fruit_sorbet = hayday(
    name='fruit sorbet',
    production_place='ice cream maker',
    level=106,
    production_time=td(hours=1),
    price_sell=518,
    img='/assets/items/Fruit_Sorbet.png',
)
fruit_sorbet.add_component(guava, 1)
fruit_sorbet.add_component(passion_fruit, 1)
fruit_sorbet.add_component(mango, 2)
fruit_sorbet.add_component(white_sugar, 3)
list_items.append(fruit_sorbet)
