#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : item.py
# @created          : 12-Nov-2019
#

"""
List of every item that is offered in HAYDAY set as a object from class hayday
"""

from hayday import hayday
#from datetime  import time as td
from datetime import timedelta as td
#from datetime  import datetime as td

list_items = []         #Store every item defined below
#-----------------------------------------------------------
#def __init__(self,
#        name,
#        production_place,
#        production_time,
#        price_sell
#        ):
#Crops

wheat = hayday(
       name = 'wheat',
       production_place = 'farm',
       level = 1,
       production_time = td(minutes=2),
       price_sell = 3,
	img=''
        )
list_items.append(wheat)

corn = hayday(
       name = 'corn',
       production_place = 'farm',
       level = 2,
       production_time = td(minutes=5),
       price_sell = 7,
	img=''
        )
list_items.append(corn)

soybean = hayday(
       name = 'soybean',
       production_place = 'farm',
       level = 5,
       production_time = td(minutes=20),
       price_sell = 10,
	img=''
        )
list_items.append(soybean)

sugarcane = hayday(
       name = 'sugarcane',
       production_place = 'farm',
       level = 7,
       production_time = td(minutes=30),
       price_sell = 14,
	img=''
        )
list_items.append(sugarcane)

carrot = hayday(
       name = 'carrot',
       production_place = 'farm',
       level = 9,
       production_time = td(minutes=10),
       price_sell = 7,
	img=''
        )
list_items.append(carrot)

indigo = hayday(
       name = 'indigo',
       production_place = 'farm',
       level = 13,
       production_time = td(hours=2),
       price_sell = 25,
	img=''
        )
list_items.append(indigo)

apple = hayday(
       name = 'apple',
       production_place = 'farm',
       level = 15,
       production_time = td(hours=16),
       price_sell = 39,
	img=''
        )
list_items.append(apple)

pumpkin  = hayday(
       name = 'pumpkin',
       production_place = 'farm',
       level = 15,
       production_time = td(hours=3),
       price_sell = 32,
	img=''
        )
list_items.append(pumpkin)

cotton = hayday(
       name = 'cotton',
       production_place = 'farm',
       level = 18,
       production_time = td(hours=2, minutes=30),
       price_sell = 28,
	img=''
        )
list_items.append(cotton)

raspberry = hayday(
       name = 'raspberry',
       production_place = 'farm',
       level = 19,
       production_time = td(hours=18),
       price_sell = 46,
	img=''
        )
list_items.append(raspberry)

cherry = hayday(
       name = 'cherry',
       production_place = 'farm',
       level = 22,
       production_time = td(days=1, hours=3),
       price_sell = 68,
	img=''
        )
list_items.append(cherry)

chili_pepper = hayday(
       name = 'chili pepper',
       production_place = 'farm',
       level = 25,
       production_time = td(hours=4),
       price_sell = 36,
	img=''
        )
list_items.append(chili_pepper)

blackberry = hayday(
       name = 'blackberry',
       production_place = 'farm',
       level = 26,
       production_time = td(days=1,hours=8),
       price_sell = 82,
	img=''
        )
list_items.append(blackberry)

tomato = hayday(
       name = 'tomato',
       production_place = 'farm',
       level = 30,
       production_time = td(hours=6),
       price_sell = 43,
	img=''
        )
list_items.append(tomato)

strawberry = hayday(
       name = 'strawberry',
       production_place = 'farm',
       level = 34,
       production_time = td(hours=8),
       price_sell = 50,
	img=''
        )
list_items.append(strawberry)

potato = hayday(
       name = 'potato',
       production_place = 'farm',
       level = 35,
       production_time = td(hours=3, minutes=40),
       price_sell = 36,
	img=''
        )
list_items.append(potato)

cacao = hayday(
       name = 'cacao',
       production_place = 'farm',
       level = 36,
       production_time = td(days=1,hours=11),
       price_sell = 86,
	img=''
        )
list_items.append(cacao)

coffee_bean = hayday(
       name = 'coffee bean',
       production_place = 'farm',
       level = 42,
       production_time = td(days=1),
       price_sell = 64,
	img=''
        )
list_items.append(coffee_bean)

sesame = hayday(
       name = 'sasame',
       production_place = 'farm',
       level = 50,
       production_time = td(hours=1),
       price_sell = 18,
	img=''
        )
list_items.append(sesame)

pineapple = hayday(
       name = 'pineapple',
       production_place = 'farm',
       level = 52,
       production_time = td(minutes=30),
       price_sell = 14,
	img=''
        )
list_items.append(pineapple)

lily = hayday(
       name = 'lily',
       production_place = 'farm',
       level = 53,
       production_time = td(hours=1, minutes=30),
       price_sell = 21,
	img=''
        )
list_items.append(lily)

rice = hayday(
       name = 'rice',
       production_place = 'farm',
       level = 56,
       production_time = td(minutes=45),
       price_sell = 18,
	img=''
        )
list_items.append(rice)

olive = hayday(
       name = 'olive',
       production_place = 'farm',
       level = 57,
       production_time = td(hours=24),
       price_sell = 82,
	img=''
        )
list_items.append(olive)

lettuce = hayday(
       name = 'lettuce',
       production_place = 'farm',
       level = 58,
       production_time = td(hours=3, minutes=30),
       price_sell = 32,
	img=''
        )
list_items.append(lettuce)

garlic = hayday(
       name = 'garlic',
       production_place = 'farm',
       level = 60,
       production_time = td(minutes=30),
       price_sell = 14,
	img=''
        )
list_items.append(garlic)

sunflower = hayday(
       name = 'sunflower',
       production_place = 'farm',
       level = 63,
       production_time = td(hours=1, minutes=30),
       price_sell = 21,
	img=''
        )
list_items.append(sunflower)

cabbage = hayday(
       name = 'cabbage',
       production_place = 'farm',
       level = 65,
       production_time = td(minutes=45),
       price_sell = 18,
	img=''
        )
list_items.append(cabbage)

lemon = hayday(
       name = 'lemon',
       production_place = 'farm',
       level = 66,
       production_time = td(days=1, hours=5 ),
       price_sell = 93,
	img=''
        )
list_items.append(lemon)

onion = hayday(
       name = 'onion',
       production_place = 'farm',
       level = 68,
       production_time = td(hours=5),
       price_sell = 39,
	img=''
        )
list_items.append(onion)

cucumber = hayday(
       name = 'cucumber',
       production_place = 'farm',
       level = 70,
       production_time = td(minutes=35),
       price_sell = 14,
	img=''
        )
list_items.append(cucumber)

orange = hayday(
       name = 'orange',
       production_place = 'farm',
       level = 71,
       production_time = td(days=1, hours=7),
       price_sell = 97,
	img=''
        )
list_items.append(orange)

beetroot = hayday(
       name = 'beetroot',
       production_place = 'farm',
       level = 72,
       production_time = td(minutes=50),
       price_sell = 14,
	img=''
        )
list_items.append(beetroot)

peach = hayday(
       name = 'peach',
       production_place = 'farm',
       level = 76,
       production_time = td(days=1, hours=6),
       price_sell = 100,
	img=''
        )
list_items.append(peach)

ginger = hayday(
       name = 'ginger',
       production_place = 'farm',
       level = 78,
       production_time = td(hours=2, minutes=30),
       price_sell = 28,
	img=''
        )
list_items.append(ginger)

bell_pepper = hayday(
       name = 'bell pepper',
       production_place = 'farm',
       level = 74,
       production_time = td(hours=4, minutes=30),
       price_sell = 36,
	img=''
        )
list_items.append(bell_pepper)


#-----------------------------------------------------------
#Animals food

chicken_food = hayday(
       name = 'chicken food',
       production_place = 'feed mill',
       level = 3,
       production_time = td(minutes=5),
       price_sell = 7.,
	img=''
        )
chicken_food.add_component(wheat, 2)
chicken_food.add_component(corn, 1)
list_items.append(chicken_food)

cow_food = hayday(
       name = 'cow food',
       production_place = 'feed mill',
       level = 6,
       production_time = td(minutes=10),
       price_sell = 14,
	img=''
        )
cow_food.add_component(soybean, 2)
cow_food.add_component(corn, 1)
list_items.append(cow_food)

#TODO
pig_food = hayday(
       name = 'pig food',
       production_place = 'feed mill',
       level = 10,
       production_time = td(minutes=10),
       price_sell = 14,
	img=''
        )
pig_food.add_component(soybean, 1)
pig_food.add_component(carrot, 2)
list_items.append(pig_food)

#TODO
sheep_food = hayday(
       name = 'sheep food',
       production_place = 'feed mill',
       level = 16,
       production_time = td(minutes=10),
       price_sell = 14,
	img=''
        )
sheep_food.add_component(soybean, 1)
sheep_food.add_component(wheat, 3)
list_items.append(sheep_food)

#TODO
goat_food = hayday(
       name = 'goat food',
       production_place = 'feed mill',
       level = 32,
       production_time = td(minutes=10),
       price_sell = 14,
	img=''
        )
goat_food.add_component(corn, 1)
goat_food.add_component(corn, 1)
goat_food.add_component(carrot, 2)
list_items.append(goat_food)

#-----------------------------------------------------------
#Animals
egg = hayday(
       name = 'egg',
       production_place = 'farm',
       level = 1,
       production_time = td(minutes=20),
       price_sell = 18,
	img=''
        )
egg.add_component(chicken_food, 1)
list_items.append(egg)

