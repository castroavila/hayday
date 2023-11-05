#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : wok_kitchen.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    rice,
    chili_pepper,
    garlic,
    ginger,
    soybean,
    onion,
    broccoli,
    sesame,
)
from .animals import egg, peanuts
from .fish import fish_fillet
from .sauce_maker import olive_oil, soy_sauce
from .pasta_maker import rice_noodles

fried_rice = hayday(
    name='fried rice',
    production_place='wok kitchen',
    level=69,
    production_time=td(hours=1),
    price_sell=205,
    img='/assets/items/Fried_Rice.png',
)
fried_rice.add_component(rice, 5)
fried_rice.add_component(egg, 5)
list_items.append(fried_rice)

spicy_fish = hayday(
    name='spicy fish',
    production_place='wok kitchen',
    level=79,
    production_time=td(hours=1, minutes=30),
    price_sell=543,
    img='/assets/items/Spicy_Fish.png',
)
spicy_fish.add_component(fish_fillet, 1)
spicy_fish.add_component(chili_pepper, 3)
spicy_fish.add_component(garlic, 5)
spicy_fish.add_component(olive_oil, 1)
list_items.append(spicy_fish)

peanut_noodles = hayday(
    name='peanut noodles',
    production_place='wok kitchen',
    level=86,
    production_time=td(minutes=45),
    price_sell=597,
    img='/assets/items/Peanut_Noodles.png',
)
peanut_noodles.add_component(ginger, 1)
peanut_noodles.add_component(rice_noodles, 1)
peanut_noodles.add_component(soy_sauce, 1)
peanut_noodles.add_component(peanuts, 1)
list_items.append(peanut_noodles)

tofu_stir_fry = hayday(
    name='tofu stir fry',
    production_place='wok kitchen',
    level=89,
    production_time=td(hours=1, minutes=15),
    price_sell=306,
    img='/assets/items/Tofu_Stir_Fry.png',
)
tofu_stir_fry.add_component(soybean, 3)
tofu_stir_fry.add_component(onion, 3)
tofu_stir_fry.add_component(broccoli, 3)
tofu_stir_fry.add_component(sesame, 3)
list_items.append(tofu_stir_fry)
