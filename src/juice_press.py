#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : juice_press.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    carrot,
    apple,
    cherry,
    tomato,
    blackberry,
    pineapple,
    orange,
    mango,
    watermelon,
    guava,
    grapes,
    passion_fruit,
    raspberry,
)

carrot_juice = hayday(
    name='carrot juice',
    production_place='juice press',
    level=26,
    production_time=td(minutes=30),
    price_sell=46,
    img='/assets/items/Carrot_Juice.png',
)
carrot_juice.add_component(carrot, 3)
list_items.append(carrot_juice)

apple_juice = hayday(
    name='apple juice',
    production_place='juice press',
    level=28,
    production_time=td(hours=2),
    price_sell=129,
    img='/assets/items/Apple_Juice.png',
)
apple_juice.add_component(apple, 2)
list_items.append(apple_juice)

cherry_juice = hayday(
    name='cherry juice',
    production_place='juice press',
    level=30,
    production_time=td(hours=2, minutes=30),
    price_sell=216,
    img='/assets/items/Cherry_Juice.png',
)
cherry_juice.add_component(cherry, 2)
list_items.append(cherry_juice)

tomato_juice = hayday(
    name='tomato juice',
    production_place='juice press',
    level=31,
    production_time=td(hours=1, minutes=30),
    price_sell=162,
    img='/assets/items/Tomato_Juice.png',
)
tomato_juice.add_component(tomato, 3)
list_items.append(tomato_juice)

berry_juice = hayday(
    name='berry juice',
    production_place='juice press',
    level=31,
    production_time=td(hours=3),
    price_sell=205,
    img='/assets/items/Berry_Juice.png',
)
berry_juice.add_component(blackberry, 1)
berry_juice.add_component(raspberry, 1)
list_items.append(berry_juice)

pineapple_juice = hayday(
    name='pineapple juice',
    production_place='juice press',
    level=52,
    production_time=td(minutes=45),
    price_sell=68,
    img='/assets/items/Pineapple_Juice.png',
)
pineapple_juice.add_component(pineapple, 3)
list_items.append(pineapple_juice)

orange_juice = hayday(
    name='orange juice',
    production_place='juice press',
    level=71,
    production_time=td(hours=2),
    price_sell=234,
    img='/assets/items/Orange_Juice.png',
)
orange_juice.add_component(orange, 2)
list_items.append(orange_juice)

grape_juice = hayday(
    name='grape juice',
    production_place='juice press',
    level=84,
    production_time=td(hours=2, minutes=30),
    price_sell=104,
    img='/assets/items/Grape_Juice.png',
)
grape_juice.add_component(grapes, 2)
list_items.append(grape_juice)

passion_fruit_juice = hayday(
    name='passion fruit juice',
    production_place='juice press',
    level=88,
    production_time=td(minutes=45),
    price_sell=104,
    img='/assets/items/Passion_Fruit_Juice.png',
)
passion_fruit_juice.add_component(passion_fruit, 2)
list_items.append(passion_fruit_juice)


watermelon_juice = hayday(
    name='watermelon juice',
    production_place='juice press',
    level=92,
    production_time=td(hours=1),
    price_sell=108,
    img='/assets/items/Watermelon_Juice.png',
)
watermelon_juice.add_component(watermelon, 2)
list_items.append(watermelon_juice)

mango_juice = hayday(
    name='mango juice',
    production_place='juice press',
    level=97,
    production_time=td(minutes=50),
    price_sell=230,
    img='/assets/items/Mango_Juice.png',
)
mango_juice.add_component(mango, 2)
list_items.append(mango_juice)

guava_juice = hayday(
    name='guava juice',
    production_place='juice press',
    level=104,
    production_time=td(minutes=55),
    price_sell=252,
    img='/assets/items/Guava_Juice.png',
)
guava_juice.add_component(guava, 2)
list_items.append(guava_juice)
