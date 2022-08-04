#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <castroavila_2004@hotmail.com>
# @file             : build_graph.py
# @created          : 28-Jul-2022
# @company          : Home
#

"""
Build Graph with connections across items.

"""
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import importlib
import functions
importlib.reload(functions)
from functions import *


dg = nx.DiGraph()
for item in  list_items:
    for single_component in item.components.keys():
        dg.add_edge(single_component.name, item.name, n_components=item.components[single_component])

def get_ancestor_nodes_and_position(final_node):
    '''
    Build sub-graph with ancestors of `final_node`.
    Parameters:
        final_node: str, item's name.
    '''
    sub_graph = nx.DiGraph()
    ancestors = nx.ancestors(dg, final_node)
    ancestors.add(final_node)
    for node in ancestors:
        for edge in dg.in_edges(node):
            sub_graph.add_edge(edge[0], edge[1])

    # Position layout
    position = graphviz_layout(sub_graph, prog='dot')

    return sub_graph, position

def get_descendant_nodes_and_position(initial_node):
    '''
    Build sub-graph with descendants of `initial_node`.
    Parameters:
        initial_node: str, item's name.
    '''
    sub_graph = nx.DiGraph()
    descendants = nx.descendants(dg, initial_node)
    descendants.add(initial_node)
    for node in descendants:
        for edge in  dg.out_edges(node):
            sub_graph.add_edge(edge[0], edge[1])

    # Position layout
    position = graphviz_layout(sub_graph, prog='dot')

    return sub_graph, position
