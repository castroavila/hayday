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
############################################################
#def __init__(self,
#        name,               
#        production_place,   
#        time_production,    
#        price_sell          
#        ):
#Crops

wheat = hayday(
       name = "wheat",
       production_place = "farm",
       level = 1,
       time_production = td(minutes=2),
       price_sell = 3
        )
list_items.append(wheat)

corn = hayday(
       name = "corn",
       production_place = "farm",
       level = 2,
       time_production = td(minutes=5),
       price_sell = 7
        )
list_items.append(corn)

soybean = hayday(
       name = "soybean",
       production_place = "farm",
       level = 5,
       time_production = td(minutes=20),
       price_sell = 10
        )
list_items.append(soybean)

sugarcane = hayday(
       name = "sugarcane",
       production_place = "farm",
       level = 7,
       time_production = td(minutes=30),
       price_sell = 14
        )
list_items.append(sugarcane)

carrot = hayday(
       name = "carrot",
       production_place = "farm",
       level = 9,
       time_production = td(minutes=10),
       price_sell = 7
        )
list_items.append(carrot)

indigo = hayday(
       name = "indigo",
       production_place = "farm",
       level = 13,
       time_production = td(hours=2),
       price_sell = 25
        )
list_items.append(indigo)

apple = hayday(
       name = "apple",
       production_place = "farm",
       level = 15,
       time_production = td(hours=16),
       price_sell = 39
        )
list_items.append(apple)

pumpkin  = hayday(
       name = "pumpkin",
       production_place = "farm",
       level = 15,
       time_production = td(hours=3),
       price_sell = 32
        )
list_items.append(pumpkin)

cotton = hayday(
       name = "cotton",
       production_place = "farm",
       level = 18,
       time_production = td(hours=2,minutes=30),
       price_sell = 28
        )
list_items.append(cotton)

raspberry = hayday(
       name = "raspberry",
       production_place = "farm",
       level = 19,
       time_production = td(hours=18),
       price_sell = 46
        )
list_items.append(raspberry)

cherry = hayday(
       name = "cherry",
       production_place = "farm",
       level = 22,
       time_production = td(hours=24+3),
       price_sell = 68
        )
list_items.append(cherry)

chili_pepper = hayday(
       name = "chili pepper",
       production_place = "farm",
       level = 25,
       time_production = td(hours=4),
       price_sell = 36
        )
list_items.append(chili_pepper)

blackberry = hayday(
       name = "blackberry",
       production_place = "farm",
       level = 26,
       time_production = td(hours=24+8),
       price_sell = 82
        )
list_items.append(blackberry)

tomato = hayday(
       name = "tomato",
       production_place = "farm",
       level = 30,
       time_production = td(hours=6),
       price_sell = 43
        )
list_items.append(tomato)

strawberry = hayday(
       name = "strawberry",
       production_place = "farm",
       level = 34,
       time_production = td(hours=8),
       price_sell = 50
        )
list_items.append(strawberry)

potato = hayday(
       name = "potato",
       production_place = "farm",
       level = 35,
       time_production = td(hours=3, minutes=40),
       price_sell = 36
        )
list_items.append(potato)

cacao = hayday(
       name = "cacao",
       production_place = "farm",
       level = 36,
       time_production = td(hours=24+11),
       price_sell = 86
        )
list_items.append(cacao)

coffee_bean = hayday(
       name = "coffee bean",
       production_place = "farm",
       level = 42,
       time_production = td(hours=24),
       price_sell = 64
        )
list_items.append(coffee_bean)

############################################################
#Animals food

chicken_food = hayday(
       name = "chicken food",
       production_place = "feed mill",
       level = 3,
       time_production = td(minutes=5),
       price_sell = 7.
        )
chicken_food.add_component(wheat,2)
chicken_food.add_component(corn,1)
list_items.append(chicken_food)

cow_food = hayday(
       name = "cow food",
       production_place = "feed mill",
       level = 6,
       time_production = td(minutes=10),
       price_sell = 14
        )
cow_food.add_component(soybean,2)
cow_food.add_component(corn,1)
list_items.append(cow_food)

