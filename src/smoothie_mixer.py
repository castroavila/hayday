#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : smoothie_mixer.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    raspberry,
    strawberry,
    blackberry,
    lettuce,
    lemon,
    apple,
    cherry,
    sesame,
    banana,
    cacao,
    cucumber,
    pineapple,
    lemon,
    orange,
    peach,
    plum,
    grapes,
    mint,
    coconut,
    passion_fruit,
    banana,
    mango,
)
from .dairy import cream, goat_milk, milk
from .sugar_mill import white_sugar
from .honey_extractor import honey

berry_smoothie = hayday(
    name='berry smoothie',
    production_place='smoothie mixer',
    level=64,
    production_time=td(hours=1, minutes=15),
    price_sell=547,
    img='/assets/items/Berry_Smoothie.png',
)
berry_smoothie.add_component(raspberry, 3)
berry_smoothie.add_component(strawberry, 3)
berry_smoothie.add_component(blackberry, 3)
list_items.append(berry_smoothie)

green_smoothie = hayday(
    name='green smoothie',
    production_place='smoothie mixer',
    level=66,
    production_time=td(minutes=45),
    price_sell=320,
    img='/assets/items/Green_Smoothie.png',
)
green_smoothie.add_component(lettuce, 5)
green_smoothie.add_component(lemon, 1)
green_smoothie.add_component(apple, 1)
list_items.append(green_smoothie)

yogurt_smoothie = hayday(
    name='yogurt smoothie',
    production_place='smoothie mixer',
    level=70,
    production_time=td(hours=1),
    price_sell=349,
    img='/assets/items/Yogurt_Smoothie.png',
)
yogurt_smoothie.add_component(cream, 1)
yogurt_smoothie.add_component(raspberry, 2)
yogurt_smoothie.add_component(cherry, 1)
yogurt_smoothie.add_component(white_sugar, 1)
list_items.append(yogurt_smoothie)

cucumber_smoothie = hayday(
    name='cucumber smoothie',
    production_place='smoothie mixer',
    level=70,
    production_time=td(minutes=40),
    price_sell=266,
    img='/assets/items/Cucumber_Smoothie.png',
)
cucumber_smoothie.add_component(cucumber, 3)
cucumber_smoothie.add_component(honey, 1)
cucumber_smoothie.add_component(pineapple, 3)
list_items.append(cucumber_smoothie)

mixed_smoothie = hayday(
    name='mixed smoothie',
    production_place='smoothie mixer',
    level=88,
    production_time=td(minutes=30),
    price_sell=504,
    img='/assets/items/Mixed_Smoothie.png',
)
mixed_smoothie.add_component(lemon, 1)
mixed_smoothie.add_component(orange, 2)
mixed_smoothie.add_component(peach, 2)
list_items.append(mixed_smoothie)

black_sesame_smoothie = hayday(
    name='black sesame smoothie',
    production_place='smoothie mixer',
    level=93,
    production_time=td(minutes=45),
    price_sell=313,
    img='/assets/items/Black_Sesame_Smoothie.png',
)
black_sesame_smoothie.add_component(sesame, 3)
black_sesame_smoothie.add_component(banana, 1)
black_sesame_smoothie.add_component(goat_milk, 2)
list_items.append(black_sesame_smoothie)

cocoa_smoothie = hayday(
    name='cocoa smoothie',
    production_place='smoothie mixer',
    level=100,
    production_time=td(minutes=40),
    price_sell=511,
    img='/assets/items/Cocoa_Smoothie.png',
)
cocoa_smoothie.add_component(banana, 2)
cocoa_smoothie.add_component(cacao, 3)
cocoa_smoothie.add_component(milk, 1)
list_items.append(cocoa_smoothie)

plum_smoothie = hayday(
    name='plum smoothie',
    production_place='smoothie mixer',
    level=102,
    production_time=td(minutes=35),
    price_sell=522,
    img='/assets/items/Plum_Smoothie.png',
)
plum_smoothie.add_component(plum, 3)
plum_smoothie.add_component(grapes, 2)
plum_smoothie.add_component(mint, 1)
plum_smoothie.add_component(honey, 1)
list_items.append(plum_smoothie)

tropical_smoothie = hayday(
    name='tropical smoothie',
    production_place='smoothie mixer',
    level=104,
    production_time=td(minutes=40),
    price_sell=475,
    img='/assets/items/Tropical_Smoothie.png',
)
tropical_smoothie.add_component(coconut, 1)
tropical_smoothie.add_component(banana, 1)
tropical_smoothie.add_component(passion_fruit, 2)
tropical_smoothie.add_component(mango, 2)
list_items.append(tropical_smoothie)