milk = hayday(
       name = 'milk',
       production_place = 'farm',
       level = 6,
       production_time = td(hours=1),
       price_sell = 32,
	img=''
        )
milk.add_component(cow_food, 1)
list_items.append(milk)

goat_milk = hayday(
       name = 'goat milk',
       production_place = 'farm',
       level = 32,
       production_time = td(hours=8),
       price_sell = 64,
	img=''
        )
goat_milk.add_component(goat_food, 1)
list_items.append(goat_milk)

honeycomb = hayday(
       name = 'honeycomb',
       production_place = 'farm',
       level = 39,
       production_time = td(minutes=35),
       price_sell = 68,
	img=''
        )
list_items.append(honeycomb)

bacon = hayday(
       name = 'bacon',
       production_place = 'farm',
       level = 10,
       production_time = td(hours=4),
       price_sell = 50,
	img=''
        )
bacon.add_component(pig_food, 1)
list_items.append(bacon)

wool = hayday(
       name = 'wool',
       production_place = 'farm',
       level = 16,
       production_time = td(hours=6),
       price_sell = 54,
	img=''
        )
wool.add_component(sheep_food, 1)
list_items.append(wool)

peanuts = hayday(
        name = 'peanuts',
        production_place = 'farm',
        level = 62,
        production_time = td(hours=2, minutes=30),
        price_sell = 360,
	img=''
        )

#------------------------------------------------------------
#Honey extractor (Every item already included)

honey = hayday(
       name = 'honey',
       production_place = 'honey extractor',
       level = 39,
       production_time = td(minutes=20),
       price_sell = 154,
	img=''
        )
honey.add_component(honeycomb, 2)
list_items.append(honey)

beeswax = hayday(
       name = 'beeswax',
       production_place = 'honey extractor',
       level = 48,
       production_time = td(minutes=45),
       price_sell = 234,
	img=''
        )
beeswax.add_component(honeycomb, 3)
list_items.append(beeswax)

#-----------------------------------------------------------
#Fish
fish_fillet = hayday(
       name = 'fish fillet',
       production_place = 'fishing lake',
       level = 27,
       production_time = td(hours=7),
       price_sell = 54,
	img=''
        )
list_items.append(fish_fillet)

lobster_tail = hayday(
       name = 'lobster tail',
       production_place = 'fishing lake',
       level = 44,
       production_time = td(hours=6),
       price_sell = 201,
	img=''
        )
list_items.append(lobster_tail)

duck = hayday(
       name = 'duck',
       production_place = 'fishing lake',
       level = 50,
       production_time = td(hours=2),
       price_sell = 1,
	img=''
        )
list_items.append(duck)

#-----------------------------------------------------------
#Duck Salon

duck_feather  = hayday(
       name = 'duck feather',
       production_place = 'duck salon',
       level = 50,
       production_time = td(hours=3),
       price_sell = 140,
	img=''
        )
duck_feather.add_component(duck, 1)
list_items.append(duck_feather)

#-----------------------------------------------------------
#Sugar mill (Every item already included)
brown_sugar = hayday(
       name = 'brown sugar',
       production_place = 'sugar mill',
       level = 7,
       production_time = td(minutes=20),
       price_sell = 32,
	img=''
        )
brown_sugar.add_component(sugarcane, 1)
list_items.append(brown_sugar)

white_sugar = hayday(
       name = 'white sugar',
       production_place = 'sugar mill',
       level = 13,
       production_time = td(minutes=40),
       price_sell = 50,
	img=''
        )
white_sugar.add_component(sugarcane, 2)
list_items.append(white_sugar)

syrup = hayday(
       name = 'syrup',
       production_place = 'sugar mill',
       level = 18,
       production_time = td(hours=1,minutes=30),
       price_sell = 90,
	img=''
        )
syrup.add_component(sugarcane, 4)
list_items.append(syrup)
#-----------------------------------------------------------
#Dairy (Every item already included)
cream = hayday(
       name = 'cream',
       production_place = 'dairy',
       level = 6,
       production_time = td(minutes=20),
       price_sell = 50,
	img=''
        )
cream.add_component(milk, 1)
list_items.append(cream)

butter = hayday(
       name = 'butter',
       production_place = 'dairy',
       level = 9,
       production_time = td(minutes=30),
       price_sell = 82,
	img=''
        )
butter.add_component(milk, 2)
list_items.append(butter)

cheese = hayday(
       name = 'cheese',
       production_place = 'dairy',
       level = 12,
       production_time = td(hours=1),
       price_sell = 122,
	img=''
        )
cheese.add_component(milk, 3)
list_items.append(cheese)

goat_cheese = hayday(
       name = 'goat cheese',
       production_place = 'dairy',
       level = 33,
       production_time = td(hours=1,minutes=30),
       price_sell = 162,
	img=''
        )
goat_cheese.add_component(goat_milk, 2)
list_items.append(goat_cheese)




#-----------------------------------------------------------

#Bakery
bread = hayday(
       name = 'bread',
       production_place = 'bakery',
       level = 2,
       production_time = td(minutes=5),
       price_sell = 21,
	img=''
        )
bread.add_component(wheat, 3)
list_items.append(bread)

corn_bread = hayday(
       name = 'corn bread',
       production_place = 'bakery',
       level = 7,
       production_time = td(minutes=30),
       price_sell = 72,
	img=''
        )
corn_bread.add_component(corn, 2)
corn_bread.add_component(egg, 2)
list_items.append(corn_bread)

cookie = hayday(
       name = 'cookie',
       production_place = 'bakery',
       level = 10,
       production_time = td(hours=1),
       price_sell = 104,
	img=''
        )
cookie.add_component(wheat, 2)
cookie.add_component(egg, 2)
cookie.add_component(brown_sugar, 1)
list_items.append(cookie)

raspberry_muffin = hayday(
       name = 'raspberry muffin',
       production_place = 'bakery',
       level = 19,
       production_time = td(minutes=45),
       price_sell =140,
	img=''
        )
raspberry_muffin.add_component(wheat, 2)
raspberry_muffin.add_component(egg, 1)
raspberry_muffin.add_component(raspberry, 2)
list_items.append(raspberry_muffin)

blackbery_muffin = hayday(
       name = 'blackberry muffin',
       production_place = 'bakery',
       level = 26,
       production_time = td(minutes=45),
       price_sell = 226,
	img=''
        )
blackbery_muffin.add_component(wheat, 1)
blackbery_muffin.add_component(egg, 2)
blackbery_muffin.add_component(blackberry, 2)
list_items.append(blackbery_muffin)

pizza = hayday(
       name = 'pizza',
       production_place = 'bakery',
       level = 33,
       production_time = td(minutes=15),
       price_sell = 190,
	img=''
        )
pizza.add_component(wheat, 2)
pizza.add_component(tomato, 1)
pizza.add_component(cheese, 1)
list_items.append(pizza)

spicy_pizza = hayday(
       name = 'spicy pizza',
       production_place = 'bakery',
       level = 37,
       production_time = td(minutes=15),
       price_sell = 226,
	img=''
        )
spicy_pizza.add_component(wheat, 2)
spicy_pizza.add_component(tomato, 1)
spicy_pizza.add_component(cheese, 1)
spicy_pizza.add_component(chili_pepper, 1)
list_items.append(spicy_pizza)

potato_bread = hayday(
       name = 'potato bread',
       production_place = 'bakery',
       level = 39,
       production_time = td(minutes=45),
       price_sell = 284,
	img=''
        )
potato_bread.add_component(potato, 2)
potato_bread.add_component(white_sugar, 1)
potato_bread.add_component(egg, 3)
potato_bread.add_component(butter, 1)
list_items.append(potato_bread)

frutti_di_mare_pizza = hayday(
       name = 'frutti di mare pizza',
       production_place = 'bakery',
       level = 45,
       production_time = td(minutes=15),
       price_sell = 403,
	img=''
        )
frutti_di_mare_pizza.add_component(wheat, 2)
frutti_di_mare_pizza.add_component(fish_fillet, 1)
frutti_di_mare_pizza.add_component(lobster_tail, 1)
frutti_di_mare_pizza.add_component(cheese, 1)
list_items.append(frutti_di_mare_pizza)

#banana_bread = hayday(
#       name = 'banana bread',
#       production_place = 'bakery',
#       level = 91,
#       production_time = td(minutes=30),
#       price_sell = 424,
	img=''
#        )
#banana_bread.add_component(wheat, 2)
#list_items.append(banana_bread)

#-----------------------------------------------------------
#Popcorn pot (Every item already included)

popcorn = hayday(
       name = 'popcorn',
       production_place = 'popcorn pot',
       level = 8,
       production_time = td(minutes=30),
       price_sell = 32,
	img=''
        )
popcorn.add_component(corn, 2)
list_items.append(popcorn)

buttered_popcorn = hayday(
       name = 'buttered popcorn',
       production_place = 'popcorn pot',
       level = 16,
       production_time = td(minutes=60),
       price_sell = 126,
	img=''
        )
buttered_popcorn.add_component(corn, 2)
buttered_popcorn.add_component(butter, 1)
list_items.append(buttered_popcorn)

chili_popcorn = hayday(
       name = 'chili popcorn',
       production_place = 'popcorn pot',
       level = 25,
       production_time = td(hours=2),
       price_sell = 122,
	img=''
        )
chili_popcorn.add_component(corn, 2)
chili_popcorn.add_component(chili_pepper, 2)
list_items.append(chili_popcorn)

