#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : cake_oven.py
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
    wheat,
    raspberry,
    cherry,
    strawberry,
    potato,
    apple,
    lily,
    cherry,
    grapes,
    orange,
    cacao,
    mint,
    pomegranate,
    pineapple
)
from .dairy import butter, cream, cheese, goat_cheese
from .animals import milk, egg
from .sugar_mill import brown_sugar, white_sugar
from .honey_extractor import honey
from .mine import gold_ore
from .sauce_maker import lemon_curd
from .bakery import cookie

carrot_cake = hayday(
    name='carrot cake',
    production_place='cake oven',
    level=21,
    production_time=td(hours=1, minutes=30),
    price_sell=165,
    img='/assets/items/Carrot_Cake.png',
)
carrot_cake.add_component(carrot, 2)
carrot_cake.add_component(butter, 1)
carrot_cake.add_component(brown_sugar, 1)
list_items.append(carrot_cake)

cream_cake = hayday(
    name='cream cake',
    production_place='cake oven',
    level=23,
    production_time=td(hours=3),
    price_sell=219,
    img='/assets/items/Cream_Cake.png',
)
cream_cake.add_component(wheat, 5)
cream_cake.add_component(cream, 1)
cream_cake.add_component(white_sugar, 1)
list_items.append(cream_cake)

red_berry_cake = hayday(
    name='red berry cake',
    production_place='cake oven',
    level=23,
    production_time=td(hours=1),
    price_sell=255,
    img='/assets/items/Red_Berry_Cake.png',
)
red_berry_cake.add_component(raspberry, 1)
red_berry_cake.add_component(cherry, 2)
red_berry_cake.add_component(milk, 1)
red_berry_cake.add_component(egg, 1)
list_items.append(red_berry_cake)

cheesecake = hayday(
    name='cheesecake',
    production_place='cake oven',
    level=24,
    production_time=td(hours=4),
    price_sell=284,
    img='/assets/items/Cheesecake.png',
)
cheesecake.add_component(cheese, 1)
cheesecake.add_component(cookie, 1)
list_items.append(cheesecake)

strawberry_cake = hayday(
    name='strawberry  cake',
    production_place='cake oven',
    level=35,
    production_time=td(hours=3),
    price_sell=316,
    img='/assets/items/Strawberry_Cake.png',
)
strawberry_cake.add_component(wheat, 3)
strawberry_cake.add_component(cream, 1)
strawberry_cake.add_component(white_sugar, 1)
strawberry_cake.add_component(strawberry, 2)
list_items.append(strawberry_cake)

chocolate_cake = hayday(
    name='chocolate cake',
    production_place='cake oven',
    level=36,
    production_time=td(hours=2),
    price_sell=320,
    img='/assets/items/Chocolate_Cake.png',
)
chocolate_cake.add_component(cacao, 2)
chocolate_cake.add_component(brown_sugar, 1)
chocolate_cake.add_component(butter, 1)
list_items.append(chocolate_cake)

potato_feta_cake = hayday(
    name='potato feta cake',
    production_place='cake oven',
    level=38,
    production_time=td(hours=2),
    price_sell=309,
    img='/assets/items/Potato_Feta_Cake.png',
)
potato_feta_cake.add_component(potato, 1)
potato_feta_cake.add_component(egg, 4)
potato_feta_cake.add_component(goat_cheese, 1)
list_items.append(potato_feta_cake)

honey_apple_cake = hayday(
    name='honey apple cake',
    production_place='cake oven',
    level=42,
    production_time=td(hours=3, minutes=20),
    price_sell=482,
    img='/assets/items/Honey_Apple_Cake.png',
)
honey_apple_cake.add_component(wheat, 2)
honey_apple_cake.add_component(egg, 2)
honey_apple_cake.add_component(apple, 2)
honey_apple_cake.add_component(honey, 2)
list_items.append(honey_apple_cake)

fancy_cake = hayday(
    name='fancy cake',
    production_place='cake oven',
    level=54,
    production_time=td(minutes=15),
    price_sell=450,
    img='/assets/items/Fancy_Cake.png',
)
fancy_cake.add_component(cream_cake, 1)
fancy_cake.add_component(lily, 3)
fancy_cake.add_component(raspberry, 3)
fancy_cake.add_component(gold_ore, 1)
list_items.append(fancy_cake)

pineapple_cake = hayday(
    name='pineapple cake',
    production_place='cake oven',
    level=65,
    production_time=td(hours=1, minutes=15),
    price_sell=259,
    img='/assets/items/Pineapple_Cake.png',
)
pineapple_cake.add_component(pineapple, 3)
pineapple_cake.add_component(egg, 2)
pineapple_cake.add_component(cherry, 2)
pineapple_cake.add_component(wheat, 4)
list_items.append(pineapple_cake)

lemon_cake = hayday(
    name='lemon cake',
    production_place='cake oven',
    level=68,
    production_time=td(hours=2, minutes=30),
    price_sell=896,
    img='/assets/items/Lemon_Cake.png',
)
lemon_cake.add_component(lemon_curd, 2)
lemon_cake.add_component(egg, 2)
lemon_cake.add_component(cream, 1)
lemon_cake.add_component(wheat, 3)
list_items.append(lemon_cake)

fruit_cake = hayday(
    name='fruit cake',
    production_place='cake oven',
    level=89,
    production_time=td(hours=3),
    price_sell=450,
    img='/assets/items/Fruit_Cake.png',
)
fruit_cake.add_component(grapes, 2)
fruit_cake.add_component(orange, 2)
fruit_cake.add_component(cherry, 2)
fruit_cake.add_component(wheat, 3)

chocolate_roll = hayday(
    name='chocolate roll',
    production_place='cake oven',
    level=95,
    production_time=td(hours=1, minutes=30),
    price_sell=604,
    img='/assets/items/Chocolate_Roll.png',
)
chocolate_roll.add_component(cacao, 5)
chocolate_roll.add_component(cream, 1)
chocolate_roll.add_component(wheat, 3)
chocolate_roll.add_component(mint, 3)
list_items.append(chocolate_roll)

pomegranate_cake = hayday(
    name='pomegranate cake',
    production_place='cake oven',
    level=108,
    production_time=td(hours=2, minutes=40),
    price_sell=316,
    img='assets/items/Pomegranate_Cake.png',
)
pomegranate_cake.add_component(pomegranate, 1)
pomegranate_cake.add_component(egg, 2)
pomegranate_cake.add_component(cream, 2)
pomegranate_cake.add_component(wheat, 6)
list_items.append(pomegranate_cake)