#TODO
pig_food = hayday(
       name = "pig food",
       production_place = "feed mill",
       level = 10,
       time_production = td(minutes=10),
       price_sell = 14
        )
pig_food.add_component(soybean,1)
pig_food.add_component(carrot,2)
list_items.append(pig_food)

#TODO
sheep_food = hayday(
       name = "sheep food",
       production_place = "feed mill",
       level = 16,
       time_production = td(minutes=10),
       price_sell = 14
        )
sheep_food.add_component(soybean,1)
sheep_food.add_component(wheat,3)
list_items.append(sheep_food)

#TODO
goat_food = hayday(
       name = "goat food",
       production_place = "feed mill",
       level = 32,
       time_production = td(minutes=10),
       price_sell = 14
        )
goat_food.add_component(corn,1)
goat_food.add_component(corn,1)
goat_food.add_component(carrot,2)
list_items.append(goat_food)

############################################################
#Animals
egg = hayday(
       name = "egg",
       production_place = "farm",
       level = 1,
       time_production = td(minutes=20),
       price_sell = 18
        )
egg.add_component(chicken_food,1)
list_items.append(egg)

milk = hayday(
       name = "milk",
       production_place = "farm",
       level = 6,
       time_production = td(hours=1),
       price_sell = 32
        )
milk.add_component(cow_food,1)
list_items.append(milk)

goat_milk = hayday(
       name = "goat milk",
       production_place = "farm",
       level = 32,
       time_production = td(hours=8),
       price_sell = 64
        )
goat_milk.add_component(goat_food,1)
list_items.append(goat_milk)

honeycomb = hayday(
       name = "honeycomb",
       production_place = "farm",
       level = 39,
       time_production = td(minutes=35),
       price_sell = 68
        )
list_items.append(honeycomb)

honey = hayday(
       name = "honey",
       production_place = "honey extractor",
       level = 39,
       time_production = td(minutes=20),
       price_sell = 154 
        )
honey.add_component(honeycomb,2)
list_items.append(honey)

bacon = hayday(
       name = "bacon",
       production_place = "farm",
       level = 10,
       time_production = td(hours=4),
       price_sell = 50
        )
bacon.add_component(pig_food,1)
list_items.append(bacon)

wool = hayday(
       name = "wool",
       production_place = "farm",
       level = 16,
       time_production = td(hours=6),
       price_sell = 54
        )
wool.add_component(sheep_food,1)
list_items.append(wool)



############################################################
#Fish 
fish_fillet = hayday(
       name = "fish fillet",
       production_place = "fishing lake",
       level = 27,
       time_production = td(minutes=0),
       price_sell = 54
        )
list_items.append(fish_fillet)

lobster_tail = hayday(
       name = "lobster tail",
       production_place = "fishing lake",
       level = 44,
       time_production = td(hours=6),
       price_sell = 201
        )
list_items.append(lobster_tail)

############################################################
#Sugar mill
brown_sugar = hayday(
       name = "brown sugar",
       production_place = "sugar mill",
       level = 7,
       time_production = td(minutes=20),
       price_sell = 32
        )
brown_sugar.add_component(sugarcane,1)
list_items.append(brown_sugar)

white_sugar = hayday(
       name = "white sugar",
       production_place = "sugar mill",
       level = 13,
       time_production = td(minutes=40),
       price_sell = 50
        )
brown_sugar.add_component(sugarcane,2)
list_items.append(white_sugar)

syrup = hayday(
       name = "syrup",
       production_place = "sugar mill",
       level = 18,
       time_production = td(hours=1,minutes=30),
       price_sell = 90
        )
brown_sugar.add_component(sugarcane,4)
list_items.append(syrup)
############################################################
#Dairy
cream = hayday(
       name = "cream",
       production_place = "dairy",
       level = 6,
       time_production = td(minutes=20),
       price_sell = 50
        )
cream.add_component(milk,1)
list_items.append(cream)

butter = hayday(
       name = "butter",
       production_place = "dairy",
       level = 9,
       time_production = td(minutes=30),
       price_sell = 82
        )
butter.add_component(milk,2)
list_items.append(butter)

cheese = hayday(
       name = "cheese",
       production_place = "dairy",
       level = 12,
       time_production = td(hours=1),
       price_sell = 122
        )