honey_popcorn = hayday(
       name = 'honey popcorn',
       production_place = 'popcorn pot',
       level = 40,
       production_time = td(hours=1,minutes=30),
       price_sell = 360,
	img=''
        )
honey_popcorn.add_component(corn, 2)
honey_popcorn.add_component(honey, 2)
list_items.append(honey_popcorn)

chocolate_popcorn = hayday(
       name = 'chocolate popcorn',
       production_place = 'popcorn pot',
       level = 44,
       production_time = td(hours=2,minutes=30),
       price_sell = 248,
	img=''
        )
chocolate_popcorn.add_component(corn, 2)
chocolate_popcorn.add_component(cacao, 2)
list_items.append(chocolate_popcorn)

#-----------------------------------------------------------
#BBQ grill

pancake = hayday(
       name = 'pancake',
       production_place = 'bbq grill',
       level = 9,
       production_time = td(minutes=30),
       price_sell = 108,
	img=''
        )
pancake.add_component(egg, 3)
pancake.add_component(brown_sugar, 1)
list_items.append(pancake)

bacon_and_eggs = hayday(
       name = 'bakon and eggs',
       production_place = 'bbq grill',
       level = 11,
       production_time = td(minutes=60),
       price_sell = 201,
	img=''
        )
bacon_and_eggs.add_component(egg, 4)
bacon_and_eggs.add_component(bacon, 2)
list_items.append(bacon_and_eggs)

hamburger = hayday(
       name = 'hamburger',
       production_place = 'bbq grill',
       level = 18,
       production_time = td(hours=2),
       price_sell = 180,
	img=''
        )
hamburger.add_component(bread, 2)
hamburger.add_component(bacon, 2)
list_items.append(hamburger)

fish_burger = hayday(
       name = 'fish burger',
       production_place = 'bbq grill',
       level = 27,
       production_time = td(hours=2),
       price_sell = 226,
	img=''
        )
fish_burger.add_component(fish_fillet, 2)
fish_burger.add_component(bread, 2)
fish_burger.add_component(chili_pepper, 1)
list_items.append(fish_burger)

roasted_tomatoes = hayday(
       name = 'roasted tomatoes',
       production_place = 'bbq grill',
       level = 30,
       production_time = td(hours=1, minutes=30),
       price_sell = 118,
	img=''
        )
roasted_tomatoes.add_component(tomato, 2)
list_items.append(roasted_tomatoes)

baked_potato = hayday(
       name = 'baked potato',
       production_place = 'bbq grill',
       level = 35,
       production_time = td(minutes=35),
       price_sell = 298,
	img=''
        )
baked_potato.add_component(potato, 2)
baked_potato.add_component(chili_pepper, 1)
baked_potato.add_component(cream, 1)
baked_potato.add_component(cheese, 1)
list_items.append(baked_potato)

fish_and_chips = hayday(
       name = 'fish and chips',
       production_place = 'bbq grill',
       level = 41,
       production_time = td(hours=1,minutes=30),
       price_sell = 244,
	img=''
        )
fish_and_chips.add_component(fish_fillet, 2)
fish_and_chips.add_component(potato, 3)
list_items.append(fish_and_chips)

lobster_skewer = hayday(
       name = 'lobster skewer',
       production_place = 'bbq grill',
       level = 48,
       production_time = td(minutes=40),
       price_sell = 417,
	img=''
        )
lobster_skewer.add_component(lobster_tail, 1)
lobster_skewer.add_component(chili_pepper, 1)
lobster_skewer.add_component(honey, 1)
list_items.append(lobster_skewer)

garlic_bread = hayday(
       name = 'garlic bread',
       production_place = 'bbq grill',
       level = 60,
       production_time = td(minutes=15),
       price_sell = 198,
	img=''
        )
garlic_bread.add_component(bread, 2)
garlic_bread.add_component(butter, 1)
garlic_bread.add_component(garlic, 4)
list_items.append(garlic_bread)


grilled_onion = hayday(
       name = 'grilled onion',
       production_place = 'bbq grill',
       level = 68,
       production_time = td(hours=1),
       price_sell = 190,
	img=''
        )
grilled_onion.add_component(butter, 1)
grilled_onion.add_component(onion, 2)
list_items.append(grilled_onion)

winter_veggies = hayday(
       name = 'winter veggies',
       production_place = 'bbq grill',
       level = 72,
       production_time = td(minutes=25),
       price_sell =  198,
	img=''
        )
winter_veggies.add_component(beetroot, 2)
winter_veggies.add_component(carrot, 2)
winter_veggies.add_component(potato, 2)
winter_veggies.add_component(pumpkin, 2)
list_items.append(winter_veggies)
#------------------------------------------------------------
#Sauce Maker (Every item already included)

soy_sauce = hayday(
        name= 'soy sauce',
        production_place = 'sauce maker',
        level = 54,
        production_time = td(hours=3),
        price_sell = 154,
	img=''
        )
soy_sauce.add_component(soybean, 9)
soy_sauce.add_component(wheat, 1)
list_items.append(soy_sauce)

olive_oil = hayday(
        name= 'olive oil',
        production_place = 'sauce maker',
        level = 60,
        production_time = td(minutes=45),
        price_sell = 277,
	img=''
        )
olive_oil.add_component(olive, 3)
list_items.append(olive_oil)

mayonnaise = hayday(
        name= 'mayonnaise',
        production_place = 'sauce maker',
        level = 62,
        production_time = td(minutes=15),
        price_sell = 367,
	img=''
        )
mayonnaise.add_component(egg, 4)
mayonnaise.add_component(olive_oil, 1)
list_items.append(mayonnaise)

olive_dip = hayday(
        name= 'olive dip',
        production_place = 'sauce maker',
        level = 66,
        production_time = td(minutes=45),
        price_sell = 468,
	img=''
        )
olive_dip.add_component(olive, 3)
olive_dip.add_component(bread, 2)
olive_dip.add_component(fish_fillet, 1)
olive_dip.add_component(lemon, 1)
list_items.append(olive_dip)

lemon_curd = hayday(
        name= 'lemon curd',
        production_place = 'sauce maker',
        level = 66,
        production_time = td(minutes=25),
        price_sell =378,
	img=''
        )
lemon_curd.add_component(lemon, 2)
lemon_curd.add_component(butter, 1)
lemon_curd.add_component(egg, 2)
lemon_curd.add_component(white_sugar, 1)
list_items.append(lemon_curd)

tomato_sauce = hayday(
        name= 'tomate sauce',
        production_place = 'sauce maker',
        level = 69,
        production_time = td(minutes=30),
        price_sell =230,
	img=''
        )
tomato_sauce.add_component(lemon, 1)
tomato_sauce.add_component(brown_sugar, 1)
tomato_sauce.add_component(tomato, 2)
list_items.append(tomato_sauce)

salsa = hayday(
        name= 'salsa',
        production_place = 'sauce maker',
        level = 77,
        production_time = td(minutes=20),
        price_sell =252,
	img=''
        )
salsa.add_component(chili_pepper, 2)
salsa.add_component(onion, 2)
salsa.add_component(tomato, 2)
list_items.append(salsa)
#-----------------------------------------------------------
#Pie oven

carrot_pie = hayday(
       name = 'carrot pie',
       production_place = 'pie oven',
       level = 14,
       production_time = td(hours=1),
       price_sell = 82,
	img=''
        )
carrot_pie.add_component(carrot, 3)
carrot_pie.add_component(wheat, 2)
carrot_pie.add_component(egg, 1)
list_items.append(carrot_pie)

pumpkin_pie = hayday(
       name = 'pumpkin pie',
       production_place = 'pie oven',
       level = 15,
       production_time = td(hours=2),
       price_sell = 158,
	img=''
        )
pumpkin_pie.add_component(pumpkin, 3)
pumpkin_pie.add_component(wheat, 2)
pumpkin_pie.add_component(egg, 1)
list_items.append(pumpkin_pie)

bacon_pie = hayday(
       name = 'bacon pie',
       production_place = 'pie oven',
       level = 18,
       production_time = td(hours=3),
       price_sell = 219,
	img=''
        )
bacon_pie.add_component(bacon, 3)
bacon_pie.add_component(wheat, 2)
bacon_pie.add_component(egg, 1)
list_items.append(bacon_pie)

apple_pie = hayday(
       name = 'apple pie',
       production_place = 'pie oven',
       level = 28,
       production_time = td(hours=2,minutes=30),
       price_sell = 270,
	img=''
        )
apple_pie.add_component(apple, 3)
apple_pie.add_component(wheat, 2)
apple_pie.add_component(egg, 1)
apple_pie.add_component(syrup, 1)
list_items.append(apple_pie)

fish_pie = hayday(
       name = 'fish pie',
       production_place = 'pie oven',
       level = 28,
       production_time = td(hours=2),
       price_sell = 226,
	img=''
        )
fish_pie.add_component(fish_fillet, 3)
fish_pie.add_component(wheat, 2)
fish_pie.add_component(egg, 1)
list_items.append(fish_pie)

feta_pie = hayday(
       name = 'feta pie',
       production_place = 'pie oven',
       level = 34,
       production_time = td(hours=1,minutes=30),
       price_sell = 223,
	img=''
        )
feta_pie.add_component(goat_cheese, 1)
feta_pie.add_component(wheat, 2)
feta_pie.add_component(egg, 1)
list_items.append(feta_pie)

casserole = hayday(
       name = 'casserole',
       production_place = 'pie oven',
       level = 36,
       production_time = td(hours=2),
       price_sell = 367,
	img=''
        )
