#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : bath_kiosk.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .sauce_maker import olive_oil
from .crops import lemon, cacao, coffee_bean, raspberry
from .dairy import goat_milk
from .animals import egg
from .honey_extractor import honey, honeycomb

lemon_lotion = hayday(
    name='lemon lotion',
    production_place='bath kiosk',
    level=84,
    production_time=td(hours=1, minutes=15),
    price_sell=403,
    img='/assets/items/Lemon_Lotion.png',
)
lemon_lotion.add_component(olive_oil, 1)
lemon_lotion.add_component(lemon, 1)
list_items.append(lemon_lotion)

honey_soap = hayday(
    name='honey soap',
    production_place='bath kiosk',
    level=84,
    production_time=td(hours=1),
    price_sell=327,
    img='/assets/items/Honey_Soap.png',
)
honey_soap.add_component(goat_milk, 1)
honey_soap.add_component(cacao, 2)
honey_soap.add_component(honeycomb, 1)
list_items.append(honey_soap)

exfoliating_soap = hayday(
    name='exfoliating soap',
    production_place='bath kiosk',
    level=93,
    production_time=td(hours=1),
    price_sell=363,
    img='/assets/items/Exfoliating_Soap.png',
)
exfoliating_soap.add_component(cacao, 2)
exfoliating_soap.add_component(coffee_bean, 2)
exfoliating_soap.add_component(raspberry, 1)
list_items.append(exfoliating_soap)

honey_face_mask = hayday(
    name='honey face mask',
    production_place='bath kiosk',
    level=99,
    production_time=td(hours=1, minutes=30),
    price_sell=320,
    img='/assets/items/Honey_Face_Mask.png',
)
honey_face_mask.add_component(egg, 2)
honey_face_mask.add_component(honey, 1)
honey_face_mask.add_component(lemon, 1)
list_items.append(honey_face_mask)
