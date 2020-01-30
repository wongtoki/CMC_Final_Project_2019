from classes import *
import matplotlib.pyplot as plt
import networkx as nx


def createGraph(allusers, paths):

    # creating Graph
    G = nx.DiGraph()

    # adding nodes
    G.add_nodes_from(allusers)

    normal = []
    waypoints = []

    for user in allusers:
        for connection in user.connections:
            normal.append((user, connection))
            G.add_edge(user, connection)

    if len(paths) <= 2:
        waypoints.append((paths[0], paths[1]))
    else:
        for i in range(len(paths)):
            if i == len(paths)-1:
                break
            waypoints.append((paths[i], paths[i+1]))

    pos = nx.spring_layout(G, k=10, iterations=200)

    # nodes
    nx.draw_networkx_nodes(
        G, pos, node_size=[s.interactivity * 100 for s in allusers], node_color="#7ac3ff")

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=normal,
                           width=1, alpha=0.1, arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist=waypoints,
                           width=1, alpha=1, edge_color='b', arrowstyle='->', arrowsize=10)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')

    plt.axis('off')
    plt.show()
