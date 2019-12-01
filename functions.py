#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : functions.py	
# @created          : 18-Nov-2019
# 

"""

"""

#Functions to deal and handle the list of items

from  item import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("# of item in list_items {:2d}".format(len(list_items)))

def list_places():
    places = []
    for item in list_items:
        places.append(item.production_place)

    unique_places = set(places)
    print(unique_places)

def list_products_at(place):
    print("Items produced at {:s}".format(place))
    print("{:20s} {:20s} {:20s}".format("name","production time","sell price"))
    number = 1
    for item in list_items:
        if(place == item.production_place):
            print("{:d} ---> {:20s} {:20d} {:20d}".format(number,item.name,item.price_sell,item.price_sell))
            number += 1

def plot_time_vs_profit_at(place):
    time_and_profit_df = pd.DataFrame(columns=["production_time","profit","item_name"])
    number = 1
    for item in list_items:
        if (place == item.production_place):
            print("{:d} ---> {:20s} {:20f} {:20f}".format(number,item.name,item.get_production_time(),item.get_profit()))
            time_and_profit_df = time_and_profit_df = time_and_profit_df.append({'production_time':item.get_production_time(),"profit":item.get_profit(),"item_name":item.name},ignore_index=True)
            number += 1
#    plt.plot(arr_time_and_profit[:,0],arr_time_and_profit[:,1],"bo",markersize=5)
    #plt.scatter(arr_time_and_profit[:,0],arr_time_and_profit[:,1])
    plt.scatter(time_and_profit_df["production_time"],time_and_profit_df["profit"])

    #Label each point in scatter plot
    for index, row in time_and_profit_df.iterrows():
        plt.annotate(row["item_name"],
                xy=(row['production_time'],row['profit']), # Label's position 
                xytext=(0,10), textcoords = "offset points", # Label offset from the plotted point
                ha="center", # alignment
                va="bottom")

    plt.title(place)
    plt.xlabel("Production time (h)")
    plt.ylabel("Profit")
    plt.show()





