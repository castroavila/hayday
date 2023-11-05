#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : donut_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .dairy import milk, cream
from .sugar_mill import white_sugar, brown_sugar, syrup
from .animals import egg, peanuts, bacon
from .crops import wheat, cacao
from .jam_maker import raspberry_jam

plain_donut = hayday(
    name='plain donut',
    production_place='donut maker',
    level=76,
    production_time=td(minutes=15),
    price_sell=129,
    img='/assets/items/Plain_Donut.png',
)
plain_donut.add_component(milk, 1)
plain_donut.add_component(white_sugar, 1)
plain_donut.add_component(egg, 1)
plain_donut.add_component(wheat, 3)
list_items.append(plain_donut)

sprinkled_donut = hayday(
    name='sprinkled donut',
    production_place='donut maker',
    level=79,
    production_time=td(minutes=20),
    price_sell=313,
    img='/assets/items/Sprinkled_Donut.png',
)
sprinkled_donut.add_component(plain_donut, 1)
sprinkled_donut.add_component(cacao, 2)
list_items.append(sprinkled_donut)

crunchy_donut = hayday(
    name='crunchy donut',
    production_place='donut maker',
    level=82,
    production_time=td(minutes=30),
    price_sell=594,
    img='/assets/items/Crunchy_Donut.png',
)
crunchy_donut.add_component(plain_donut, 1)
crunchy_donut.add_component(cacao, 1)
crunchy_donut.add_component(peanuts, 1)
list_items.append(crunchy_donut)

cream_donut = hayday(
    name='cream donut',
    production_place='donut maker',
    level=86,
    production_time=td(minutes=25),
    price_sell=230,
    img='/assets/items/Cream_Donut.png',
)
cream_donut.add_component(plain_donut, 1)
cream_donut.add_component(cream, 1)
cream_donut.add_component(brown_sugar, 1)
list_items.append(cream_donut)

bacon_donut = hayday(
    name='bacon donut',
    production_place='donut maker',
    level=88,
    production_time=td(minutes=30),
    price_sell=388,
    img='/assets/items/Bacon_Donut.png',
)
bacon_donut.add_component(plain_donut, 1)
bacon_donut.add_component(bacon, 3)
bacon_donut.add_component(syrup, 1)
list_items.append(bacon_donut)

filled_donut = hayday(
    name='filled donut',
    production_place='donut maker',
    level=93,
    production_time=td(minutes=35),
    price_sell=403,
    img='/assets/items/Filled_Donut.png',
)
filled_donut.add_component(plain_donut, 1)
filled_donut.add_component(raspberry_jam, 1)
list_items.append(filled_donut)
