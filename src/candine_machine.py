#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : candine_machine.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .sugar_mill import syrup, white_sugar
from .crops import apple, wheat, cacao, cherry, strawberry, sesame, ginger
from .dairy import butter, cream
from .jam_maker import blackberry_jam, raspberry_jam
from .honey_extractor import honey
from .animals import peanuts

caramel_apple = hayday(
    name='caramel apple',
    production_place='candy machine',
    level=51,
    production_time=td(hours=2),
    price_sell=255,
    img='/assets/items/Caramel_Apple.png',
)
caramel_apple.add_component(syrup, 2)
caramel_apple.add_component(apple, 1)
list_items.append(caramel_apple)

toffee = hayday(
    name='toffee',
    production_place='candy machine',
    level=52,
    production_time=td(hours=1, minutes=30),
    price_sell=176,
    img='/assets/items/Toffee.png',
)
toffee.add_component(butter, 1)
toffee.add_component(wheat, 1)
toffee.add_component(white_sugar, 1)
list_items.append(toffee)

chocolate = hayday(
    name='chocolate',
    production_place='candy machine',
    level=54,
    production_time=td(hours=20),
    price_sell=460,
    img='/assets/items/Chocolate.png',
)
chocolate.add_component(cacao, 3)
chocolate.add_component(cream, 1)
chocolate.add_component(white_sugar, 1)
list_items.append(chocolate)

lollipop = hayday(
    name='lollipop',
    production_place='candy machine',
    level=57,
    production_time=td(hours=12),
    price_sell=342,
    img='/assets/items/Lollipop.png',
)
lollipop.add_component(syrup, 1)
lollipop.add_component(cherry, 1)
lollipop.add_component(strawberry, 2)
list_items.append(lollipop)

jelly_beans = hayday(
    name='jelly beans',
    production_place='candy machine',
    level=60,
    production_time=td(hours=24),
    price_sell=684,
    img='/assets/items/Jelly_Beans.png',
)
jelly_beans.add_component(blackberry_jam, 1)
jelly_beans.add_component(raspberry_jam, 1)
jelly_beans.add_component(white_sugar, 1)
list_items.append(jelly_beans)

honey_peanuts = hayday(
    name='honey peanuts',
    production_place='candy machine',
    level=63,
    production_time=td(minutes=40),
    price_sell=468,
    img='/assets/items/Honey_Peanuts.png',
)
honey_peanuts.add_component(honey, 1)
honey_peanuts.add_component(peanuts, 1)
list_items.append(honey_peanuts)

cotton_candy = hayday(
    name='cottom candy',
    production_place='candy machine',
    level=75,
    production_time=td(minutes=30),
    price_sell=226,
    img='/assets/items/Cotton_Candy.png',
)
cotton_candy.add_component(white_sugar, 3)
cotton_candy.add_component(strawberry, 1)
list_items.append(cotton_candy)

sesame_brittle = hayday(
    name='sesame brittle',
    production_place='candy machine',
    level=78,
    production_time=td(hours=1),
    price_sell=270,
    img='/assets/items/Sesame_Brittle.png',
)
sesame_brittle.add_component(sesame, 3)
sesame_brittle.add_component(ginger, 1)
sesame_brittle.add_component(honey, 1)
list_items.append(sesame_brittle)
