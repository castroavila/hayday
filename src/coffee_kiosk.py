#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : coffee_kiosk.py
# @created          : 29-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .hayday import hayday
from .main import list_items
from .crops import coffee_bean, cacao, raspberry, banana
from .sugar_mill import white_sugar
from .dairy import cream, milk
from .candy_machine import toffee

espresso = hayday(
    name='espresso',
    production_place='coffee kiosk',
    level=42,
    production_time=td(minutes=5),
    price_sell=248,
    img='/assets/items/Espresso.png',
)
espresso.add_component(coffee_bean, 3)
espresso.add_component(white_sugar, 1)
list_items.append(espresso)

caffe_latte = hayday(
    name='caffe latte',
    production_place='coffee kiosk',
    level=43,
    production_time=td(minutes=10),
    price_sell=219,
    img='/assets/items/Caffe_Latte.png',
)
caffe_latte.add_component(coffee_bean, 2)
caffe_latte.add_component(white_sugar, 1)
caffe_latte.add_component(milk, 1)
list_items.append(caffe_latte)

caffe_mocha = hayday(
    name='caffe mocha',
    production_place='coffee kiosk',
    level=45,
    production_time=td(minutes=15),
    price_sell=291,
    img='/assets/items/Caffe_Mocha.png',
)
caffe_mocha.add_component(coffee_bean, 1)
caffe_mocha.add_component(cream, 1)
caffe_mocha.add_component(cacao, 2)
list_items.append(caffe_mocha)

raspberry_mocha = hayday(
    name='raspberry mocha',
    production_place='coffee kiosk',
    level=46,
    production_time=td(minutes=30),
    price_sell=259,
    img='/assets/items/Raspberry_Mocha.png',
)
raspberry_mocha.add_component(coffee_bean, 1)
raspberry_mocha.add_component(cream, 1)
raspberry_mocha.add_component(cacao, 1)
raspberry_mocha.add_component(raspberry, 1)
list_items.append(raspberry_mocha)

hot_chocolate = hayday(
    name='hot chocolate',
    production_place='coffee kiosk',
    level=47,
    production_time=td(minutes=25),
    price_sell=316,
    img='/assets/items/Hot_Chocolate.png',
)
hot_chocolate.add_component(cacao, 2)
hot_chocolate.add_component(white_sugar, 1)
hot_chocolate.add_component(cream, 1)
hot_chocolate.add_component(milk, 1)
list_items.append(hot_chocolate)

caramel_latte = hayday(
    name='caramel latte',
    production_place='coffee kiosk',
    level=62,
    production_time=td(minutes=15),
    price_sell=345,
    img='/assets/items/Caramel_Latte.png',
)
caramel_latte.add_component(coffee_bean, 2)
caramel_latte.add_component(toffee, 1)
caramel_latte.add_component(milk, 1)
list_items.append(caramel_latte)

iced_banana_latte = hayday(
    name='iced banana latte',
    production_place='coffee kiosk',
    level=88,
    production_time=td(minutes=20),
    price_sell=277,
    img='/assets/items/Iced_Banana_Latte.png',
)
iced_banana_latte.add_component(banana, 1)
iced_banana_latte.add_component(coffee_bean, 2)
iced_banana_latte.add_component(milk, 1)
list_items.append(iced_banana_latte)

caramel_latte = hayday(
    name='caramel latte',
    production_place='coffee kiosk',
    level=62,
    production_time=td(minutes=15),
    price_sell=345,
    img='/assets/items/Caramel_Latte.png',
)
caramel_latte.add_component(coffee_bean, 2)
caramel_latte.add_component(toffee, 1)
caramel_latte.add_component(milk, 1)
list_items.append(caramel_latte)
