# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:41:52 2021

@author: Fernando Sanchez
UNI: fs2664
"""
import sys
import networkx as nx
from collections import defaultdict
#Exercise 4.2
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

edges_ = list(G.edges())
nodes_ = list(G.nodes())

total_nodes = len(nodes_)
tracker = defaultdict(lambda: [])
nodes_view = G.degree();
for nodes in nodes_view:
    tracker[nodes[1]].append(nodes[0]);

percentage_1 = len(tracker[1]) / total_nodes
print("Percentage of authors with only 1 coauthor: ", percentage_1)
metrics = [10, 20, 40, 80]
collections_sum = [];
for milestones in metrics:
    track_sum = 0
    for i in range(milestones):
        track_sum += len(tracker[i])
    collections_sum.append(track_sum / total_nodes);
    
print("Percentage of authors with 10 or fewer coauthors: ", collections_sum[0])
print("Percentage of authors with 20 or fewer coauthors: ", collections_sum[1])
print("Percentage of authors with 40 or fewer coauthors: ", collections_sum[2])
print("Percentage of authors with 80 or fewer coauthors: ", collections_sum[3])

    