casserole.add_component(potato, 2)
casserole.add_component(bacon, 2)
casserole.add_component(egg, 2)
casserole.add_component(cheese, 1)
list_items.append(casserole)

shepherds_pie = hayday(
       name = 'shepherds pie',
       production_place = 'pie oven',
       level = 39,
       production_time = td(hours=1,minutes=40),
       price_sell = 280,
	img=''
        )
shepherds_pie.add_component(potato, 2)
shepherds_pie.add_component(bacon, 2)
shepherds_pie.add_component(carrot, 2)
shepherds_pie.add_component(pumpkin, 2)
list_items.append(shepherds_pie)

chocolate_pie = hayday(
       name = 'chocolate pie',
       production_place = 'pie oven',
       level = 65,
       production_time = td(hours=1,minutes=15),
       price_sell = 514,
	img=''
        )
chocolate_pie.add_component(wheat, 3)
chocolate_pie.add_component(cacao, 2)
chocolate_pie.add_component(egg,1)
chocolate_pie.add_component(peanuts, 1)
list_items.append(chocolate_pie)

lemon_pie = hayday(
       name = 'lemon pie',
       production_place = 'pie oven',
       level = 67,
       production_time = td(hours=2,minutes=15),
       price_sell = 446,
	img=''
        )
lemon_pie.add_component(lemon_curd, 1)
lemon_pie.add_component(wheat, 2)
lemon_pie.add_component(egg,1)
list_items.append(lemon_pie)

peach_tart = hayday(
       name = 'peach tart',
       production_place = 'pie oven',
       level = 76,
       production_time = td(hours=2,minutes=30),
       price_sell = 435,
	img=''
        )
peach_tart.add_component(cream, 1)
peach_tart.add_component(egg, 2)
peach_tart.add_component(peach,3)
peach_tart.add_component(wheat,2)
list_items.append(peach_tart)

#-----------------------------------------------------------
#Loom (Every item already  included)
sweater = hayday(
       name = 'sweater',
       production_place = 'loom',
       level = 17,
       production_time = td(hours=2),
       price_sell = 158,
	img=''
        )
sweater.add_component(wool, 2)
list_items.append(sweater)

cotton_fabric = hayday(
       name = 'cotton fabric',
       production_place = 'loom',
       level = 18,
       production_time = td(minutes=30),
       price_sell = 108,
	img=''
        )
cotton_fabric.add_component(cotton, 3)
list_items.append(cotton_fabric)

blue_woolly_hat = hayday(
       name = 'blue woolly hat',
       production_place = 'loom',
       level = 19,
       production_time = td(hours=1),
       price_sell = 111,
	img=''
        )
blue_woolly_hat.add_component(wool, 1)
blue_woolly_hat.add_component(indigo, 1)
list_items.append(blue_woolly_hat)

red_scarf = hayday(
       name = 'red scarf',
       production_place = 'loom',
       level = 48,
       production_time = td(hours=2,minutes=30),
       price_sell = 288,
	img=''
        )
red_scarf.add_component(wool, 2)
red_scarf.add_component(strawberry, 2)
list_items.append(red_scarf)

flower_shawl = hayday(
       name = 'flower shawl',
       production_place = 'loom',
       level = 71,
       production_time = td(hours=1,minutes=30),
       price_sell = 295,
	img=''
        )
flower_shawl.add_component(wool, 2)
flower_shawl.add_component(blackberry, 1)
flower_shawl.add_component(sunflower, 3)
list_items.append(flower_shawl)
#-----------------------------------------------------------
#Sewing machine (Every item already included)

cotton_shirt = hayday(
       name = 'cotton shirt',
       production_place = 'sewing machine',
       level = 19,
       production_time = td(minutes=45),
       price_sell = 241,
	img=''
        )
cotton_shirt.add_component(cotton_fabric, 2)
list_items.append(cotton_shirt)

wooly_chaps = hayday(
       name = 'wooly chaps',
       production_place = 'sewing machine',
       level = 21,
       production_time = td(hours=1,minutes=30),
       price_sell = 309,
	img=''
        )
wooly_chaps.add_component(cotton_fabric, 1)
wooly_chaps.add_component(wool, 3)
list_items.append(wooly_chaps)

violet_dress = hayday(
       name = 'violet dress',
       production_place = 'sewing machine',
       level = 25,
       production_time = td(hours=2,minutes=15),
       price_sell = 327,
	img=''
        )
violet_dress.add_component(cotton_fabric, 2)
violet_dress.add_component(raspberry, 1)
violet_dress.add_component(indigo, 1)
list_items.append(violet_dress)

pillow = hayday(
       name = 'pillow',
       production_place = 'sewing machine',
       level = 51,
       production_time = td(hours=3),
       price_sell = 676,
	img=''
        )
pillow.add_component(cotton_fabric, 2)
pillow.add_component(duck_feather, 3)
list_items.append(pillow)


blanket = hayday(
       name = 'blanket',
       production_place = 'sewing machine',
       level = 59,
       production_time = td(hours=3, minutes=30),
       price_sell = 1098,
	img=''
        )
blanket.add_component(cotton_fabric, 3)
blanket.add_component(duck_feather, 5)
blanket.add_component(pumpkin, 1)
list_items.append(blanket)

#--------------------------------------------------------------------------------
#Mine (Every item already included)
silver_ore = hayday(
       name = 'silver ore',
       production_place = 'mine',
       level = 24,
       production_time = td(minutes=1),
       price_sell = 18,
	img=''
        )
list_items.append(silver_ore)

gold_ore = hayday(
       name = 'gold ore',
       production_place = 'mine',
       level = 24,
       production_time = td(minutes=1),
       price_sell = 21,
	img=''
        )
list_items.append(gold_ore)

platinum_ore = hayday(
       name = 'platinum ore',
       production_place = 'mine',
       level = 25,
       production_time = td(minutes=1),
       price_sell = 32,
	img=''
        )
list_items.append(platinum_ore)

coal = hayday(
       name = 'coal',
       production_place = 'mine',
       level = 33,
       production_time = td(minutes=1),
       price_sell = 10,
	img=''
        )
list_items.append(coal)

iron_ore = hayday(
       name = 'iron ore',
       production_place = 'mine',
       level = 34,
       production_time = td(minutes=1),
       price_sell = 14,
	img=''
        )
list_items.append(iron_ore)

#--------------------------------------------------------------------------------
#Cake oven

carrot_cake = hayday(
       name = 'carrot cake',
       production_place = 'cake oven',
       level = 21,
       production_time = td(hours=1,minutes=30),
       price_sell = 165,
	img=''
        )
carrot_cake.add_component(carrot, 2)
carrot_cake.add_component(butter, 1)
carrot_cake.add_component(brown_sugar, 1)
list_items.append(carrot_cake)

cream_cake = hayday(
       name = 'cream cake',
       production_place = 'cake oven',
       level = 23,
       production_time = td(hours=3),
       price_sell = 219,
	img=''
        )
cream_cake.add_component(wheat, 5)
cream_cake.add_component(cream, 1)
cream_cake.add_component(white_sugar, 1)
list_items.append(cream_cake)

red_berry_cake = hayday(
       name = 'red berry cake',
       production_place = 'cake oven',
       level = 23,
       production_time = td(hours=1),
       price_sell = 255,
	img=''
        )
red_berry_cake.add_component(raspberry, 1)
red_berry_cake.add_component(cherry, 2)
red_berry_cake.add_component(milk, 1)
red_berry_cake.add_component(egg, 1)
list_items.append(red_berry_cake)

cheesecake = hayday(
       name = 'cheesecake',
       production_place = 'cake oven',
       level = 24,
       production_time = td(hours=4),
       price_sell = 248,
	img=''
        )
cheesecake.add_component(cheese, 1)
cheesecake.add_component(cookie, 1)
list_items.append(cheesecake)

strawberry_cake = hayday(
       name = 'strawberry  cake',
       production_place = 'cake oven',
       level = 35,
       production_time = td(hours=3),
       price_sell = 316,
	img=''
        )
strawberry_cake.add_component(wheat, 3)
strawberry_cake.add_component(cream, 1)
strawberry_cake.add_component(white_sugar, 1)
strawberry_cake.add_component(strawberry, 2)
list_items.append(strawberry_cake)

chocolate_cake = hayday(
       name = 'chocolate cake',
       production_place = 'cake oven',
       level = 36,
       production_time = td(hours=2),
       price_sell = 320,
	img=''
        )
chocolate_cake.add_component(cacao, 2)
chocolate_cake.add_component(brown_sugar, 1)
chocolate_cake.add_component(butter, 1)
list_items.append(chocolate_cake)

potato_feta_cake = hayday(
       name = 'potato feta cake',
       production_place = 'cake oven',
       level = 38,
       production_time = td(hours=2),
       price_sell = 309,
	img=''
        )
potato_feta_cake.add_component(potato, 1)
potato_feta_cake.add_component(egg, 4)
potato_feta_cake.add_component(goat_cheese, 1)
list_items.append(potato_feta_cake)

honey_apple_cake = hayday(
       name = 'honey apple cake',
       production_place = 'cake oven',
       level = 42,
       production_time = td(hours=3,minutes=20),
       price_sell = 482,
	img=''
        )
honey_apple_cake.add_component(wheat, 2)
honey_apple_cake.add_component(egg, 2)
honey_apple_cake.add_component(apple, 2)
honey_apple_cake.add_component(honey, 2)
list_items.append(honey_apple_cake)