cheese.add_component(milk,3)
list_items.append(cheese)

goat_cheese = hayday(
       name = "goat cheese",
       production_place = "dairy",
       level = 33,
       time_production = td(hours=1,minutes=30),
       price_sell = 162
        )
goat_cheese.add_component(goat_milk,2)
list_items.append(goat_cheese)




############################################################

#Bakery 
bread = hayday(
       name = "bread",
       production_place = "bakery",
       level = 2,
       time_production = td(minutes=5),
       price_sell = 21
        )
bread.add_component(wheat,3)
list_items.append(bread)

corn_bread = hayday(
       name = "corn bread",
       production_place = "bakery",
       level = 7,
       time_production = td(minutes=30),
       price_sell = 72
        )
bread.add_component(wheat,3)
list_items.append(corn_bread)

cookie = hayday(
       name = "cookie",
       production_place = "bakery",
       level = 10,
       time_production = td(hours=1),
       price_sell = 104
        )
cookie.add_component(wheat,2)
cookie.add_component(egg,2)
cookie.add_component(brown_sugar,1)
list_items.append(cookie)

raspberry_muffin = hayday(
       name = "raspberry muffin",
       production_place = "bakery",
       
       level = 19,
       time_production = td(minutes=45),
       price_sell =140
        )
raspberry_muffin.add_component(wheat,2)
raspberry_muffin.add_component(egg,1)
raspberry_muffin.add_component(raspberry,2)
list_items.append(raspberry_muffin)

blackbery_muffin = hayday(
       name = "blackberry muffin",
       production_place = "bakery",
       level = 26,
       time_production = td(minutes=45),
       price_sell = 226
        )
blackbery_muffin.add_component(wheat,1)
blackbery_muffin.add_component(egg,2)
blackbery_muffin.add_component(blackberry,2)
list_items.append(blackbery_muffin)

pizza = hayday(
       name = "pizza",
       production_place = "bakery",
       level = 33,
       time_production = td(minutes=15),
       price_sell = 190
        )
pizza.add_component(wheat,2)
pizza.add_component(tomato,1)
pizza.add_component(cheese,2)
list_items.append(pizza)

spicy_pizza = hayday(
       name = "spicy pizza",
       production_place = "bakery",
       level = 37,
       time_production = td(minutes=15),
       price_sell = 226
        )
spicy_pizza.add_component(wheat,2)
spicy_pizza.add_component(tomato,1)
spicy_pizza.add_component(cheese,1)
spicy_pizza.add_component(chili_pepper,1)
list_items.append(spicy_pizza)

potato_bread = hayday(
       name = "potato bread",
       production_place = "bakery",
       level = 39,
       time_production = td(minutes=45),
       price_sell = 284
        )
potato_bread.add_component(potato,2)
potato_bread.add_component(white_sugar,1)
potato_bread.add_component(egg,3)
potato_bread.add_component(butter,1)
list_items.append(potato_bread)

frutti_di_mare_pizza = hayday(
       name = "frutti di mare pizza",
       production_place = "bakery",
       level = 45,
       time_production = td(minutes=15),
       price_sell = 403
        )
frutti_di_mare_pizza.add_component(wheat,2)
frutti_di_mare_pizza.add_component(fish_fillet,1)
frutti_di_mare_pizza.add_component(lobster_tail,1)
frutti_di_mare_pizza.add_component(cheese,1)
list_items.append(frutti_di_mare_pizza)

#banana_bread = hayday(
#       name = "banana bread",
#       production_place = "bakery",
#       level = 91,
#       time_production = td(minutes=30),
#       price_sell = 424
#        )
#banana_bread.add_component(wheat,2)
#list_items.append(banana_bread)

############################################################
#Popcorn pot

popcorn = hayday(
       name = "popcorn",
       production_place = "popcorn pot",
       level = 8,
       time_production = td(minutes=30),
       price_sell = 32
        )
popcorn.add_component(corn,2)
list_items.append(popcorn)

buttered_popcorn = hayday(
       name = "buttered popcorn",
       production_place = "popcorn pot",
       level = 16,
       time_production = td(minutes=60),
       price_sell = 126
        )
