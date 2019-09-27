import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx
from .config import *

# Initialise directed multi-graph
graph = nx.MultiDiGraph()

# Add state nodes
graph.add_nodes_from(states)

for state in states:
    for action in actions:
        # Add state-action nodes
        graph.add_node((state, action))
        # Add edges from states to state-actions
        graph.add_edge(state, (state, action))
        # Add edges from state-actions to next states
        for next_state in states - set(state):
            graph.add_edge((state, action), next_state)

# Colour states differently from state-actions
# color_map = []
# for node in graph:
#     if isinstance(node, str):
#         color_map.append('white')
#     else:
#         color_map.append('white')

# Draw graph
pos = nx.kamada_kawai_layout(graph)
nx.draw(
    graph,
    pos,
    node_color='white',
    edge_color='black',
    width=1,
    linewidths=1,
    node_size=500,
    with_labels=True
)
nx.draw_networkx_edge_labels(
    graph,
    pos,
    edge_labels=edge_labels,
    font_size=8
)
plt.show()