fancy_cake = hayday(
       name = 'fancy cake',
       production_place = 'cake oven',
       level = 54,
       production_time = td(minutes=15),
       price_sell = 450,
	img=''
        )
fancy_cake.add_component(cream_cake, 1)
fancy_cake.add_component(lily, 3)
fancy_cake.add_component(raspberry, 3)
fancy_cake.add_component(gold_ore, 1)
list_items.append(fancy_cake)

pineapple_cake = hayday(
       name = 'pineapple cake',
       production_place = 'cake oven',
       level = 65,
       production_time = td(hours=1, minutes=15),
       price_sell = 259,
	img=''
        )
pineapple_cake.add_component(pineapple, 3)
pineapple_cake.add_component(egg, 2)
pineapple_cake.add_component(cherry, 2)
pineapple_cake.add_component(wheat, 4)
list_items.append(pineapple_cake)

lemon_cake = hayday(
       name = 'lemon cake',
       production_place = 'cake oven',
       level = 68,
       production_time = td(hours=2, minutes=30),
       price_sell = 896,
	img=''
        )
lemon_cake.add_component(lemon_curd, 2)
lemon_cake.add_component(egg, 2)
lemon_cake.add_component(cream, 1)
lemon_cake.add_component(wheat, 3)
list_items.append(lemon_cake)

#--------------------------------------------------------------------------------
#Smelter (Every item already included)

silver_bar = hayday(
       name = 'silver bar',
       production_place = 'smelter',
       level = 24,
       production_time = td(hours=8),
       price_sell = 147,
	img=''
        )
silver_bar.add_component(silver_ore, 3)
list_items.append(silver_bar)

gold_bar = hayday(
       name = 'gold bar',
       production_place = 'smelter',
       level = 25,
       production_time = td(hours=12),
       price_sell = 180,
	img=''
        )
gold_bar.add_component(gold_ore, 3)
list_items.append(gold_bar)

platinum_bar = hayday(
       name = 'platinum  bar',
       production_place = 'smelter',
       level = 25,
       production_time = td(hours=16),
       price_sell = 250,
	img=''
        )
platinum_bar.add_component(platinum_ore, 3)
list_items.append(platinum_bar)

refined_coal = hayday(
       name = 'refined coal',
       production_place = 'smelter',
       level = 33,
       production_time = td(hours=6),
       price_sell = 108,
	img=''
        )
refined_coal.add_component(coal, 3)
list_items.append(refined_coal)

iron_bar = hayday(
       name = 'iron bar',
       production_place = 'smelter',
       level = 34,
       production_time = td(hours=7),
       price_sell = 129,
	img=''
        )
iron_bar.add_component(iron_ore, 3)
list_items.append(iron_bar)

#------------------------------------------------------------
#Juice press
carrot_juice = hayday(
       name = 'carrot juice',
       production_place = 'juice press',
       level = 26,
       production_time = td(minutes=30),
       price_sell = 46,
	img=''
        )
carrot_juice.add_component(carrot, 3)
list_items.append(carrot_juice)

apple_juice = hayday(
       name = 'apple juice',
       production_place = 'juice press',
       level = 28,
       production_time = td(hours=2),
       price_sell = 129,
	img=''
        )
apple_juice.add_component(apple, 2)
list_items.append(apple_juice)

cherry_juice = hayday(
       name = 'cherry juice',
       production_place = 'juice press',
       level = 30,
       production_time = td(hours=2,minutes=30),
       price_sell = 216,
	img=''
        )
cherry_juice.add_component(cherry, 2)
list_items.append(cherry_juice)

tomato_juice = hayday(
       name = 'tomato juice',
       production_place = 'juice press',
       level = 31,
       production_time = td(hours=1,minutes=30),
       price_sell = 162,
	img=''
        )
tomato_juice.add_component(tomato, 3)
list_items.append(tomato_juice)

berry_juice = hayday(
       name = 'berry juice',
       production_place = 'juice press',
       level = 31,
       production_time = td(hours=3),
       price_sell = 205,
	img=''
        )
berry_juice.add_component(blackberry, 1)
berry_juice.add_component(raspberry, 1)
list_items.append(berry_juice)

pineapple_juice = hayday(
       name = 'pineapple juice',
       production_place = 'juice press',
       level = 52,
       production_time = td(minutes=45),
       price_sell = 68,
	img=''
        )
pineapple_juice.add_component(pineapple, 3)
list_items.append(pineapple_juice)

orange_juice = hayday(
       name = 'orange juice',
       production_place = 'juice press',
       level = 71,
       production_time = td(hours=2),
       price_sell = 234,
	img=''
        )
orange_juice.add_component(orange, 2)
list_items.append(orange_juice)

#------------------------------------------------------------
#Ice cream maker

vanilla_ice_cream = hayday(
       name = 'vanilla ice cream',
       production_place = 'ice cream maker',
       level = 29,
       production_time = td(hours=2),
       price_sell = 172,
	img=''
        )
vanilla_ice_cream.add_component(milk, 1)
vanilla_ice_cream.add_component(cream, 1)
vanilla_ice_cream.add_component(white_sugar, 1)
list_items.append(vanilla_ice_cream)

cherry_popsicle = hayday(
       name = 'cherry popsicle',
       production_place = 'ice cream maker',
       level = 33,
       production_time = td(hours=3),
       price_sell = 352,
	img=''
        )
cherry_popsicle.add_component(syrup, 1)
cherry_popsicle.add_component(cherry_juice, 1)
list_items.append(cherry_popsicle)

strawberry_ice_cream = hayday(
       name = 'strawberry ice cream',
       production_place = 'ice cream maker',
       level = 34,
       production_time = td(hours=4),
       price_sell = 331,
	img=''
        )
strawberry_ice_cream.add_component(milk, 1)
strawberry_ice_cream.add_component(cream, 1)
strawberry_ice_cream.add_component(white_sugar, 1)
strawberry_ice_cream.add_component(strawberry, 3)
list_items.append(strawberry_ice_cream)

chocolate_ice_cream = hayday(
       name = 'chocolate ice cream',
       production_place = 'ice cream maker',
       level = 39,
       production_time = td(hours=2,minutes=30),
       price_sell = 342,
	img=''
        )
chocolate_ice_cream.add_component(milk, 1)
chocolate_ice_cream.add_component(cream, 1)
chocolate_ice_cream.add_component(white_sugar, 1)
chocolate_ice_cream.add_component(cacao, 2)
list_items.append(chocolate_ice_cream)

sesame_ice_cream = hayday(
       name = 'sesame ice cream',
       production_place = 'ice cream maker',
       level = 50,
       production_time = td(hours=2),
       price_sell = 176,
	img=''
        )
sesame_ice_cream.add_component(cream, 1)
sesame_ice_cream.add_component(brown_sugar, 1)
sesame_ice_cream.add_component(sesame, 3)
list_items.append(sesame_ice_cream)

peanut_butter_milkshake = hayday(
       name = 'peanut butter milkshake',
       production_place = 'ice cream maker',
       level = 68,
       production_time = td(hours=1, minutes=40),
       price_sell = 619,
	img=''
        )
peanut_butter_milkshake.add_component(peanuts, 1)
peanut_butter_milkshake.add_component(milk, 1)
peanut_butter_milkshake.add_component(cream, 3)
peanut_butter_milkshake.add_component(cacao, 3)
list_items.append(peanut_butter_milkshake)

orange_sorbet = hayday(
       name = 'orange sorbet',
       production_place = 'ice cream maker',
       level = 78,
       production_time = td(hours=3, minutes=30),
       price_sell = 399,
	img=''
        )
orange_sorbet.add_component(honey, 1)
orange_sorbet.add_component(orange, 2)
list_items.append(orange_sorbet)

#------------------------------------------------------------
#Jam maker

apple_jam = hayday(
       name = 'apple jam',
       production_place = 'jam maker',
       level = 35,
       production_time = td(hours=6),
       price_sell = 219,
	img=''
        )
apple_jam.add_component(apple, 3)
list_items.append(apple_jam)

raspberry_jam = hayday(
       name = 'raspberry jam',
       production_place = 'jam maker',
       level = 36,
       production_time = td(hours=7),
       price_sell = 252,
	img=''
        )
raspberry_jam.add_component(raspberry, 3)
list_items.append(raspberry_jam)

blackberry_jam = hayday(
       name = 'blackberry jam',
       production_place = 'jam maker',
       level = 37,
       production_time = td(hours=8),
       price_sell = 388,
	img=''
        )
blackberry_jam.add_component(blackberry, 3)
list_items.append(blackberry_jam)

cherry_jam = hayday(
       name = 'cherry jam',
       production_place = 'jam maker',
       level = 38,
       production_time = td(hours=7),
       price_sell = 334,
	img=''
        )
cherry_jam.add_component(cherry, 3)
list_items.append(cherry_jam)

strawberry_jam = hayday(
       name = 'strawberry jam',
       production_place = 'jam maker',
       level = 50,
       production_time = td(hours=7, minutes=30),
       price_sell = 270,
	img=''
        )
strawberry_jam.add_component(strawberry, 3)
list_items.append(strawberry_jam)

marmalade = hayday(
       name = 'marmalade',
       production_place = 'jam maker',
       level = 74,
       production_time = td(hours=8, minutes=30),
       price_sell =457,
	img=''
        )
marmalade.add_component(orange, 3)
list_items.append(marmalade)

