#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file             : hayday.py
#

"""

"""
import pandas as pd


class hayday(object):
    def __init__(
        self, name, production_place, level, production_time, price_sell, img
    ):
        # list to store individual components
        self.name = name
        self.production_place = production_place
        self.production_time = production_time
        self.price_sell = price_sell
        self.components = {}
        self.n_components = 0
        self.img = img

    # -----------------------------------------------------------
    # Function to add components the item is made of
    def add_component(self, component_name, number_of_components):
        self.components[component_name] = number_of_components
        self.n_components += 1

    # -----------------------------------------------------------
    # Function to compute the production price: sum of individual selling prices of each component
    def get_production_price(self):
        production_price = 0.0
        for item, quantity in self.components.items():
            production_price += item.price_sell * quantity

        if (
            self.name == "pig food"
            or self.name == "cow food"
            or self.name == "chicken food"
        ):
            return production_price / 3.0

        return production_price

    # -----------------------------------------------------------
    def get_components(self):
        for item, quantity in self.components.items():
            print("{:20s} -----> {:2d}".format(item.name, quantity))

    # Function to compute the time is spending producing every component the item is made of
    def get_production_time_components(self):
        #       TODO
        pass

    # ------------------------------------------------------------
    # Return item's production time in hours
    def get_production_time(self):
        return (
            self.production_time.days * 24
            + self.production_time.seconds / 3600.0
        )

    # ------------------------------------------------------------
    # Compute profit = price_sell - production_price
    def get_profit(self):
        return self.price_sell - self.get_production_price()

    def get_profit_per_time(self):
        '''
        Return profit per hour.
        '''
        return self.get_profit() / (
            self.production_time.total_seconds() / 3600.0
        )

    def summary(self):
        '''
        Print summary on item.
        '''
        print(f'name: {self.name}')
        print(f'production time (h): {self.get_production_time()}')
        print(f'price sell: {self.price_sell}')
        print(f'production price: {self.get_production_price()}')
        print('Components:')
        self.get_components()
