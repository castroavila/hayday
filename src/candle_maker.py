#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : candle_maker.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .honey_extractor import beeswax
from .crops import (
    strawberry,
    raspberry,
    lemon,
    carrot,
    peony,
    sunflower,
    indigo,
)

strawberry_candle = hayday(
    name='strawberry candle',
    production_place='candle maker',
    level=48,
    production_time=td(hours=2),
    price_sell=370,
    img='/assets/items/Strawberry_Candle.png',
)

strawberry_candle.add_component(beeswax, 1)
strawberry_candle.add_component(strawberry, 2)
list_items.append(strawberry_candle)

raspberry_candle = hayday(
    name='raspberry candle',
    production_place='candle maker',
    level=52,
    production_time=td(hours=1, minutes=45),
    price_sell=360,
    img='/assets/items/Raspberry_Candle.png',
)

raspberry_candle.add_component(beeswax, 1)
raspberry_candle.add_component(raspberry, 2)
list_items.append(raspberry_candle)

lemon_candle = hayday(
    name='lemon candle',
    production_place='candle maker',
    level=72,
    production_time=td(hours=2, minutes=15),
    price_sell=457,
    img='/assets/items/Lemon_Candle.png',
)

lemon_candle.add_component(beeswax, 1)
lemon_candle.add_component(lemon, 2)
list_items.append(lemon_candle)

colorful_candles = hayday(
    name='colorful candles',
    production_place='candle maker',
    level=84,
    production_time=td(hours=1, minutes=50),
    price_sell=324,
    img='/assets/items/Party_Candles.png',
)

colorful_candles.add_component(beeswax, 1)
colorful_candles.add_component(strawberry, 1)
colorful_candles.add_component(carrot, 1)
list_items.append(colorful_candles)

floral_candle = hayday(
    name='floral candle',
    production_place='candle maker',
    level=95,
    production_time=td(hours=2),
    price_sell=442,
    img='/assets/items/Floral_Candle.png',
)

floral_candle.add_component(beeswax, 1)
floral_candle.add_component(peony, 2)
floral_candle.add_component(sunflower, 2)
floral_candle.add_component(indigo, 2)
list_items.append(floral_candle)