peach_jam = hayday(
       name = 'peach jam',
       production_place = 'jam maker',
       level = 79,
       production_time = td(hours=8),
       price_sell = 464,
	img=''
        )
peach_jam.add_component(peach, 3)
list_items.append(peach_jam)

#------------------------------------------------------------
#Jeweler

bracelet = hayday(
       name = 'bracelet',
       production_place = 'jeweler',
       level = 38,
       production_time = td(hours=2),
       price_sell = 514,
	img=''
        )
bracelet.add_component(silver_bar, 2)
bracelet.add_component(gold_bar, 1)
list_items.append(bracelet)

necklace = hayday(
       name = 'necklace',
       production_place = 'jeweler',
       level = 39,
       production_time = td(hours=3),
       price_sell = 727,
	img=''
        )
necklace.add_component(silver_bar, 2)
necklace.add_component(gold_bar, 1)
necklace.add_component(platinum_bar, 1)
list_items.append(necklace)

diamond_ring = hayday(
       name = 'diamond ring',
       production_place = 'jeweler',
       level = 40,
       production_time = td(hours=4),
       price_sell = 824,
	img=''
        )
diamond_ring.add_component(platinum_bar, 2)
diamond_ring.add_component(gold_bar, 2)
#Diamond missing - no definition
list_items.append(diamond_ring)

iron_bracelet = hayday(
       name = 'iron bracelet',
       production_place = 'jeweler',
       level = 41,
       production_time = td(hours=1,minutes=30),
       price_sell = 658,
	img=''
        )
iron_bracelet.add_component(silver_bar, 1)
iron_bracelet.add_component(refined_coal, 2)
iron_bracelet.add_component(iron_bar, 2)
list_items.append(iron_bracelet)

#------------------------------------------------------------
#Candy machine (Every item already included)

caramel_apple = hayday(
        name= 'caramel apple',
        production_place = 'candy machine',
        level = 51,
        production_time = td(hours=2),
        price_sell = 255,
	img=''
        )
caramel_apple.add_component(syrup, 2)
caramel_apple.add_component(apple, 1)
list_items.append(caramel_apple)

toffee = hayday(
        name= 'toffee',
        production_place = 'candy machine',
        level = 52,
        production_time = td(hours=1, minutes=30),
        price_sell = 176,
	img=''
        )
toffee.add_component(butter, 1)
toffee.add_component(wheat, 1)
toffee.add_component(white_sugar, 1)
list_items.append(toffee)

chocolate = hayday(
        name= 'chocolate',
        production_place = 'candy machine',
        level = 54,
        production_time = td(hours=20),
        price_sell = 460,
	img=''
        )
chocolate.add_component(cacao, 3)
chocolate.add_component(cream, 1)
chocolate.add_component(white_sugar, 1)
list_items.append(chocolate)

lollipop = hayday(
        name= 'lollipop',
        production_place = 'candy machine',
        level = 57,
        production_time = td(hours=12),
        price_sell = 342,
	img=''
        )
lollipop.add_component(syrup, 1)
lollipop.add_component(cherry, 1)
lollipop.add_component(strawberry, 2)
list_items.append(lollipop)

jelly_beans = hayday(
        name= 'jelly beans',
        production_place = 'candy machine',
        level = 60,
        production_time = td(hours=24),
        price_sell = 684,
	img=''
        )
jelly_beans.add_component(blackberry_jam, 1)
jelly_beans.add_component(raspberry_jam, 1)
jelly_beans.add_component(white_sugar, 1)
list_items.append(jelly_beans)

honey_peanuts = hayday(
        name= 'honey peanuts',
        production_place = 'candy machine',
        level = 63,
        production_time = td(minutes=40),
        price_sell = 540,
	img=''
        )
honey_peanuts.add_component(honey, 1)
honey_peanuts.add_component(peanuts, 1)
list_items.append(honey_peanuts)

cottom_candy = hayday(
        name= 'cottom candy',
        production_place = 'candy machine',
        level = 75,
        production_time = td(minutes=30),
        price_sell = 226,
	img=''
        )
cottom_candy.add_component(white_sugar, 3)
cottom_candy.add_component(strawberry, 1)
list_items.append(cottom_candy)

sesame_brittle = hayday(
        name= 'sesame brittle',
        production_place = 'candy machine',
        level = 78,
        production_time = td(hours=1),
        price_sell = 270,
	img=''
        )
sesame_brittle.add_component(sesame, 3)
sesame_brittle.add_component(ginger, 1)
sesame_brittle.add_component(honey, 1)
list_items.append(sesame_brittle)
#------------------------------------------------------------
#Coffee kiosk

expresso = hayday(
       name = 'expresso',
       production_place = 'coffee kiosk',
       level = 42,
       production_time = td(minutes=5),
       price_sell = 248,
	img=''
        )
expresso.add_component(coffee_bean, 3)
expresso.add_component(white_sugar, 1)
list_items.append(expresso)

caffe_latte = hayday(
       name = 'caffe latte',
       production_place = 'coffee kiosk',
       level = 43,
       production_time = td(minutes=10),
       price_sell = 219,
	img=''
        )
caffe_latte.add_component(coffee_bean, 2)
caffe_latte.add_component(white_sugar, 1)
caffe_latte.add_component(milk, 1)
list_items.append(caffe_latte)

caffe_mocha = hayday(
       name = 'caffe mocha',
       production_place = 'coffee kiosk',
       level = 45,
       production_time = td(minutes=15),
       price_sell = 291,
	img=''
        )
caffe_mocha.add_component(coffee_bean, 1)
caffe_mocha.add_component(cream, 1)
caffe_mocha.add_component(cacao, 2)
list_items.append(caffe_mocha)

raspberry_mocha = hayday(
       name = 'raspberry mocha',
       production_place = 'coffee kiosk',
       level = 46,
       production_time = td(minutes=30),
       price_sell = 259,
	img=''
        )
raspberry_mocha.add_component(coffee_bean, 1)
raspberry_mocha.add_component(cream, 1)
raspberry_mocha.add_component(cacao, 1)
raspberry_mocha.add_component(raspberry, 1)
list_items.append(raspberry_mocha)

hot_chocolate = hayday(
       name = 'hot chocolate',
       production_place = 'coffee kiosk',
       level = 47,
       production_time = td(minutes=25),
       price_sell = 316,
	img=''
        )
hot_chocolate.add_component(cacao, 2)
hot_chocolate.add_component(white_sugar, 1)
hot_chocolate.add_component(cream, 1)
hot_chocolate.add_component(milk, 1)
list_items.append(hot_chocolate)

caramel_latte = hayday(
       name = 'caramel latte',
       production_place = 'coffee kiosk',
       level = 62,
       production_time = td(minutes=15),
       price_sell = 345,
	img=''
        )
caramel_latte.add_component(coffee_bean, 2)
caramel_latte.add_component(toffee, 1)
caramel_latte.add_component(milk, 1)
list_items.append(caramel_latte)
#------------------------------------------------------------
#Pasta maker (Every item already included)

fresh_pasta = hayday(
        name= 'fresh pasta',
        production_place = 'pasta maker',
        level = 67,
        production_time = td(minutes = 15),
        price_sell = 43,
	img=''
        )
fresh_pasta.add_component(wheat, 2)
fresh_pasta.add_component(egg, 1)
list_items.append(fresh_pasta)

rice_noodles = hayday(
        name= 'rice noddles',
        production_place = 'pasta maker',
        level = 73,
        production_time = td(minutes = 20),
        price_sell = 100,
	img=''
        )
rice_noodles.add_component(rice, 5)
list_items.append(rice_noodles)
#------------------------------------------------------------
#Soup kitchen

lobster_soup = hayday(
       name = 'lobster soup',
       production_place = 'soup kitchen',
       level = 46,
       production_time = td(hours=2,minutes=30),
       price_sell = 612,
	img=''
        )
lobster_soup.add_component(lobster_tail, 2)
lobster_soup.add_component(tomato, 1)
lobster_soup.add_component(chili_pepper, 2)
lobster_soup.add_component(cream, 1)
list_items.append(lobster_soup)

tomato_soup = hayday(
       name = 'tomato soup',
       production_place = 'soup kitchen',
       level = 47,
       production_time = td(hours=1,minutes=30),
       price_sell = 478,
	img=''
        )
tomato_soup.add_component(tomato, 2)
tomato_soup.add_component(tomato_juice, 1)
tomato_soup.add_component(chili_pepper, 1)
tomato_soup.add_component(goat_cheese, 1)
list_items.append(tomato_soup)


pumpkin_soup = hayday(
       name = 'pumpkin soup',
       production_place = 'soup kitchen',
       level = 49,
       production_time = td(hours=2),
       price_sell = 392,
	img=''
        )
pumpkin_soup.add_component(pumpkin, 3)
pumpkin_soup.add_component(cheese, 1)
pumpkin_soup.add_component(honey, 1)
pumpkin_soup.add_component(carrot, 2)
list_items.append(pumpkin_soup)

fish_soup = hayday(
       name = 'fish soup',
       production_place = 'soup kitchen',
       level = 53,
       production_time = td(hours=3),
       price_sell = 298,
	img=''
        )
fish_soup.add_component(potato, 3)
fish_soup.add_component(fish_fillet, 2)
fish_soup.add_component(milk, 1)
fish_soup.add_component(carrot, 1)
list_items.append(fish_soup)

cabbage_soup = hayday(
       name = 'cabbage soup',
       production_place = 'soup kitchen',
       level = 65,
       production_time = td(hours=1, minutes=30),
       price_sell = 270,
	img=''
        )
