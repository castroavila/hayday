#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : crops.py
# @created          : 25-Oct-2023
# @company          : Home
#

"""

"""
from datetime import timedelta as td
from .main import list_items
from .hayday import hayday


wheat = hayday(
    name='wheat',
    production_place='farm',
    level=1,
    production_time=td(minutes=2),
    price_sell=3,
    img='/assets/items/Wheat.png',
)
list_items.append(wheat)

corn = hayday(
    name='corn',
    production_place='farm',
    level=2,
    production_time=td(minutes=5),
    price_sell=7,
    img='/assets/items/Corn.png',
)
list_items.append(corn)

soybean = hayday(
    name='soybean',
    production_place='farm',
    level=5,
    production_time=td(minutes=20),
    price_sell=10,
    img='/assets/items/Soybean.png',
)
list_items.append(soybean)

sugarcane = hayday(
    name='sugarcane',
    production_place='farm',
    level=7,
    production_time=td(minutes=30),
    price_sell=14,
    img='/assets/items/Sugarcane.png',
)
list_items.append(sugarcane)

carrot = hayday(
    name='carrot',
    production_place='farm',
    level=9,
    production_time=td(minutes=10),
    price_sell=7,
    img='/assets/items/Carrot.png',
)
list_items.append(carrot)

indigo = hayday(
    name='indigo',
    production_place='farm',
    level=13,
    production_time=td(hours=2),
    price_sell=25,
    img='/assets/items/Indigo.png',
)
list_items.append(indigo)

apple = hayday(
    name='apple',
    production_place='farm',
    level=15,
    production_time=td(hours=16),
    price_sell=39,
    img='/assets/items/Apple.png',
)
list_items.append(apple)

pumpkin = hayday(
    name='pumpkin',
    production_place='farm',
    level=15,
    production_time=td(hours=3),
    price_sell=32,
    img='/assets/items/Pumpkin.png',
)
list_items.append(pumpkin)

cotton = hayday(
    name='cotton',
    production_place='farm',
    level=18,
    production_time=td(hours=2, minutes=30),
    price_sell=28,
    img='/assets/items/Cotton.png',
)
list_items.append(cotton)

raspberry = hayday(
    name='raspberry',
    production_place='farm',
    level=19,
    production_time=td(hours=18),
    price_sell=46,
    img='/assets/items/Raspberry.png',
)
list_items.append(raspberry)

cherry = hayday(
    name='cherry',
    production_place='farm',
    level=22,
    production_time=td(days=1, hours=3),
    price_sell=68,
    img='/assets/items/Cherry.png',
)
list_items.append(cherry)

chili_pepper = hayday(
    name='chili pepper',
    production_place='farm',
    level=25,
    production_time=td(hours=4),
    price_sell=36,
    img='/assets/items/Chili_Pepper.png',
)
list_items.append(chili_pepper)

blackberry = hayday(
    name='blackberry',
    production_place='farm',
    level=26,
    production_time=td(days=1, hours=8),
    price_sell=82,
    img='/assets/items/Blackberry.png',
)
list_items.append(blackberry)

tomato = hayday(
    name='tomato',
    production_place='farm',
    level=30,
    production_time=td(hours=6),
    price_sell=43,
    img='/assets/items/Tomato.png',
)
list_items.append(tomato)

strawberry = hayday(
    name='strawberry',
    production_place='farm',
    level=34,
    production_time=td(hours=8),
    price_sell=50,
    img='/assets/items/Strawberry.png',
)
list_items.append(strawberry)

potato = hayday(
    name='potato',
    production_place='farm',
    level=35,
    production_time=td(hours=3, minutes=40),
    price_sell=36,
    img='/assets/items/Potato.png',
)
list_items.append(potato)

cacao = hayday(
    name='cacao',
    production_place='farm',
    level=36,
    production_time=td(days=1, hours=11),
    price_sell=86,
    img='/assets/items/Cacao.png',
)
list_items.append(cacao)

coffee_bean = hayday(
    name='coffee bean',
    production_place='farm',
    level=42,
    production_time=td(days=1, hours=1),
    price_sell=64,
    img='/assets/items/Coffee_Bean.png',
)
list_items.append(coffee_bean)

