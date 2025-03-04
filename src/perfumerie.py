#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @author	   : Manuel Castro Avila <castroavila@ic.unicamp.br>
# @file	   	   : perfumerie.py
# @created	   : 04-Mar-2025
# @company 	   : Institute of Computing - UNICAMP - Campinas - Brazil

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday
from .essential_oils_lab import (
    ginger_essential_oil,
    mint_essential_oil,
    lemon_essential_oil,
    chamomile_essential_oil,
)
from .crops import ginger, indigo

fresh_diffuser = hayday(
    name='fresh diffuser',
    production_place='perfumerie',
    level=110,
    production_time=td(minutes=20),
    price_sell=349,
    img='assets/items/Fresh_Diffuser.png',
)
fresh_diffuser.add_component(ginger_essential_oil, 1)
fresh_diffuser.add_component(mint_essential_oil, 1)
list_items.append(fresh_diffuser)

zesty_perfume = hayday(
    name='zesty perfume',
    production_place='perfumerie',
    level=113,
    production_time=td(minutes=15),
    price_sell=388,
    img='assets/items/Zesty_Perfume.png',
)
zesty_perfume.add_component(lemon_essential_oil, 1)
zesty_perfume.add_component(ginger, 3)
list_items.append(zesty_perfume)

calming_diffuser = hayday(
    name='calming diffuser',
    production_place='perfumerie',
    level=116,
    production_time=td(minutes=25),
    price_sell=169,
    img='assets/items/Calming_Diffuser.png',
)
calming_diffuser.add_component(chamomile_essential_oil, 1)
calming_diffuser.add_component(indigo, 3)
list_items.append(calming_diffuser)