cabbage_soup.add_component(cabbage, 3)
cabbage_soup.add_component(bacon, 2)
cabbage_soup.add_component(potato, 2)
cabbage_soup.add_component(carrot, 2)
list_items.append(cabbage_soup)

onion_soup = hayday(
       name = 'onion soup',
       production_place = 'soup kitchen',
       level = 72,
       production_time = td(hours=2, minutes=30),
       price_sell = 327,
	img=''
        )
onion_soup.add_component(bread, 2)
onion_soup.add_component(cheese, 1)
onion_soup.add_component(onion, 3)
list_items.append(onion_soup)

noodle_soup = hayday(
       name = 'noodle soup',
       production_place = 'soup kitchen',
       level = 73,
       production_time = td(hours=2),
       price_sell = 432,
	img=''
        )
noodle_soup.add_component(carrot, 2)
noodle_soup.add_component(chili_pepper, 1)
noodle_soup.add_component(egg, 2)
noodle_soup.add_component(rice_noodles, 3)
list_items.append(noodle_soup)

potato_soup = hayday(
       name = 'potato soup',
       production_place = 'soup kitchen',
       level = 78,
       production_time = td(hours=2, minutes=30),
       price_sell = 255,
	img=''
        )
potato_soup.add_component(potato, 3)
potato_soup.add_component(onion, 2)
potato_soup.add_component(milk, 1)
list_items.append(potato_soup)

#------------------------------------------------------------
#Candle maker
strawberry_candle = hayday(
        name= 'strawberry candle',
        production_place = 'candle maker',
        level = 48,
        production_time = td(hours=2),
        price_sell = 370,
	img=''
        )

strawberry_candle.add_component(beeswax, 1)
strawberry_candle.add_component(strawberry, 2)
list_items.append(strawberry_candle)

raspberry_candle = hayday(
        name= 'raspberry candle',
        production_place = 'candle maker',
        level = 52,
        production_time = td(hours=1, minutes=45),
        price_sell = 360,
	img=''
        )

raspberry_candle.add_component(beeswax, 1)
raspberry_candle.add_component(raspberry, 2)
list_items.append(raspberry_candle)

lemon_candle = hayday(
        name= 'lemon candle',
        production_place = 'candle maker',
        level = 72,
        production_time = td(hours=2, minutes=15),
        price_sell = 457,
	img=''
        )

lemon_candle.add_component(beeswax, 1)
lemon_candle.add_component(lemon, 2)
list_items.append(lemon_candle)

#------------------------------------------------------------
#Flower shop

rustic_bouquet = hayday(
        name= 'rustic bouquet',
        production_place = 'flower shop',
        level = 49,
        production_time = td(minutes=45),
        price_sell = 208,
	img=''
        )
rustic_bouquet.add_component(wheat, 5)
rustic_bouquet.add_component(indigo, 3)
rustic_bouquet.add_component(cotton, 3)
list_items.append(rustic_bouquet)

bright_bouquet = hayday(
        name= 'brigth bouquet',
        production_place = 'flower shop',
        level = 65,
        production_time = td(minutes=20),
        price_sell = 338,
	img=''
        )
bright_bouquet.add_component(sunflower, 5)
bright_bouquet.add_component(indigo, 3)
bright_bouquet.add_component(cotton, 1)
bright_bouquet.add_component(iron_ore, 5)
list_items.append(bright_bouquet)

gracious_bouquet = hayday(
        name= 'gracious bouquet',
        production_place = 'flower shop',
        level = 73,
        production_time = td(minutes=40),
        price_sell = 500,
	img=''
        )
gracious_bouquet.add_component(cotton_fabric, 1)
gracious_bouquet.add_component(lily, 5)
gracious_bouquet.add_component(gold_ore, 1)
# bright_bouquet.add_component(diamond, 5)
list_items.append(gracious_bouquet)
#------------------------------------------------------------
#Sushi bar

sushi_roll = hayday(
        name= 'sushi roll',
        production_place = 'sushi bar',
        level = 56,
        production_time = td(hours=1),
        price_sell = 489,
	img=''
        )
sushi_roll.add_component(fish_fillet, 1)
sushi_roll.add_component(rice, 15)
sushi_roll.add_component(soy_sauce, 1)
list_items.append(sushi_roll)

lobster_sushi = hayday(
        name= 'lobster sushi',
        production_place = 'sushi bar',
        level = 59,
        production_time = td(hours=1),
        price_sell = 637,
	img=''
        )
lobster_sushi.add_component(lobster_tail, 1)
lobster_sushi.add_component(rice, 15)
lobster_sushi.add_component(soy_sauce, 1)
list_items.append(lobster_sushi)

egg_sushi = hayday(
        name= 'egg sushi',
        production_place = 'sushi bar',
        level = 66,
        production_time = td(hours=2),
        price_sell = 550,
	img=''
        )
egg_sushi.add_component(brown_sugar, 1)
egg_sushi.add_component(egg, 4)
egg_sushi.add_component(rice, 15)
egg_sushi.add_component(soy_sauce, 1)
list_items.append(egg_sushi)

big_sushi_roll = hayday(
        name= 'big sushi roll',
        production_place = 'sushi bar',
        level = 76,
        production_time = td(hours=1, minutes=30),
        price_sell = 648,
	img=''
        )
big_sushi_roll.add_component(fish_fillet, 1)
big_sushi_roll.add_component(rice, 20)
big_sushi_roll.add_component(egg, 3)
big_sushi_roll.add_component(lettuce, 5)
list_items.append(big_sushi_roll)

#------------------------------------------------------------
#Salad bar
feta_salad = hayday(
        name= 'feta salad',
        production_place = 'salad bar',
        level = 58,
        production_time = td(hours=1, minutes=30),
        price_sell = 745,
	img=''
        )
feta_salad.add_component(lettuce, 3)
feta_salad.add_component(roasted_tomatoes, 1)
feta_salad.add_component(goat_cheese, 2)
feta_salad.add_component(olive, 2)
list_items.append(feta_salad)

blt_salad = hayday(
        name= 'BLT salad',
        production_place = 'salad bar',
        level = 62,
        production_time = td(hours=1, minutes=45),
        price_sell = 723,
	img=''
        )
blt_salad.add_component(lettuce, 3)
blt_salad.add_component(roasted_tomatoes, 1)
blt_salad.add_component(bacon, 2)
blt_salad.add_component(mayonnaise, 1)
list_items.append(blt_salad)

seafood_salad = hayday(
        name= 'seafood salad',
        production_place = 'salad bar',
        level = 64,
        production_time = td(hours=2),
        price_sell = 763,
	img=''
        )
seafood_salad.add_component(lettuce, 3)
seafood_salad.add_component(fish_fillet, 1)
seafood_salad.add_component(lobster_tail, 1)
seafood_salad.add_component(mayonnaise, 1)
list_items.append(seafood_salad)

pasta_salad = hayday(
        name= 'pasta salad',
        production_place = 'salad bar',
        level = 67,
        production_time = td(hours=2, minutes=30),
        price_sell = 759,
	img=''
        )
pasta_salad.add_component(fresh_pasta, 4)
pasta_salad.add_component(lemon, 2)
pasta_salad.add_component(olive_oil, 1)
pasta_salad.add_component(tomato, 2)
list_items.append(pasta_salad)

veggie_platter = hayday(
        name= 'veggie platter',
        production_place = 'salad bar',
        level = 74,
        production_time = td(hours=2),
        price_sell = 266,
	img=''
        )
veggie_platter.add_component(bell_pepper, 2)
veggie_platter.add_component(carrot, 2)
veggie_platter.add_component(tomato, 2)
veggie_platter.add_component(cream, 1)
list_items.append(veggie_platter)

coleslaw = hayday(
        name= 'coleslaw',
        production_place = 'salad bar',
        level = 75,
        production_time = td(hours=1, minutes=15),
        price_sell = 468,
	img=''
        )
coleslaw.add_component(cabbage, 3)
coleslaw.add_component(carrot, 2)
coleslaw.add_component(mayonnaise, 1)
list_items.append(coleslaw)

beetroot_salad = hayday(
        name= 'beetroot salad',
        production_place = 'salad bar',
        level = 76,
        production_time = td(minutes=45),
        price_sell = 234,
	img=''
        )
beetroot_salad.add_component(beetroot, 3)
beetroot_salad.add_component(goat_cheese, 2)
list_items.append(beetroot_salad)

summer_rolls = hayday(
        name= 'summer rolls',
        production_place = 'salad bar',
        level = 78,
        production_time = td(hours=1),
        price_sell = 316
        )
summer_rolls.add_component(rice_noodles, 2)
summer_rolls.add_component(carrot, 2)
summer_rolls.add_component(lettuce, 1)
summer_rolls.add_component(chili_pepper, 1)
list_items.append(summer_rolls)

#------------------------------------------------------------
#Sandwich bar

veggie_bagel = hayday(
        name= 'veggie bagel',
        production_place = 'sandwich bar',
        level = 61,
        production_time = td(minutes=40),
        price_sell = 532
        )
veggie_bagel.add_component(bread, 2)
veggie_bagel.add_component(tomato, 2)
veggie_bagel.add_component(lettuce, 3)
veggie_bagel.add_component(olive_oil, 1)
list_items.append(veggie_bagel)

bacon_toast = hayday(
        name= 'bacon toast',
        production_place = 'sandwich bar',
        level = 65,
        production_time = td(hours=1, minutes=40),
        price_sell = 648
        )