sesame = hayday(
    name='sasame',
    production_place='farm',
    level=50,
    production_time=td(hours=1),
    price_sell=18,
    img='/assets/items/Sesame.png',
)
list_items.append(sesame)

pineapple = hayday(
    name='pineapple',
    production_place='farm',
    level=52,
    production_time=td(minutes=30),
    price_sell=14,
    img='/assets/items/Pineapple.png',
)
list_items.append(pineapple)

lily = hayday(
    name='lily',
    production_place='farm',
    level=53,
    production_time=td(hours=1, minutes=30),
    price_sell=21,
    img='/assets/items/Lily.png',
)
list_items.append(lily)

rice = hayday(
    name='rice',
    production_place='farm',
    level=56,
    production_time=td(minutes=45),
    price_sell=18,
    img='/assets/items/Rice.png',
)
list_items.append(rice)

olive = hayday(
    name='olive',
    production_place='farm',
    level=57,
    production_time=td(hours=24),
    price_sell=82,
    img='/assets/items/Olive.png',
)
list_items.append(olive)

lettuce = hayday(
    name='lettuce',
    production_place='farm',
    level=58,
    production_time=td(hours=3, minutes=30),
    price_sell=32,
    img='/assets/items/Lettuce.png',
)
list_items.append(lettuce)

garlic = hayday(
    name='garlic',
    production_place='farm',
    level=60,
    production_time=td(minutes=30),
    price_sell=14,
    img='/assets/items/Garlic.png',
)
list_items.append(garlic)

sunflower = hayday(
    name='sunflower',
    production_place='farm',
    level=63,
    production_time=td(hours=1, minutes=30),
    price_sell=21,
    img='/assets/items/Sunflower.png',
)
list_items.append(sunflower)

cabbage = hayday(
    name='cabbage',
    production_place='farm',
    level=65,
    production_time=td(minutes=45),
    price_sell=18,
    img='/assets/items/Cabbage.png',
)
list_items.append(cabbage)

lemon = hayday(
    name='lemon',
    production_place='farm',
    level=66,
    production_time=td(days=1, hours=5),
    price_sell=93,
    img='/assets/items/Lemon.png',
)
list_items.append(lemon)

onion = hayday(
    name='onion',
    production_place='farm',
    level=68,
    production_time=td(hours=5),
    price_sell=39,
    img='/assets/items/Onion.png',
)
list_items.append(onion)

cucumber = hayday(
    name='cucumber',
    production_place='farm',
    level=70,
    production_time=td(minutes=35),
    price_sell=14,
    img='/assets/items/Cucumber.png',
)
list_items.append(cucumber)

orange = hayday(
    name='orange',
    production_place='farm',
    level=71,
    production_time=td(days=1, hours=7),
    price_sell=97,
    img='/assets/items/Orange.png',
)
list_items.append(orange)

beetroot = hayday(
    name='beetroot',
    production_place='farm',
    level=72,
    production_time=td(minutes=40),
    price_sell=14,
    img='/assets/items/Beetroot.png',
)
list_items.append(beetroot)

peach = hayday(
    name='peach',
    production_place='farm',
    level=76,
    production_time=td(days=1, hours=6),
    price_sell=100,
    img='/assets/items/Peach.png',
)
list_items.append(peach)

ginger = hayday(
    name='ginger',
    production_place='farm',
    level=78,
    production_time=td(hours=2, minutes=30),
    price_sell=28,
    img='/assets/items/Ginger.png',
)
list_items.append(ginger)

bell_pepper = hayday(
    name='bell pepper',
    production_place='farm',
    level=74,
    production_time=td(hours=4, minutes=30),
    price_sell=36,
    img='/assets/items/Bell_Pepper.png',
)
list_items.append(bell_pepper)

tea_leaf = hayday(
    name='tea leaf',
    production_place='farm',
    level=80,
    production_time=td(hours=6, minutes=30),
    price_sell=43,
    img='/assets/items/Tea_Leaf.png',
)
list_items.append(tea_leaf)

