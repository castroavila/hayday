#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : salad_bar.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    lettuce,
    olive,
    lemon,
    tomato,
    bell_pepper,
    carrot,
    cabbage,
    beetroot,
    chili_pepper,
    blackberry,
    orange,
    strawberry,
    onion,
    peach,
    mushroom,
    potato,
    pomegranate,
    chili_pepper,
)
from .bbq_grill import roasted_tomatoes
from .dairy import goat_cheese, cream, cheese
from .fish import fish_fillet, lobster_tail
from .animals import bacon
from .sauce_maker import mayonnaise, olive_oil
from .pasta_maker import fresh_pasta, rice_noodles
from .honey_extractor import honey

feta_salad = hayday(
    name='feta salad',
    production_place='salad bar',
    level=58,
    production_time=td(hours=1, minutes=30),
    price_sell=745,
    img='/assets/items/Feta_Salad.png',
)
feta_salad.add_component(lettuce, 3)
feta_salad.add_component(roasted_tomatoes, 1)
feta_salad.add_component(goat_cheese, 2)
feta_salad.add_component(olive, 2)
list_items.append(feta_salad)

blt_salad = hayday(
    name='BLT salad',
    production_place='salad bar',
    level=62,
    production_time=td(hours=1, minutes=45),
    price_sell=723,
    img='/assets/items/BLT_Salad.png',
)
blt_salad.add_component(lettuce, 3)
blt_salad.add_component(roasted_tomatoes, 1)
blt_salad.add_component(bacon, 2)
blt_salad.add_component(mayonnaise, 1)
list_items.append(blt_salad)

seafood_salad = hayday(
    name='seafood salad',
    production_place='salad bar',
    level=64,
    production_time=td(hours=2),
    price_sell=763,
    img='/assets/items/Seafood_Salad.png',
)
seafood_salad.add_component(lettuce, 3)
seafood_salad.add_component(fish_fillet, 1)
seafood_salad.add_component(lobster_tail, 1)
seafood_salad.add_component(mayonnaise, 1)
list_items.append(seafood_salad)

pasta_salad = hayday(
    name='pasta salad',
    production_place='salad bar',
    level=67,
    production_time=td(hours=2, minutes=30),
    price_sell=759,
    img='/assets/items/Pasta_Salad.png',
)
pasta_salad.add_component(fresh_pasta, 4)
pasta_salad.add_component(lemon, 2)
pasta_salad.add_component(olive_oil, 1)
pasta_salad.add_component(tomato, 2)
list_items.append(pasta_salad)

veggie_platter = hayday(
    name='veggie platter',
    production_place='salad bar',
    level=74,
    production_time=td(hours=2),
    price_sell=266,
    img='/assets/items/Veggie_Platter.png',
)
veggie_platter.add_component(bell_pepper, 2)
veggie_platter.add_component(carrot, 2)
veggie_platter.add_component(tomato, 2)
veggie_platter.add_component(cream, 1)
list_items.append(veggie_platter)

coleslaw = hayday(
    name='coleslaw',
    production_place='salad bar',
    level=75,
    production_time=td(hours=1, minutes=15),
    price_sell=468,
    img='/assets/items/Coleslaw.png',
)
coleslaw.add_component(cabbage, 3)
coleslaw.add_component(carrot, 2)
coleslaw.add_component(mayonnaise, 1)
list_items.append(coleslaw)

beetroot_salad = hayday(
    name='beetroot salad',
    production_place='salad bar',
    level=76,
    production_time=td(minutes=45),
    price_sell=234,
    img='/assets/items/Beetroot_Salad.png',
)
beetroot_salad.add_component(beetroot, 3)
beetroot_salad.add_component(goat_cheese, 1)
list_items.append(beetroot_salad)

summer_rolls = hayday(
    name='summer rolls',
    production_place='salad bar',
    level=78,
    production_time=td(hours=1),
    price_sell=316,
    img='/assets/items/Summer_Rolls.png',
)
summer_rolls.add_component(rice_noodles, 2)
summer_rolls.add_component(carrot, 2)
summer_rolls.add_component(lettuce, 1)
summer_rolls.add_component(chili_pepper, 1)
list_items.append(summer_rolls)

fruit_salad = hayday(
    name='fruit salad',
    production_place='salad bar',
    level=82,
    production_time=td(hours=2),
    price_sell=597,
    img='/assets/items/Fruit_Salad.png',
)
fruit_salad.add_component(blackberry, 2)
fruit_salad.add_component(honey, 1)
fruit_salad.add_component(orange, 1)
fruit_salad.add_component(strawberry, 3)
list_items.append(fruit_salad)


summer_salad = hayday(
    name='summer salad',
    production_place='salad bar',
    level=84,
    production_time=td(hours=3),
    price_sell=554,
    img='/assets/items/Summer_Salad.png',
)
summer_salad.add_component(goat_cheese, 1)
summer_salad.add_component(onion, 3)
summer_salad.add_component(peach, 1)
summer_salad.add_component(tomato, 3)
list_items.append(summer_salad)

mushroom_salad = hayday(
    name='mushroom salad',
    production_place='salad bar',
    level=89,
    production_time=td(hours=1),
    price_sell=216,
    img='/assets/items/Mushroom_Salad.png',
)
mushroom_salad.add_component(mushroom, 3)
mushroom_salad.add_component(lettuce, 1)
mushroom_salad.add_component(potato, 2)
mushroom_salad.add_component(bacon, 1)
list_items.append(mushroom_salad)

orange_salad = hayday(
    name='orange salad',
    production_place='salad bar',
    level=117,
    production_time=td(minutes=45),
    price_sell=558,
    img='/assets/items/Orange_Salad.png',
)
orange_salad.add_component(cheese, 1)
orange_salad.add_component(lettuce, 3)
orange_salad.add_component(pomegranate, 1)
orange_salad.add_component(orange, 2)
list_items.append(orange_salad)