bacon_toast.add_component(bread, 2)
bacon_toast.add_component(bacon, 2)
bacon_toast.add_component(lettuce, 3)
bacon_toast.add_component(mayonnaise, 1)
list_items.append(bacon_toast)

egg_sandwich = hayday(
        name= 'egg sandwich',
        production_place = 'sandwich bar',
        level = 66,
        production_time = td(hours=1, minutes=20),
        price_sell = 583
        )
egg_sandwich.add_component(bread, 2)
egg_sandwich.add_component(egg, 2)
egg_sandwich.add_component(lettuce, 3)
egg_sandwich.add_component(mayonnaise, 1)
list_items.append(egg_sandwich)

honey_toast = hayday(
        name= 'honey toast',
        production_place = 'sandwich bar',
        level = 69,
        production_time = td(hours=1),
        price_sell = 255
        )
honey_toast.add_component(bread, 1)
honey_toast.add_component(egg, 1)
honey_toast.add_component(milk, 1)
honey_toast.add_component(honey, 1)
list_items.append(honey_toast)

peanut_butter_and_jelly_sandwich = hayday(
        name= 'peanut butter and jelly sandwich',
        production_place = 'sandwich bar',
        level = 71,
        production_time = td(minutes=25),
        price_sell = 601
        )
peanut_butter_and_jelly_sandwich.add_component(bread, 2)
peanut_butter_and_jelly_sandwich.add_component(raspberry_jam, 1)
peanut_butter_and_jelly_sandwich.add_component(peanuts, 1)
list_items.append(peanut_butter_and_jelly_sandwich)

cucumber_sandwich = hayday(
        name= 'cucumber sandwich',
        production_place = 'sandwich bar',
        level = 79,
        production_time = td(minutes=35),
        price_sell = 464
        )
cucumber_sandwich.add_component(cucumber, 2)
cucumber_sandwich.add_component(mayonnaise, 1)
cucumber_sandwich.add_component(bread, 2)
list_items.append(cucumber_sandwich)


#------------------------------------------------------------
#Smoothie Mixer

berry_smoothie = hayday(
                name = 'berry smoothie',
                production_place = 'smoothie mixer',
                level = 64,
                production_time = td(hours=1, minutes=15),
                price_sell = 547
        )
berry_smoothie.add_component(raspberry, 3)
berry_smoothie.add_component(strawberry, 3)
berry_smoothie.add_component(blackberry, 3)
list_items.append(berry_smoothie)

green_smoothie = hayday(
                name = 'green smoothie',
                production_place = 'smoothie mixer',
                level = 66,
                production_time = td(minutes=45),
                price_sell = 320
        )
green_smoothie.add_component(lettuce, 5)
green_smoothie.add_component(lemon, 1)
green_smoothie.add_component(apple, 3)
list_items.append(green_smoothie)

yogurt_smoothie = hayday(
                name = 'yogurt smoothie',
                production_place = 'smoothie mixer',
                level = 70,
                production_time = td(hours=1),
                price_sell = 349
        )
yogurt_smoothie.add_component(cream, 1)
yogurt_smoothie.add_component(raspberry, 2)
yogurt_smoothie.add_component(cherry, 1)
yogurt_smoothie.add_component(white_sugar, 1)
list_items.append(yogurt_smoothie)

cucumber_smoothie = hayday(
                name = 'cucumber smoothie',
                production_place = 'smoothie mixer',
                level = 70,
                production_time = td(minutes=40),
                price_sell = 266
        )
cucumber_smoothie.add_component(cucumber, 3)
cucumber_smoothie.add_component(honey, 1)
cucumber_smoothie.add_component(pineapple, 3)
list_items.append(cucumber_smoothie)
#------------------------------------------------------------
# Wok kitchen

fried_rice = hayday(
                name = 'fried rice',
                production_place = 'wok kitchen',
                level = 69,
                production_time = td(hours=1),
                price_sell = 205
        )
fried_rice.add_component(rice, 5)
fried_rice.add_component(egg, 5)
list_items.append(fried_rice)

spicy_fish = hayday(
                name = 'spicy fish',
                production_place = 'wok kitchen',
                level = 79,
                production_time = td(hours=1, minutes=30),
                price_sell = 543
        )
spicy_fish.add_component(fish_fillet, 1)
spicy_fish.add_component(chili_pepper, 3)
spicy_fish.add_component(garlic, 5)
spicy_fish.add_component(olive_oil, 1)
list_items.append(spicy_fish)

#------------------------------------------------------------
# Hat maker

cloche_hat = hayday(
                name = 'cloche hat',
                production_place = 'hat maker',
                level = 70,
                production_time = td(hours=2),
                price_sell = 468
        )
cloche_hat.add_component(strawberry, 2)
cloche_hat.add_component(wool, 6)
list_items.append(cloche_hat)

top_hat = hayday(
                name = 'top hat',
                production_place = 'hat maker',
                level = 72,
                production_time = td(hours=3, minutes=30),
                price_sell = 619
        )
top_hat.add_component(cotton_fabric, 3)
top_hat.add_component(refined_coal, 1)
top_hat.add_component(duck_feather, 1)
list_items.append(top_hat)

sun_hat = hayday(
                name = 'sun hat',
                production_place = 'hat maker',
                level = 74,
                production_time = td(hours=2, minutes=30),
                price_sell = 558
        )
sun_hat.add_component(wool, 3)
sun_hat.add_component(indigo, 1)
sun_hat.add_component(duck_feather, 2)
sun_hat.add_component(raspberry, 1)
list_items.append(sun_hat)
#------------------------------------------------------------
# Pasta Kitchen

gnocchi = hayday(
    name = 'gnocchi',
    production_place = 'pasta kitchen',
    level= 72,
    production_time = td(hours=1, minutes=20),
    price_sell = 475
)
gnocchi.add_component(potato, 4)
gnocchi.add_component(tomato, 3)
gnocchi.add_component(wheat, 2)
gnocchi.add_component(butter, 2)
list_items.append(gnocchi)

veggie_lasagna = hayday(
    name = 'veggie lasagna',
    production_place = 'pasta kitchen',
    level= 74,
    production_time = td(hours=1, minutes=40),
    price_sell = 532
)
veggie_lasagna.add_component(carrot, 1)
veggie_lasagna.add_component(cheese, 1)
veggie_lasagna.add_component(tomato_sauce, 1)
veggie_lasagna.add_component(fresh_pasta, 3)
list_items.append(veggie_lasagna)

lobster_pasta = hayday(
    name = 'lobster pasta',
    production_place = 'pasta kitchen',
    level= 79,
    production_time = td(hours=2),
    price_sell = 637
)
lobster_pasta.add_component(lobster_tail, 1)
lobster_pasta.add_component(cream, 2)
lobster_pasta.add_component(fresh_pasta, 3)
lobster_pasta.add_component(tomato, 4)
list_items.append(lobster_pasta)

#------------------------------------------------------------
# Hot Dog Stand

hot_dog = hayday(
    name = 'hot dog',
    production_place = 'hot dog stand',
    level= 75,
    production_time = td(minutes=30),
    price_sell = 370
)
hot_dog.add_component(bacon, 2)
hot_dog.add_component(bread, 1)
hot_dog.add_component(tomato_sauce, 1)
list_items.append(hot_dog)

tofu_dog = hayday(
    name = 'tofu dog',
    production_place = 'hot dog stand',
    level= 76,
    production_time = td(minutes=45),
    price_sell = 367
)
tofu_dog.add_component(lettuce, 3)
tofu_dog.add_component(soybean, 6)
tofu_dog.add_component(tomato, 4)
list_items.append(tofu_dog)

corn_dog = hayday(
    name = 'corn dog',
    production_place = 'hot dog stand',
    level= 78,
    production_time = td(hours=1),
    price_sell = 529
)
corn_dog.add_component(bacon, 4)
corn_dog.add_component(corn, 4)
corn_dog.add_component(olive_oil, 1)
list_items.append(corn_dog)

#------------------------------------------------------------
# Donut Maker

plain_donut = hayday(
    name = 'plain donut',
    production_place = 'donut maker',
    level= 76,
    production_time = td(minutes=15),
    price_sell = 129
)
plain_donut.add_component(milk, 1)
plain_donut.add_component(white_sugar, 1)
plain_donut.add_component(egg, 1)
plain_donut.add_component(wheat, 3)
list_items.append(plain_donut)

sprinkled_donut = hayday(
    name = 'sprinkled donut',
    production_place = 'donut maker',
    level= 79,
    production_time = td(minutes=20),
    price_sell = 313
)
sprinkled_donut.add_component(plain_donut, 1)
sprinkled_donut.add_component(cacao, 2)
list_items.append(sprinkled_donut)

#------------------------------------------------------------
# Taco Kitchen

taco = hayday(
    name = 'taco',
    production_place = 'taco kitchen',
    level= 77,
    production_time = td(minutes=45),
    price_sell = 396
)
taco.add_component(corn_bread, 1)
taco.add_component(bacon, 1)
taco.add_component(salsa, 1)
list_items.append(taco)

fish_taco = hayday(
    name = 'fish taco',
    production_place = 'taco kitchen',
    level= 79,
    production_time = td(hours=1, minutes=30),
    price_sell = 392
)
fish_taco.add_component(chili_pepper, 2)
fish_taco.add_component(corn_bread, 2)
fish_taco.add_component(fish_fillet, 1)
fish_taco.add_component(lemon, 1)
list_items.append(fish_taco)
