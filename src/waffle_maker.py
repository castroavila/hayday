#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : waffle_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .sugar_mill import white_sugar, syrup, brown_sugar
from .animals import egg, bacon, milk
from .crops import (
    wheat,
    raspberry,
    blackberry,
    cacao,
    strawberry,
    banana,
    asparagus,
    blueberry,
    onion,
    lemon,
)

plain_waffles = hayday(
    name='plain waffles',
    production_place='waffle maker',
    level=114,
    production_time=td(minutes=25),
    price_sell=198,
    img='/assets/items/Plain_Waffles.png',
)
plain_waffles.add_component(white_sugar, 2)
plain_waffles.add_component(egg, 3)
plain_waffles.add_component(wheat, 5)
list_items.append(plain_waffles)

berry_waffles = hayday(
    name='berry waffles',
    production_place='waffle maker',
    level=114,
    production_time=td(minutes=35),
    price_sell=604,
    img='/assets/items/Berry_Waffles.png',
)
berry_waffles.add_component(plain_waffles, 1)
berry_waffles.add_component(syrup, 1)
berry_waffles.add_component(raspberry, 3)
berry_waffles.add_component(blackberry, 2)
list_items.append(berry_waffles)

chocolate_waffles = hayday(
    name='chocolate waffles',
    production_place='waffle maker',
    level=117,
    production_time=td(minutes=40),
    price_sell=637,
    img='/assets/items/Chocolate_Waffles.png',
)
chocolate_waffles.add_component(plain_waffles, 1)
chocolate_waffles.add_component(cacao, 2)
chocolate_waffles.add_component(strawberry, 3)
chocolate_waffles.add_component(banana, 1)
list_items.append(chocolate_waffles)

breakfast_waffles = hayday(
    name='breakfast waffles',
    production_place='waffle maker',
    level=119,
    production_time=td(minutes=45),
    price_sell=424,
    img='/assets/items/Breakfast_Waffles.png',
)
breakfast_waffles.add_component(plain_waffles, 1)
breakfast_waffles.add_component(bacon, 2)
breakfast_waffles.add_component(egg, 1)
breakfast_waffles.add_component(asparagus, 2)
list_items.append(breakfast_waffles)

blueberry_chutney = hayday(
    name='blueberry chutney',
    production_place='waffle maker',
    level=70,
    production_time=td(hours=4),
    price_sell=579,
    img='/assets/items/Blueberry_Chutney.png',
)
blueberry_chutney.add_component(onion, 1)
blueberry_chutney.add_component(brown_sugar, 1)
blueberry_chutney.add_component(blueberry, 3)
blueberry_chutney.add_component(lemon, 1)
list_items.append(blueberry_chutney)

blueberry_waffles = hayday(
    name='blueberry waffles',
    production_place='waffle maker',
    level=118,
    production_time=td(minutes=42),
    price_sell=669,
    img='assets/items/Blueberry_Waffles.png',
)
blueberry_waffles.add_component(plain_waffles, 1)
blueberry_waffles.add_component(milk, 1)
blueberry_waffles.add_component(cacao, 2)
blueberry_waffles.add_component(blueberry, 3)
list_items.append(blueberry_waffles)
