#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : sushi_bar.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .fish import fish_fillet, lobster_tail
from .crops import rice, lettuce, sesame, plum
from .sauce_maker import soy_sauce
from .sugar_mill import brown_sugar
from .animals import egg

sushi_roll = hayday(
    name='sushi roll',
    production_place='sushi bar',
    level=56,
    production_time=td(hours=1),
    price_sell=489,
    img='/assets/items/sushi_roll.png',
)
sushi_roll.add_component(fish_fillet, 1)
sushi_roll.add_component(rice, 15)
sushi_roll.add_component(soy_sauce, 1)
list_items.append(sushi_roll)

lobster_sushi = hayday(
    name='lobster sushi',
    production_place='sushi bar',
    level=59,
    production_time=td(hours=1),
    price_sell=637,
    img='/assets/items/lobster_sushi.png',
)
lobster_sushi.add_component(lobster_tail, 1)
lobster_sushi.add_component(rice, 15)
lobster_sushi.add_component(soy_sauce, 1)
list_items.append(lobster_sushi)

egg_sushi = hayday(
    name='egg sushi',
    production_place='sushi bar',
    level=66,
    production_time=td(hours=2),
    price_sell=550,
    img='/assets/items/egg_sushi.png',
)
egg_sushi.add_component(brown_sugar, 1)
egg_sushi.add_component(egg, 4)
egg_sushi.add_component(rice, 15)
egg_sushi.add_component(soy_sauce, 1)
list_items.append(egg_sushi)

big_sushi_roll = hayday(
    name='big sushi roll',
    production_place='sushi bar',
    level=76,
    production_time=td(hours=1, minutes=30),
    price_sell=648,
    img='/assets/items/big_sushi_roll.png',
)
big_sushi_roll.add_component(fish_fillet, 1)
big_sushi_roll.add_component(rice, 20)
big_sushi_roll.add_component(egg, 3)
big_sushi_roll.add_component(lettuce, 5)
list_items.append(big_sushi_roll)

rice_ball = hayday(
    name='rice ball',
    production_place='sushi bar',
    level=110,
    production_time=td(minutes=45),
    price_sell=464,
    img='/assets/items/rice_ball.png',
)
rice_ball.add_component(rice, 20)
rice_ball.add_component(sesame, 1)
rice_ball.add_component(plum, 1)
list_items.append(rice_ball)
