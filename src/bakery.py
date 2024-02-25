#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : bakery.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .crops import (
    wheat,
    corn,
    raspberry,
    blackberry,
    tomato,
    chili_pepper,
    potato,
    ginger,
    banana,
    grapes,
    cacao,
    coconut,
    pineapple,
    oats,
)
from .animals import egg
from .dairy import cheese, butter
from .sugar_mill import brown_sugar, white_sugar, syrup
from .fish import fish_fillet, lobster_tail

bread = hayday(
    name='bread',
    production_place='bakery',
    level=2,
    production_time=td(minutes=5),
    price_sell=21,
    img='/assets/items/Bread.png',
)
bread.add_component(wheat, 3)
list_items.append(bread)

corn_bread = hayday(
    name='corn bread',
    production_place='bakery',
    level=7,
    production_time=td(minutes=30),
    price_sell=72,
    img='/assets/items/Corn_Bread.png',
)
corn_bread.add_component(corn, 2)
corn_bread.add_component(egg, 2)
list_items.append(corn_bread)

cookie = hayday(
    name='cookie',
    production_place='bakery',
    level=10,
    production_time=td(hours=1),
    price_sell=104,
    img='/assets/items/Cookie.png',
)
cookie.add_component(wheat, 2)
cookie.add_component(egg, 2)
cookie.add_component(brown_sugar, 1)
list_items.append(cookie)

raspberry_muffin = hayday(
    name='raspberry muffin',
    production_place='bakery',
    level=19,
    production_time=td(minutes=45),
    price_sell=140,
    img='/assets/items/Raspberry_Muffin.png',
)
raspberry_muffin.add_component(wheat, 2)
raspberry_muffin.add_component(egg, 1)
raspberry_muffin.add_component(raspberry, 2)
list_items.append(raspberry_muffin)

blackbery_muffin = hayday(
    name='blackberry muffin',
    production_place='bakery',
    level=26,
    production_time=td(minutes=45),
    price_sell=226,
    img='/assets/items/Blackberry_Muffin.png',
)
blackbery_muffin.add_component(wheat, 1)
blackbery_muffin.add_component(egg, 2)
blackbery_muffin.add_component(blackberry, 2)
list_items.append(blackbery_muffin)

pizza = hayday(
    name='pizza',
    production_place='bakery',
    level=33,
    production_time=td(minutes=15),
    price_sell=190,
    img='/assets/items/Pizza.png',
)
pizza.add_component(wheat, 2)
pizza.add_component(tomato, 1)
pizza.add_component(cheese, 1)
list_items.append(pizza)

spicy_pizza = hayday(
    name='spicy pizza',
    production_place='bakery',
    level=37,
    production_time=td(minutes=15),
    price_sell=226,
    img='/assets/items/Spicy_Pizza.png',
)
spicy_pizza.add_component(wheat, 2)
spicy_pizza.add_component(tomato, 1)
spicy_pizza.add_component(cheese, 1)
spicy_pizza.add_component(chili_pepper, 1)
list_items.append(spicy_pizza)

potato_bread = hayday(
    name='potato bread',
    production_place='bakery',
    level=39,
    production_time=td(minutes=45),
    price_sell=284,
    img='/assets/items/Potato_Bread.png',
)
potato_bread.add_component(potato, 2)
potato_bread.add_component(white_sugar, 1)
potato_bread.add_component(egg, 3)
potato_bread.add_component(butter, 1)
list_items.append(potato_bread)

frutti_di_mare_pizza = hayday(
    name='frutti di mare pizza',
    production_place='bakery',
    level=45,
    production_time=td(minutes=15),
    price_sell=403,
    img='/assets/items/Frutti_di_Mare_Pizza.png',
)
frutti_di_mare_pizza.add_component(wheat, 2)
frutti_di_mare_pizza.add_component(fish_fillet, 1)
frutti_di_mare_pizza.add_component(lobster_tail, 1)
frutti_di_mare_pizza.add_component(cheese, 1)
list_items.append(frutti_di_mare_pizza)

gingerbread_cookie = hayday(
    name='ginger bread cookie',
    production_place='bakery',
    level=86,
    production_time=td(minutes=30),
    price_sell=273,
    img='/assets/items/Gingerbread_Cookie.png',
)
gingerbread_cookie.add_component(wheat, 5)
gingerbread_cookie.add_component(butter, 1)
gingerbread_cookie.add_component(syrup, 1)
gingerbread_cookie.add_component(ginger, 2)
list_items.append(gingerbread_cookie)

banana_bread = hayday(
    name='banana bread',
    production_place='bakery',
    level=91,
    production_time=td(minutes=30),
    price_sell=424,
    img='/assets/items/Banana_Bread.png',
)
banana_bread.add_component(banana, 3)
banana_bread.add_component(grapes, 2)
banana_bread.add_component(wheat, 3)
banana_bread.add_component(egg, 1)
list_items.append(banana_bread)

macaroon = hayday(
    name='macaroon',
    production_place='bakery',
    level=101,
    production_time=td(minutes=30),
    price_sell=421,
    img='/assets/items/Macaroon.png',
)
macaroon.add_component(cacao, 1)
macaroon.add_component(coconut, 2)
macaroon.add_component(white_sugar, 2)
list_items.append(macaroon)

pineaple_coconut_bars = hayday(
    name='pineaple coconut bars',
    production_place='bakery',
    level=120,
    production_time=td(minutes=40),
    price_sell=284,
    img='/assets/items/Pineapple_Coconut_Bars.png',
)
pineaple_coconut_bars.add_component(coconut, 1)
pineaple_coconut_bars.add_component(white_sugar, 2)
pineaple_coconut_bars.add_component(oats, 3)
pineaple_coconut_bars.add_component(pineapple, 2)
list_items.append(pineaple_coconut_bars)
