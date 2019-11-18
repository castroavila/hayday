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
            time_production,    #Time of production
            price_sell          #Max. price for selling
            ):
#list to store individual components
        self.name = name
        self.production_place = production_place
        self.time_production = time_production
        self.price_sell = price_sell
        self.components = []

############################################################
#Function to add components the item is made of
    def add_component(self,component_name,number_of_components):
        self.components.append([component_name, number_of_components])

############################################################
#Function to compute the production price: sum of individual selling prices of each component
    def get_production_price(self):
#       TODO
        pass

############################################################
#Function to compute the time is spending producing every component the item is made of
    def get_time_production_components(self):
#       TODO
        pass




