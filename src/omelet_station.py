#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : omelet_station.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .animals import egg
from .crops import carrot, bell_pepper, cabbage, asparagus, tomato, onion
from .dairy import cheese, butter

colourful_omelet = hayday(
    name='colourful omelet',
    production_place='omelet station',
    level=77,
    production_time=td(hours=1),
    price_sell=136,
    img='/assets/items/Colourful_Omelet.png',
)
colourful_omelet.add_component(egg, 2)
colourful_omelet.add_component(carrot, 2)
colourful_omelet.add_component(bell_pepper, 1)
colourful_omelet.add_component(cabbage, 1)
list_items.append(colourful_omelet)

spring_omelet = hayday(
    name='spring omelet',
    production_place='omelet station',
    level=77,
    production_time=td(minutes=40),
    price_sell=230,
    img='/assets/items/Spring_Omelet.png',
)
spring_omelet.add_component(egg, 2)
spring_omelet.add_component(asparagus, 2)
spring_omelet.add_component(butter, 1)
list_items.append(spring_omelet)

cheese_omelet = hayday(
    name='cheese omelet',
    production_place='omelet station',
    level=79,
    production_time=td(hours=1, minutes=30),
    price_sell=464,
    img='/assets/items/Cheese_Omelet.png',
)
cheese_omelet.add_component(egg, 3)
cheese_omelet.add_component(cheese, 2)
cheese_omelet.add_component(tomato, 2)
cheese_omelet.add_component(onion, 1)
list_items.append(cheese_omelet)
