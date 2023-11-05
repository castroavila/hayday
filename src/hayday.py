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
        """Constructor to describe each item in the game.

        Parameters
        ----------
        name :  str
            Item's name.
        production_place : str
            Place (machine) where item is produced.
        level : int
            Minimum level required to achive in order to be able to produce the item.
        production_time :  datetime.timedelta
            How long takes produce item in `production_place`.
        price_sell : int
            Maximum price allowed to sell item in market.
        img : str
            Path to image showing item.

        Returns
        -------

        """
        # list to store individual components
        self.name = name
        self.production_place = production_place
        self.production_time = production_time
        self.price_sell = price_sell
        self.components = {}
        self.n_components = 0
        self.img = img

    def add_component(self, component_name, number_of_components):
        """Add components the item is made of.

        Parameters
        ----------
        component_name : str
            Component's name.
        number_of_components : int
            How many items from this given component are needed.

        Returns
        -------
        TODO

        """
        self.components[component_name] = number_of_components
        self.n_components += 1

    def get_production_price(self):
        """Return production price as the sum of maximum selling price per
        individual (and how many) component.
        Returns
        -------
        price : int

        """
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

    def get_components(self):
        """Print info on components.
        Returns
        -------
        TODO

        """
        for item, quantity in self.components.items():
            print("{:20s} -----> {:2d}".format(item.name, quantity))

    def get_production_time(self):
        """Item's production time in hours.
        Returns
        -------
        float

        """
        return (
            self.production_time.days * 24
            + self.production_time.seconds / 3600.0
        )

    def get_profit(self):
        """Return profit: price_sell - production_price
        Returns
        -------
        TODO

        """
        return self.price_sell - self.get_production_price()

    def get_profit_per_time(self):
        """Divide total profit over production time.
        Returns
        -------
        float

        """
        return self.get_profit() / (
            self.production_time.total_seconds() / 3600.0
        )

    def summary(self):
        """Print summary on item.
        Returns
        -------
        TODO

        """
        print(f'name: {self.name}')
        print(f'production time (h): {self.get_production_time()}')
        print(f'price sell: {self.price_sell}')
        print(f'production price: {self.get_production_price()}')
        print('Components:')
        self.get_components()
