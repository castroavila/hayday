#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : hayday.py
#

"""

"""
import pandas as pd

class hayday(object):

    def __init__(self,
            name,               #item's name
            production_place,   #Place of production
            level,              # Level at which its production is allowed from
            production_time,    #Time of production
            price_sell,          #Max. price for selling
            img                 # Item's image path
            ):
#list to store individual components
        self.name = name
        self.production_place = production_place
        self.production_time = production_time
        self.price_sell = price_sell
        self.components = []
        self.img  = img

#-----------------------------------------------------------
#Function to add components the item is made of
    def add_component(self,component_name,number_of_components):
        self.components.append([component_name, number_of_components])
#-----------------------------------------------------------
#Function to compute the production price: sum of individual selling prices of each component
    def get_production_price(self):
        production_price = 0.
        for item,quantity in self.components:
            production_price += item.price_sell*quantity

        if (self.name == "pig food" or self.name == "cow food" or self.name == "chicken food"):
            return production_price/3.

        return production_price

#-----------------------------------------------------------
    def get_components(self):
        for item, quantity in self.components:
            print("{:20s} -----> {:2d}".format(item.name,quantity))
#Function to compute the time is spending producing every component the item is made of
    def get_production_time_components(self):
#       TODO
        pass
#------------------------------------------------------------
# Return item's production time in hours
    def get_production_time(self):
        return self.production_time.days*24 + self.production_time.seconds/3600.

#------------------------------------------------------------
#Compute profit = price_sell - production_price
    def get_profit(self):
        return self.price_sell - self.get_production_price()



