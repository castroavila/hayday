#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : sauce_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    soybean,
    wheat,
    olive,
    lemon,
    chili_pepper,
    passion_fruit,
    chickpea,
    garlic,
    tomato,
    onion
)
from .animals import egg
from .bakery import bread
from .fish import fish_fillet
from .dairy import butter
from .sugar_mill import white_sugar, brown_sugar
from .honey_extractor import honey

soy_sauce = hayday(
    name='soy sauce',
    production_place='sauce maker',
    level=54,
    production_time=td(hours=3),
    price_sell=154,
    img='/assets/items/Soy_Sauce.png',
)
soy_sauce.add_component(soybean, 9)
soy_sauce.add_component(wheat, 1)
list_items.append(soy_sauce)

olive_oil = hayday(
    name='olive oil',
    production_place='sauce maker',
    level=60,
    production_time=td(minutes=45),
    price_sell=277,
    img='/assets/items/Olive_Oil.png',
)
olive_oil.add_component(olive, 3)
list_items.append(olive_oil)

mayonnaise = hayday(
    name='mayonnaise',
    production_place='sauce maker',
    level=62,
    production_time=td(minutes=15),
    price_sell=367,
    img='/assets/items/Mayonnaise.png',
)
mayonnaise.add_component(egg, 4)
mayonnaise.add_component(olive_oil, 1)
list_items.append(mayonnaise)

olive_dip = hayday(
    name='olive dip',
    production_place='sauce maker',
    level=66,
    production_time=td(minutes=45),
    price_sell=468,
    img='/assets/items/Olive_Dip.png',
)
olive_dip.add_component(olive, 3)
olive_dip.add_component(bread, 2)
olive_dip.add_component(fish_fillet, 1)
olive_dip.add_component(lemon, 1)
list_items.append(olive_dip)

lemon_curd = hayday(
    name='lemon curd',
    production_place='sauce maker',
    level=66,
    production_time=td(minutes=25),
    price_sell=378,
    img='/assets/items/Lemon_Curd.png',
)
lemon_curd.add_component(lemon, 2)
lemon_curd.add_component(butter, 1)
lemon_curd.add_component(egg, 2)
lemon_curd.add_component(white_sugar, 1)
list_items.append(lemon_curd)

tomato_sauce = hayday(
    name='tomate sauce',
    production_place='sauce maker',
    level=69,
    production_time=td(minutes=30),
    price_sell=230,
    img='/assets/items/Tomato_Sauce.png',
)
tomato_sauce.add_component(lemon, 1)
tomato_sauce.add_component(brown_sugar, 1)
tomato_sauce.add_component(tomato, 2)
list_items.append(tomato_sauce)

salsa = hayday(
    name='salsa',
    production_place='sauce maker',
    level=77,
    production_time=td(minutes=20),
    price_sell=252,
    img='/assets/items/Salsa.png',
)
salsa.add_component(chili_pepper, 2)
salsa.add_component(onion, 2)
salsa.add_component(tomato, 2)
list_items.append(salsa)

hummus = hayday(
    name='hummus',
    production_place='sauce maker',
    level=95,
    production_time=td(minutes=30),
    price_sell=277,
    img='/assets/items/Hummus.png',
)
hummus.add_component(chickpea, 3)
hummus.add_component(lemon, 2)
hummus.add_component(garlic, 2)
list_items.append(hummus)

tart_dressing = hayday(
    name='tart dressing',
    production_place='sauce maker',
    level=100,
    production_time=td(minutes=30),
    price_sell=288,
    img='/assets/items/Tart_Dressing.png',
)
tart_dressing.add_component(passion_fruit, 2)
tart_dressing.add_component(chili_pepper, 2)
tart_dressing.add_component(honey, 2)
list_items.append(tart_dressing)
