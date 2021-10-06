# -*- coding: utf-8 -*-
import sys
import networkx as nx
from collections import defaultdict
"""
Created on Fri Sep 24 17:53:17 2021

@author: Fernando Sanchez
Date: September 24, 2021
"""
#Exercise 5.1
def determine_connection(first_edges, second_edges):
    if len(first_edges) == 0 or len(second_edges) == 0:
        print("False")
        return False
    else:
        neighbors_1 = set([pairs[1] for pairs in first_edges])
        neighbors_2 = set([pairs[1] for pairs in second_edges])
        
        common_nodes = neighbors_1.intersection(neighbors_2)
        if len(common_nodes) == 0:
            print("False")
            return False
        else:
            return True
    
if __name__ == '__main__':
    #python solution5_1.py filename 1 2
    file_path = "C:/Users/ferna/Desktop/ca-GrQc.txt/CA-GrQc.txt"
    
    filename = sys.argv[1]
    node1 = sys.argv[2] 
    node2 = sys.argv[3]
    
    G = nx.Graph()
    counter = 0
    with open(file_path) as f:
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
    
    #print(nodes_)
    #3466 and 10310
    #Algorithm: Get the edges of each of the nodes that are passed
    edges_for_first_node = G.edges(node1)
    edges_for_second_node = G.edges(node2)
    possible_edge = G.has_edge(node1, node2)
    if possible_edge == True:
        result = determine_connection(edges_for_first_node, edges_for_second_node)
        print(result)
    else:
        print("False")
        
