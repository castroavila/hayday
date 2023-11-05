#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : tea_stand.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    tea_leaf,
    lemon,
    ginger,
    apple,
    orange,
    peach,
    watermelon,
    mint,
    pomegranate,
)
from .dairy import milk
from .honey_extractor import honey


green_tea = hayday(
    name='green tea',
    production_place='tea stand',
    level=80,
    production_time=td(minutes=30),
    price_sell=241,
    img='/assets/items/Green_Tea.png',
)
green_tea.add_component(tea_leaf, 5)
list_items.append(green_tea)

milk_tea = hayday(
    name='milk tea',
    production_place='tea stand',
    level=81,
    production_time=td(minutes=45),
    price_sell=190,
    img='/assets/items/Milk_Tea.png',
)
milk_tea.add_component(tea_leaf, 3)
milk_tea.add_component(milk, 1)
list_items.append(milk_tea)

honey_tea = hayday(
    name='honey tea',
    production_place='tea stand',
    level=83,
    production_time=td(minutes=40),
    price_sell=313,
    img='/assets/items/Honey_Tea.png',
)
honey_tea.add_component(tea_leaf, 3)
honey_tea.add_component(honey, 1)
list_items.append(honey_tea)

lemon_tea = hayday(
    name='lemon tea',
    production_place='tea stand',
    level=86,
    production_time=td(minutes=20),
    price_sell=241,
    img='/assets/items/Lemon_Tea.png',
)
lemon_tea.add_component(tea_leaf, 3)
lemon_tea.add_component(lemon, 1)
list_items.append(lemon_tea)

apple_ginger_tea = hayday(
    name='apple ginger tea',
    production_place='tea stand',
    level=88,
    production_time=td(minutes=30),
    price_sell=169,
    img='/assets/items/Apple_Ginger_Tea.png',
)
apple_ginger_tea.add_component(ginger, 1)
apple_ginger_tea.add_component(apple, 2)
apple_ginger_tea.add_component(tea_leaf, 1)
list_items.append(apple_ginger_tea)

orange_tea = hayday(
    name='orange tea',
    production_place='tea stand',
    level=89,
    production_time=td(minutes=40),
    price_sell=255,
    img='/assets/items/Orange_Tea.png',
)
orange_tea.add_component(orange, 1)
orange_tea.add_component(tea_leaf, 3)
list_items.append(orange_tea)

iced_tea = hayday(
    name='iced tea',
    production_place='tea stand',
    level=92,
    production_time=td(minutes=30),
    price_sell=252,
    img='/assets/items/Iced_Tea.png',
)
iced_tea.add_component(peach, 1)
iced_tea.add_component(tea_leaf, 3)
list_items.append(iced_tea)

mint_tea = hayday(
    name='mint tea',
    production_place='tea stand',
    level=97,
    production_time=td(minutes=35),
    price_sell=255,
    img='/assets/items/Mint_Tea.png',
)
mint_tea.add_component(tea_leaf, 3)
mint_tea.add_component(watermelon, 1)
mint_tea.add_component(mint, 1)
list_items.append(mint_tea)

pomegrante_tea = hayday(
    name='pomegranate tea',
    production_place='tea stand',
    level=107,
    production_time=td(minutes=34),
    price_sell=313,
    img='/assets/items/Pomegranate_Tea.png',
)
pomegrante_tea.add_component(pomegranate, 1)
pomegrante_tea.add_component(tea_leaf, 4)
list_items.append(pomegrante_tea)
