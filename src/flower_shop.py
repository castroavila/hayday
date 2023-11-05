#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : flower_shop.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import (
    wheat,
    indigo,
    cotton,
    sunflower,
    lily,
    peony,
    broccoli,
    tomato,
    mushroom,
)
from .mine import iron_ore, gold_ore
from .loom import cotton_fabric
from .candine_machine import caramel_apple, toffee
from .juice_press import cherry_juice

rustic_bouquet = hayday(
    name='rustic bouquet',
    production_place='flower shop',
    level=49,
    production_time=td(minutes=45),
    price_sell=208,
    img='/assets/items/Rustic_Bouquet.png',
)
rustic_bouquet.add_component(wheat, 5)
rustic_bouquet.add_component(indigo, 3)
rustic_bouquet.add_component(cotton, 3)
list_items.append(rustic_bouquet)

bright_bouquet = hayday(
    name='brigth bouquet',
    production_place='flower shop',
    level=65,
    production_time=td(minutes=20),
    price_sell=338,
    img='/assets/items/Bright_Bouquet.png',
)
bright_bouquet.add_component(sunflower, 5)
bright_bouquet.add_component(indigo, 3)
bright_bouquet.add_component(cotton, 1)
bright_bouquet.add_component(iron_ore, 5)
list_items.append(bright_bouquet)

gracious_bouquet = hayday(
    name='gracious bouquet',
    production_place='flower shop',
    level=73,
    production_time=td(minutes=40),
    price_sell=500,
    img='/assets/items/Gracious_Bouquet.png',
)
gracious_bouquet.add_component(cotton_fabric, 1)
gracious_bouquet.add_component(lily, 5)
gracious_bouquet.add_component(gold_ore, 1)
# bright_bouquet.add_component(diamond, 5)
list_items.append(gracious_bouquet)

candy_bouquet = hayday(
    name='candy bouquet',
    production_place='flower shop',
    level=90,
    production_time=td(minutes=20),
    price_sell=554,
    img='/assets/items/Candy_Bouquet.png',
)
candy_bouquet.add_component(peony, 3)
candy_bouquet.add_component(caramel_apple, 1)
candy_bouquet.add_component(toffee, 1)
list_items.append(candy_bouquet)

birthday_bouquet = hayday(
    name='birthday bouquet',
    production_place='flower shop',
    level=92,
    production_time=td(minutes=20),
    price_sell=349,
    img='/assets/items/Birthday_Bouquet.png',
)
birthday_bouquet.add_component(cherry_juice, 1)
birthday_bouquet.add_component(peony, 3)
birthday_bouquet.add_component(lily, 1)
birthday_bouquet.add_component(indigo, 1)
list_items.append(birthday_bouquet)

soft_bouquet = hayday(
    name='soft bouquet',
    production_place='flower shop',
    level=93,
    production_time=td(minutes=30),
    price_sell=298,
    img='/assets/items/Soft_Bouquet.png',
)
soft_bouquet.add_component(peony, 4)
soft_bouquet.add_component(cotton, 1)
soft_bouquet.add_component(cotton_fabric, 1)
list_items.append(soft_bouquet)

veggie_bouquet = hayday(
    name='veggie bouquet',
    production_place='flower shop',
    level=106,
    production_time=td(minutes=15),
    price_sell=352,
    img='/assets/items/Veggie_Bouquet.png',
)
veggie_bouquet.add_component(broccoli, 3)
veggie_bouquet.add_component(tomato, 3)
veggie_bouquet.add_component(mushroom, 3)
veggie_bouquet.add_component(cotton_fabric, 1)
list_items.append(veggie_bouquet)
