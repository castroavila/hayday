#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : fudge_shop.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .dairy import butter, milk
from .crops import cacao, mint, chili_pepper, lemon
from .sugar_mill import white_sugar
from .animals import peanuts

rich_fudge = hayday(
    name='rich fudge',
    production_place='fudge shop',
    level=99,
    production_time=td(hours=2),
    price_sell=644,
    img='/assets/items/Rich_Fudge.png',
)
rich_fudge.add_component(butter, 3)
rich_fudge.add_component(cacao, 3)
rich_fudge.add_component(white_sugar, 1)
list_items.append(rich_fudge)

mint_fudge = hayday(
    name='mint fudge',
    production_place='fudge shop',
    level=102,
    production_time=td(hours=2, minutes=30),
    price_sell=522,
    img='/assets/items/Mint_Fudge.png',
)
mint_fudge.add_component(butter, 2)
mint_fudge.add_component(cacao, 2)
mint_fudge.add_component(white_sugar, 1)
mint_fudge.add_component(mint, 3)
list_items.append(mint_fudge)

chili_fudge = hayday(
    name='chili fudge',
    production_place='fudge shop',
    level=104,
    production_time=td(hours=2, minutes=50),
    price_sell=522,
    img='/assets/items/Chili_Fudge.png',
)
chili_fudge.add_component(butter, 2)
chili_fudge.add_component(cacao, 2)
chili_fudge.add_component(white_sugar, 1)
chili_fudge.add_component(chili_pepper, 3)
list_items.append(chili_fudge)

lemon_fudge = hayday(
    name='lemon fudge',
    production_place='fudge shop',
    level=108,
    production_time=td(hours=1, minutes=50),
    price_sell=590,
    img='/assets/items/Lemon_Fudge.png',
)
lemon_fudge.add_component(butter, 2)
lemon_fudge.add_component(white_sugar, 2)
lemon_fudge.add_component(milk, 3)
lemon_fudge.add_component(lemon, 2)
list_items.append(lemon_fudge)

peanut_fudge = hayday(
    name='peanut fudge',
    production_place='fudge shop',
    level=111,
    production_time=td(hours=1, minutes=30),
    price_sell=1141,
    img='/assets/items/Peanut_Fudge.png',
)
peanut_fudge.add_component(butter, 2)
peanut_fudge.add_component(cacao, 2)
peanut_fudge.add_component(white_sugar, 1)
peanut_fudge.add_component(peanuts, 2)
list_items.append(peanut_fudge)
