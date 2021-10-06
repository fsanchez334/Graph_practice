# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:26:14 2021

@author: Fernando Sanchez
UNI: fs2664
"""
import sys
import networkx as nx
#Exercise 4.1
#Take file -> turn into network -> get min and max degree
G = nx.Graph();
#Open the file -> file is in the working directory
file_path = "C:/Users/ferna/Desktop/ca-GrQc.txt/CA-GrQc.txt"
filename = sys.argv[1]
counter = 0;
with open(filename) as f:
    for line in f:
        if counter < 4:
            counter += 1
            continue
        else:
            edge = line.split()
            G.add_edge(edge[0], edge[1])
f.close()
'''
looker = list(G.edges())
print(len(looker))
looker_ = list(G.nodes())
print(len(looker_))
The above is just a sanity check to make sure that I got the right amount of nodes and edges
'''
list_of_nodes = list(G.degree());
high_degree = 0;
low_degree = 100000
for nodes in list_of_nodes:
    if nodes[1] > high_degree:
        high_degree = nodes[1]
        
    if nodes[1] < low_degree:
        low_degree = nodes[1]

print("Highest Degree: ", high_degree)
print("Lowest Degree: " , low_degree)

        