# -*- coding: utf-8 -*-
import sys
import networkx as nx
"""
Created on Sat Sep 25 20:22:59 2021

@author: Fernando Sanchez
Exercise 5.2
"""
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
            return 1

if __name__ == '__main__':
    #python solution5_1.py filename 1 2
    file_path = "C:/Users/ferna/Desktop/ca-GrQc.txt/CA-GrQc.txt"

    #filename = sys.argv[1]
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
    
    edges_ = G.number_of_edges();
    nodes_ = list(G.nodes())
    weak = 0
    strong = 0
    for i in range(len(nodes_)):
        for j in range(i+1, len(nodes_)):
            possible_edge = G.has_edge(nodes_[i], nodes_[j])
            if not possible_edge:
                continue
            else:
                first_edg = G.edges(nodes_[i])
                second_edg = G.edges(nodes_[j])
                strong += determine_connection(first_edg, second_edg)
    weak = edges_ - strong
    #Number of edges
    print("Number of edges:", edges_)
    print("Number of strong ties:", strong)
    print("Number of weak ties: ", weak)
    