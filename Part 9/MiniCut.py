# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:55:14 2019

@author: 曾秋皓
"""

import random
import numpy as np

filepath = "D:\\File\\Algo\\Part 9\\kargerMinCut.txt"
result={}
with open(filepath,'r') as f:
    for line in f:
        temp = list(line.strip('\n').split(','))[0].split()
        temp = list(map(int,temp))
#        import ipdb
#        ipdb.set_trace()
        if len(temp) != 0:
            result[temp[0]] = temp[1:]
size = len(result)

for iteration in range(1):
    a = random.choice(list(result.keys()))
    A_nodes = [a]
    A_edges = result[a]
    del(result[a])
    b = random.choice(list(result.keys()))
    B_nodes = [b]
    B_edges = result[b]
    del(result[b])
    while len(result)!=0:
        coin = random.choice([0,1])
        if coin == 0:
            next_node = random.choice(A_edges)
            A_edges.remove(next_node)
            A_nodes.append(next_node)
            import ipdb;
            ipdb.set_trace()
            for edge in result[next_node]:
                if edge not in A_nodes:
                    A_edges.append(edge)
                    
        else:
            next_node = random.choice(B_edges)
            B_edges.remove(next_node)
            B_nodes.append(next_node)
            for edge in result[next_node]:
                if edge not in B_nodes:
                    B_edges.append(edge)

        del(result[next_node])
    cut = len(A_edges)
    cut_2 = len(B_edges)
