#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : milkshake_bar.py
# @created          : 25-Feb-2024
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .ice_cream_maker import (
    vanilla_ice_cream,
    chocolate_ice_cream,
    peach_ice_cream,
)
from .bakery import cookie
from .candy_machine import toffee
from .sugar_mill import syrup
from .coffee_kiosk import espresso
from .crops import orange, lemon

vanilla_milkshake = hayday(
    name='vanilla milkshake',
    production_place='milkshake bar',
    level=124,
    production_time=td(minutes=45),
    price_sell=673,
    img='/assets/items/Vanilla_Milkshake.png',
)
vanilla_milkshake.add_component(vanilla_ice_cream, 1)
vanilla_milkshake.add_component(cookie, 2)
vanilla_milkshake.add_component(toffee, 1)
vanilla_milkshake.add_component(syrup, 1)
list_items.append(vanilla_milkshake)

mocha_milkshake = hayday(
    name='mocha milkshake',
    production_place='milkshake bar',
    level=125,
    production_time=td(minutes=30),
    price_sell=856,
    img='/assets/items/Mocha_Milkshake.png',
)
mocha_milkshake.add_component(chocolate_ice_cream, 1)
mocha_milkshake.add_component(espresso, 2)
list_items.append(mocha_milkshake)

fruity_milkshake = hayday(
    name='fruity milkshake',
    production_place='milkshake bar',
    level=126,
    production_time=td(minutes=35),
    price_sell=759,
    img='/assets/items/Fruity_Milkshake.png',
)
fruity_milkshake.add_component(peach_ice_cream, 1)
fruity_milkshake.add_component(orange, 2)
fruity_milkshake.add_component(lemon, 1)
list_items.append(fruity_milkshake)