buttered_popcorn.add_component(corn,2)
buttered_popcorn.add_component(butter,1)
list_items.append(buttered_popcorn)

chili_popcorn = hayday(
       name = "chili popcorn",
       production_place = "popcorn pot",
       level = 25,
       time_production = td(hours=2),
       price_sell = 122
        )
chili_popcorn.add_component(corn,2)
chili_popcorn.add_component(chili_pepper,2)
list_items.append(chili_popcorn)

honey_popcorn = hayday(
       name = "honey popcorn",
       production_place = "popcorn pot",
       level = 40,
       time_production = td(hours=1,minutes=30),
       price_sell = 360
        )
honey_popcorn.add_component(corn,2)
honey_popcorn.add_component(honey,2)
list_items.append(honey_popcorn)

chocolate_popcorn = hayday(
       name = "chocolate popcorn",
       production_place = "potcorn pot",
       level = 44,
       time_production = td(hours=2,minutes=30),
       price_sell = 248
        )
chocolate_popcorn.add_component(corn,2)
chocolate_popcorn.add_component(cacao,2)
list_items.append(chocolate_popcorn)

############################################################
#BBQ grill

pancake = hayday(
       name = "pancake",
       production_place = "bbq grill",
       level = 9,
       time_production = td(minutes=30),
       price_sell = 108
        )
pancake.add_component(egg,3)
pancake.add_component(brown_sugar,1)
list_items.append(pancake)

bacon_and_eggs = hayday(
       name = "bakon and eggs",
       production_place = "bbq grill",
       level = 11,
       time_production = td(minutes=60),
       price_sell = 201
        )
bacon_and_eggs.add_component(egg,4)
bacon_and_eggs.add_component(bacon,2)
list_items.append(bacon_and_eggs)

hamburger = hayday(
       name = "hamburger",
       production_place = "bbq grill",
       level = 18,
       time_production = td(hours=2),
       price_sell = 180
        )
hamburger.add_component(bread,2)
hamburger.add_component(bacon,2)
list_items.append(hamburger)

fish_burger = hayday(
       name = "fish burger",
       production_place = "bbq grill",
       level = 27,
       time_production = td(hours=2),
       price_sell = 226
        )
fish_burger.add_component(fish_fillet,2)
fish_burger.add_component(bread,2)
fish_burger.add_component(chili_pepper,1)
list_items.append(fish_burger)

roasted_tomatoes = hayday(
       name = "roasted tomatoes",
       production_place = "bbq grill",
       level = 30,
       time_production = td(hours=1, minutes=30),
       price_sell = 118
        )
roasted_tomatoes.add_component(tomato,2)
list_items.append(roasted_tomatoes)

baked_potato = hayday(
       name = "baked potato",
       production_place = "bbq grill",
       level = 35,
       time_production = td(minutes=35),
       price_sell = 298
        )
baked_potato.add_component(potato,2)
baked_potato.add_component(chili_pepper,1)
baked_potato.add_component(cream,1)
baked_potato.add_component(cheese,1)
list_items.append(baked_potato)

fish_and_chips = hayday(
       name = "fish and chips",
       production_place = "bbq grill",
       level = 41,
       time_production = td(hours=1,minutes=30),
       price_sell = 244
        )
fish_and_chips.add_component(fish_fillet,2)
fish_and_chips.add_component(potato,3)
list_items.append(fish_and_chips)

lobster_skewer = hayday(
       name = "lobster skewer",
       production_place = "bbq grill",
       level = 48,
       time_production = td(minutes=40),
       price_sell = 417
        )
lobster_skewer.add_component(lobster_tail,1)
lobster_skewer.add_component(chili_pepper,1)
lobster_skewer.add_component(honey,1)
list_items.append(lobster_skewer)

############################################################
#Pie oven

carrot_pie = hayday(
       name = "carrot pie",
       production_place = "pie oven",
       level = 14,
       time_production = td(hours=1),
       price_sell = 82
        )
carrot_pie.add_component(carrot,3)
carrot_pie.add_component(wheat,2)
carrot_pie.add_component(egg,1)
list_items.append(carrot_pie)

