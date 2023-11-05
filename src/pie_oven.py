#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : pie_oven.py
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
    pumpkin,
    apple,
    potato,
    wheat,
    cacao,
    peach,
    passion_fruit,
    mushroom,
    cabbage,
    eggplant,
    asparagus,
)
from .animals import egg, bacon, peanuts
from .sugar_mill import syrup
from .fish import fish_fillet
from .dairy import goat_cheese, cheese, cream
from .sauce_maker import lemon_curd, tomato_sauce

carrot_pie = hayday(
    name='carrot pie',
    production_place='pie oven',
    level=14,
    production_time=td(hours=1),
    price_sell=82,
    img='/assets/items/Carrot_Pie.png',
)
carrot_pie.add_component(carrot, 3)
carrot_pie.add_component(wheat, 2)
carrot_pie.add_component(egg, 1)
list_items.append(carrot_pie)

pumpkin_pie = hayday(
    name='pumpkin pie',
    production_place='pie oven',
    level=15,
    production_time=td(hours=2),
    price_sell=158,
    img='/assets/items/Pumpkin_Pie.png',
)
pumpkin_pie.add_component(pumpkin, 3)
pumpkin_pie.add_component(wheat, 2)
pumpkin_pie.add_component(egg, 1)
list_items.append(pumpkin_pie)

bacon_pie = hayday(
    name='bacon pie',
    production_place='pie oven',
    level=18,
    production_time=td(hours=3),
    price_sell=219,
    img='/assets/items/Bacon_Pie.png',
)
bacon_pie.add_component(bacon, 3)
bacon_pie.add_component(wheat, 2)
bacon_pie.add_component(egg, 1)
list_items.append(bacon_pie)

apple_pie = hayday(
    name='apple pie',
    production_place='pie oven',
    level=28,
    production_time=td(hours=2, minutes=30),
    price_sell=270,
    img='/assets/items/Apple_Pie.png',
)
apple_pie.add_component(apple, 3)
apple_pie.add_component(wheat, 2)
apple_pie.add_component(egg, 1)
apple_pie.add_component(syrup, 1)
list_items.append(apple_pie)

fish_pie = hayday(
    name='fish pie',
    production_place='pie oven',
    level=28,
    production_time=td(hours=2),
    price_sell=226,
    img='/assets/items/Fish_Pie.png',
)
fish_pie.add_component(fish_fillet, 3)
fish_pie.add_component(wheat, 2)
fish_pie.add_component(egg, 1)
list_items.append(fish_pie)

feta_pie = hayday(
    name='feta pie',
    production_place='pie oven',
    level=34,
    production_time=td(hours=1, minutes=30),
    price_sell=223,
    img='/assets/items/Feta_Pie.png',
)
feta_pie.add_component(goat_cheese, 1)
feta_pie.add_component(wheat, 2)
feta_pie.add_component(egg, 1)
list_items.append(feta_pie)

casserole = hayday(
    name='casserole',
    production_place='pie oven',
    level=36,
    production_time=td(hours=2),
    price_sell=367,
    img='/assets/items/Casserole.png',
)
casserole.add_component(potato, 2)
casserole.add_component(bacon, 2)
casserole.add_component(egg, 2)
casserole.add_component(cheese, 1)
list_items.append(casserole)

shepherds_pie = hayday(
    name='shepherds pie',
    production_place='pie oven',
    level=39,
    production_time=td(hours=1, minutes=40),
    price_sell=280,
    img='/assets/items/Shepherds_Pie.png',
)
shepherds_pie.add_component(potato, 2)
shepherds_pie.add_component(bacon, 2)
shepherds_pie.add_component(carrot, 2)
shepherds_pie.add_component(pumpkin, 2)
list_items.append(shepherds_pie)

chocolate_pie = hayday(
    name='chocolate pie',
    production_place='pie oven',
    level=65,
    production_time=td(hours=1, minutes=15),
    price_sell=514,
    img='/assets/items/Chocolate_Pie.png',
)
chocolate_pie.add_component(wheat, 3)
chocolate_pie.add_component(cacao, 2)
chocolate_pie.add_component(egg, 1)
chocolate_pie.add_component(peanuts, 1)
list_items.append(chocolate_pie)

lemon_pie = hayday(
    name='lemon pie',
    production_place='pie oven',
    level=67,
    production_time=td(hours=2, minutes=15),
    price_sell=446,
    img='/assets/items/Lemon_Pie.png',
)
lemon_pie.add_component(lemon_curd, 1)
lemon_pie.add_component(wheat, 2)
lemon_pie.add_component(egg, 1)
list_items.append(lemon_pie)

peach_tart = hayday(
    name='peach tart',
    production_place='pie oven',
    level=76,
    production_time=td(hours=2, minutes=30),
    price_sell=435,
    img='/assets/items/Peach_Tart.png',
)
peach_tart.add_component(cream, 1)
peach_tart.add_component(egg, 2)
peach_tart.add_component(peach, 3)
peach_tart.add_component(wheat, 2)
list_items.append(peach_tart)

passion_fruit_pie = hayday(
    name='passion fruit pie',
    production_place='pie oven',
    level=92,
    production_time=td(minutes=50),
    price_sell=111,
    img='/assets/items/Passion_Fruit_Pie.png',
)
passion_fruit_pie.add_component(passion_fruit, 3)
passion_fruit_pie.add_component(wheat, 1)
passion_fruit_pie.add_component(egg, 2)
list_items.append(passion_fruit_pie)

mushroom_pot_pie = hayday(
    name='mushroom pot pie',
    production_place='pie oven',
    level=97,
    production_time=td(hours=1),
    price_sell=162,
    img='/assets/items/Mushroom_Pot_Pie.png',
)
mushroom_pot_pie.add_component(mushroom, 3)
mushroom_pot_pie.add_component(cabbage, 3)
mushroom_pot_pie.add_component(wheat, 3)
mushroom_pot_pie.add_component(egg, 2)
list_items.append(mushroom_pot_pie)

eggplant_parmesan = hayday(
    name='eggplant parmesan',
    production_place='pie oven',
    level=99,
    production_time=td(minutes=45),
    price_sell=442,
    img='/assets/items/Eggplant_Parmesan.png',
)
eggplant_parmesan.add_component(eggplant, 4)
eggplant_parmesan.add_component(cheese, 1)
eggplant_parmesan.add_component(tomato_sauce, 1)
list_items.append(eggplant_parmesan)

asparagus_quiche = hayday(
    name='asparagus quiche',
    production_place='pie oven',
    level=49,
    production_time=td(hours=2),
    price_sell=302,
    img='/assets/items/Asparagus_Quiche.png',
)
asparagus_quiche.add_component(asparagus, 2)
asparagus_quiche.add_component(egg, 2)
asparagus_quiche.add_component(cheese, 1)
asparagus_quiche.add_component(wheat, 4)
list_items.append(asparagus_quiche)
