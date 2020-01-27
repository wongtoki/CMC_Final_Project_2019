from classes import *
import matplotlib.pyplot as plt
import networkx as nx

def createGraph(allusers, allblogs):
    G = nx.Graph()
    G.add_nodes_from(allusers)
    for blog in allblogs:
        for replier in blog.getRepliers():
            G.add_edge(blog.getCreator(), replier)
    nx.draw(G, with_labels=True)    
    plt.show()