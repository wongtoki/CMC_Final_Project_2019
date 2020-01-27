from classes import *
import matplotlib.pyplot as plt
import networkx as nx

def createGraph(allusers, allblogs):
    # creating Graph
    G = nx.Graph()

    # adding nodes
    G.add_nodes_from(allusers)

    # adding edges
    edgesBetweenUsers = Post.getConnections(allblogs)
    G.add_edges_from(edgesBetweenUsers)

    # draw graph
    nx.draw(G, with_labels=True)    
    plt.show()
