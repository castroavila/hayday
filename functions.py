#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file             : functions.py
# @created          : 18-Nov-2019
#

"""

"""

# Functions to deal and handle the list of items
import importlib
import item

importlib.reload(item)
from item import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# print('# of item in list_items {:2d}'.format(len(list_items)))


def list_places():
    places = []
    for item in list_items:
        places.append(item.production_place)

    unique_places = set(places)
    return unique_places


def list_products_at(place):
    items = []
    number = 1
    for item in list_items:
        if place == item.production_place:
            items.append(item)
    return items


def plot_time_vs_profit_at(place):
    time_and_profit_df = pd.DataFrame(
        columns=['production_time', 'profit', 'item_name', 'price_sell']
    )
    number = 1
    for item in list_items:
        if place == item.production_place:
            print(
                '{:d} ---> {:20s} {:20f} {:20f}'.format(
                    number,
                    item.name,
                    item.get_production_time(),
                    item.get_profit(),
                )
            )
            time_and_profit_df = time_and_profit_df.append(
                {
                    'production_time': item.get_production_time(),
                    'profit': item.get_profit(),
                    'item_name': item.name,
                    'price_sell': item.price_sell,
                    'profit_per_hour': item.get_profit()
                    / item.get_production_time(),
                    'prod_cost': item.get_production_price(),
                },
                ignore_index=True,
            )
            number += 1
    #    plt.plot(arr_time_and_profit[:, 0], arr_time_and_profit[:, 1], 'bo', markersize=5)
    # plt.scatter(arr_time_and_profit[:, 0], arr_time_and_profit[:, 1])
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 10))
    axis = ax.scatter(
        time_and_profit_df['prod_cost'],
        time_and_profit_df['profit'],
        c=time_and_profit_df['production_time'],
        cmap='viridis',
    )
    cmap = fig.colorbar(axis, ax=ax)
    cmap.set_label('production time (h)')

    # Label each point in scatter plot
    for index, row in time_and_profit_df.iterrows():
        ax.annotate(
            '{:s} \n {:.2f}'.format(row['item_name'], row['profit_per_hour']),
            xy=(row['prod_cost'], row['profit']),  # Label's position
            xytext=(0, 10),
            textcoords='offset points',  # Label offset from the plotted point
            ha='center',  # alignment
            va='bottom',
        )

    ax.set_title(place, color='blue')
    ax.set_xlabel('production cost')
    ax.set_ylabel('Profit')
    return fig
    # plt.show()


def generate_df():
    df_items = pd.DataFrame(
        columns=[
            'production_time',
            'profit',
            'item_name',
            'price_sell',
            'profit_per_hour',
            'prod_cost',
            'place',
        ]
    )
    
    dfs = []
    for item in list_items:
        dfs.append(pd.DataFrame(
            {
                'production_time': [item.get_production_time()],
                'profit': [item.get_profit()],
                'item_name': [item.name],
                'price_sell': [item.price_sell],
                'profit_per_hour': [item.get_profit() / item.get_production_time()],
                'prod_cost': [item.get_production_price()],
                'place': [item.production_place],
            }
        ))
    df_items = pd.concat(dfs, ignore_index=True)
    return df_items

def get_object(name):
    for item in list_items:
        if item.name == name:
            return item