pumpkin_pie = hayday(
       name = "pumpkin pie",
       production_place = "pie oven",
       level = 15,
       time_production = td(hours=2),
       price_sell = 158
        )
pumpkin_pie.add_component(pumpkin,3)
pumpkin_pie.add_component(wheat,2)
pumpkin_pie.add_component(egg,1)
list_items.append(pumpkin_pie)

bacon_pie = hayday(
       name = "bacon pie",
       production_place = "pie oven",
       level = 18,
       time_production = td(hours=3),
       price_sell = 219
        )
bacon_pie.add_component(bacon,3)
bacon_pie.add_component(wheat,2)
bacon_pie.add_component(egg,1)
list_items.append(bacon_pie)

apple_pie = hayday(
       name = "apple pie",
       production_place = "pie oven",
       level = 28,
       time_production = td(hours=2,minutes=30),
       price_sell = 270
        )
apple_pie.add_component(apple,3)
apple_pie.add_component(wheat,2)
apple_pie.add_component(egg,1)
apple_pie.add_component(syrup,1)
list_items.append(apple_pie)

fish_pie = hayday(
       name = "fish pie",
       production_place = "pie oven",
       level = 28,
       time_production = td(hours=2),
       price_sell = 226
        )
fish_pie.add_component(fish_fillet,3)
fish_pie.add_component(wheat,2)
fish_pie.add_component(egg,1)
list_items.append(fish_pie)

feta_pie = hayday(
       name = "feta pie",
       production_place = "pie oven",
       level = 34,
       time_production = td(hours=1,minutes=30),
       price_sell = 223
        )
feta_pie.add_component(goat_cheese,1)
feta_pie.add_component(wheat,2)
feta_pie.add_component(egg,1)
list_items.append(feta_pie)

casserole = hayday(
       name = "casserole",
       production_place = "pie oven",
       level = 36,
       time_production = td(hours=2),
       price_sell = 367
        )
casserole.add_component(potato,2)
casserole.add_component(bacon,2)
casserole.add_component(egg,2)
casserole.add_component(cheese,1)
list_items.append(casserole)

shepherds_pie = hayday(
       name = "shepherds pie",
       production_place = "pie oven",
       level = 39,
       time_production = td(hours=1,minutes=40),
       price_sell = 280
        )
shepherds_pie.add_component(potato,2)
shepherds_pie.add_component(bacon,2)
shepherds_pie.add_component(carrot,2)
shepherds_pie.add_component(pumpkin,2)
list_items.append(shepherds_pie)

############################################################
#Loom
sweater = hayday(
       name = "sweater",
       production_place = "loom",
       level = 17,
       time_production = td(hours=2),
       price_sell = 158
        )
sweater.add_component(wool,2)
list_items.append(sweater)

cotton_fabric = hayday(
       name = "cotton fabric",
       production_place = "loom",
       level = 18,
       time_production = td(minutes=30),
       price_sell = 108
        )
cotton_fabric.add_component(cotton,3)
list_items.append(cotton_fabric)

blue_woolly_hat = hayday(
       name = "blue woolly hat",
       production_place = "loom",
       level = 19,
       time_production = td(hours=1),
       price_sell = 111
        )
blue_woolly_hat.add_component(wool,1)
blue_woolly_hat.add_component(indigo,1)
list_items.append(blue_woolly_hat)

red_scarf = hayday(
       name = "red scarf",
       production_place = "loom",
       level = 48,
       time_production = td(hours=2,minutes=30),
       price_sell = 288
        )
red_scarf.add_component(wool,2)
red_scarf.add_component(strawberry,2)
list_items.append(red_scarf)

############################################################
#Sewing machine

cotton_shirt = hayday(
       name = "cotton shirt",
       production_place = "sewing machine",
       level = 19,
       time_production = td(minutes=45),
       price_sell = 241
        )
cotton_shirt.add_component(cotton_fabric,2)
list_items.append(cotton_shirt)

wooly_chaps = hayday(
       name = "wooly chaps",
       production_place = "sewing machine",
       level = 21,
       time_production = td(hours=1,minutes=30),
       price_sell = 309
        )
cotton_shirt.add_component(cotton_fabric,1)
cotton_shirt.add_component(wool,3)
list_items.append(wooly_chaps)