peony = hayday(
    name='peony',
    production_place='farm',
    level=82,
    production_time=td(hours=4),
    price_sell=36,
    img='/assets/items/Peony.png',
)
list_items.append(peony)

broccoli = hayday(
    name='broccoli',
    production_place='farm',
    level=83,
    production_time=td(hours=1, minutes=20),
    price_sell=21,
    img='/assets/items/Broccoli.png',
)
list_items.append(broccoli)

grapes = hayday(
    name='grapes',
    production_place='farm',
    level=84,
    production_time=td(hours=3),
    price_sell=32,
    img='/assets/items/Grapes.png',
)
list_items.append(grapes)

mint = hayday(
    name='mint',
    production_place='farm',
    level=85,
    production_time=td(hours=3),
    price_sell=32,
    img='/assets/items/Mint.png',
)
list_items.append(mint)

banana = hayday(
    name='banana',
    production_place='farm',
    level=88,
    production_time=td(hours=27),
    price_sell=104,
    img='/assets/items/Banana.png',
)
list_items.append(banana)

passion_fruit = hayday(
    name='passion fruit',
    production_place='farm',
    level=88,
    production_time=td(hours=1),
    price_sell=18,
    img='/assets/items/Passion_Fruit.png',
)
list_items.append(passion_fruit)

mushroom = hayday(
    name='mushroom',
    production_place='farm',
    level=89,
    production_time=td(minutes=10),
    price_sell=10,
    img='/assets/items/Mushroom.png',
)
list_items.append(mushroom)

eggplant = hayday(
    name='eggplant',
    production_place='farm',
    level=90,
    production_time=td(minutes=40),
    price_sell=14,
    img='/assets/items/Eggplant.png',
)
list_items.append(eggplant)

watermelon = hayday(
    name='watermelon',
    production_place='farm',
    level=92,
    production_time=td(hours=5),
    price_sell=39,
    img='/assets/items/Watermelon.png',
)
list_items.append(watermelon)

plum = hayday(
    name='plum',
    production_place='farm',
    level=94,
    production_time=td(days=1, hours=1),
    price_sell=82,
    img='/assets/items/Plum.png',
)
list_items.append(plum)

chickpea = hayday(
    name='chickpea',
    production_place='farm',
    level=95,
    production_time=td(hours=1),
    price_sell=18,
    img='/assets/items/Chickpea.png',
)
list_items.append(chickpea)

mango = hayday(
    name='mango',
    production_place='farm',
    level=97,
    production_time=td(days=1, hours=8),
    price_sell=100,
    img='/assets/items/Mango.png',
)
list_items.append(mango)

coconut = hayday(
    name='coconut',
    production_place='farm',
    level=101,
    production_time=td(days=1, hours=12),
    price_sell=108,
    img='/assets/items/Coconut.png',
)
list_items.append(coconut)

guava = hayday(
    name='guava',
    production_place='farm',
    level=104,
    production_time=td(days=1, hours=10),
    price_sell=111,
    img='/assets/items/Guava.png',
)
list_items.append(guava)

pomegranate = hayday(
    name='pomegranate',
    production_place='farm',
    level=107,
    production_time=td(days=1, hours=3),
    price_sell=111,
    img='/assets/items/Pomegranate.png',
)
list_items.append(pomegranate)

asparagus = hayday(
    name='asparagus',
    production_place='farm',
    level=49,
    production_time=td(hours=6),
    price_sell=43,
    img='/assets/items/Asparagus.png',
)
list_items.append(asparagus)

oats = hayday(
    name='oats',
    production_place='farm',
    level=119,
    production_time=td(minutes=7),
    price_sell=7,
    img='/assets/items/Oats.png',
)
list_items.append(oats)

clay = hayday(
    name='clay',
    production_place='farm',
    level=94,
    production_time=td(hours=1, minutes=50),
    price_sell=18,
    img='/assets/items/Clay.png',
)
list_items.append(clay)

chamomile = hayday(
    name='chamomile',
    production_place='farm',
    level=45,
    production_time=td(minutes=20),
    price_sell=10,
    img='/assets/items/Chamomile.png',
)
list_items.append(chamomile)
