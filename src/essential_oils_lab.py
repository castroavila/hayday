#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @author	   : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file	   	   : essential_oils_lab.py
# @created	   : 24-Nov-2024
# @company 	   : Home

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import lemon, chamomile, ginger, mint

lemon_essential_oil = hayday(
    name='lemon essential oil',
    production_place='essential oils lab',
    level=68,
    production_time=td(minutes=10),
    price_sell=288,
    img='/assets/items/Lemon_Essential_Oil.png',
)
lemon_essential_oil.add_component(lemon, 3)
list_items.append(lemon_essential_oil)

chamomile_essential_oil = hayday(
    name='chamomile essential oil',
    production_place='essential oils lab',
    level=74,
    production_time=td(minutes=10),
    price_sell=72,
    img='/assets/items/Chamomile_Essential_Oil.png',
)
chamomile_essential_oil.add_component(chamomile, 5)
list_items.append(chamomile_essential_oil)

ginger_essential_oil = hayday(
    name='ginger essential oil',
    production_place='essential oils lab',
    level=80,
    production_time=td(minutes=20),
    price_sell=162,
    img='/assets/items/Ginger_Essential_Oil.png',
)
ginger_essential_oil.add_component(ginger, 5)
list_items.append(ginger_essential_oil)

mint_essential_oil = hayday(
    name='mint essential oil',
    production_place='essential oils lab',
    level=85,
    production_time=td(minutes=15),
    price_sell=172,
    img='/assets/items/Mint_Essential_Oil.png',
)
mint_essential_oil.add_component(mint, 5)
list_items.append(mint_essential_oil)
