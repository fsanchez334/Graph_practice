# -*- coding: utf-8 -*
import sys
import networkx as nx
from collections import defaultdict
"""
Created on Mon Sep 27 01:18:51 2021

@author: ferna
Exercise 3: Version #2
"""
def largest_component(lister):
    longest = 0;
    for setters in lister:
        possible = len(setters)
        if possible > longest:
            longest = possible
    return longest

def determine_connection(first_edges, second_edges):
    if len(first_edges) == 0 or len(second_edges) == 0:
        return 0
    else:
        neighbors_1 = set([pairs[1] for pairs in first_edges])
        neighbors_2 = set([pairs[1] for pairs in second_edges])
        
        common_nodes = neighbors_1.intersection(neighbors_2)
        if len(common_nodes) == 0:
            return 0
        else:
            return common_nodes
if __name__ == '__main__':
    #python solution5_1.py filename 1 2
    file_path = "C:/Users/ferna/Desktop/ca-GrQc.txt/CA-GrQc.txt"

    filename = sys.argv[1] 
    G = nx.Graph()
    strong_graph = nx.Graph()
    counter = 0
    with open(filename) as f:
        for line in f:
            if counter < 4:
                counter += 1
                continue
            else:
                edge = line.split()
                if edge[0] == edge[1]:
                    continue
                else:
                    G.add_edge(edge[0], edge[1])
    f.close()
    
    edges_ = G.number_of_edges();
    nodes_ = list(G.nodes())
    strong_graph.add_nodes_from(nodes_)
    
    for i in range(len(nodes_)):
        for j in range(i+1, len(nodes_)):
            possible = G.has_edge(nodes_[i], nodes_[j])
            if not possible:
                continue
            else:
                first_ = G.edges(nodes_[i])
                second_ = G.edges(nodes_[j])
                edges_to_form  = determine_connection(first_, second_)
                if edges_to_form == 0:
                    continue
                else:
                    for noders in edges_to_form:
                        strong_graph.add_edge(nodes_[i], noders)
                        strong_graph.add_edge(nodes_[j], noders)
                
    
    number_connected_components = list(nx.connected_components(G))
    strong_connected_components = list(nx.connected_components(strong_graph))
    print("Number of connected component originally:", len(number_connected_components))
    print("Number of nodes in the largest connected components originally:", largest_component(number_connected_components))
    print("Number of connected components without weak ties:", len(strong_connected_components))
    print("Number of nodes in the largest connected component without weak ties:", largest_component(strong_connected_components))
    

