from classes import *
import matplotlib.pyplot as plt
import networkx as nx

def createGraph(userDict, blogsDict):
    G = nx.Graph()
    G.add_nodes_from(userDict.values())
    nx.draw(G, with_labels=True)    
    plt.show()