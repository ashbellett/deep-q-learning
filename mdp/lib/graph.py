import networkx as nx
import matplotlib.pyplot as plt
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
color_map = []
for node in graph:
    if isinstance(node, str):
        color_map.append('blue')
    else:
        color_map.append('red')

# Draw graph
pos = nx.kamada_kawai_layout(graph)
nx.draw(
    graph,
    pos,
    node_color=color_map,
    edge_color='black',
    width=1,
    linewidths=1,
    node_size=500,
    with_labels=True
)

nx.draw_networkx_edge_labels(
    graph,
    pos,
    edge_labels={
        ('a', ('a','x')):'2/3',
        ('a', ('a','y')):'1/3',
        ('b', ('b','x')):'2/3',
        ('b', ('b','y')):'1/3',
        ('c', ('c','x')):'2/3',
        ('c', ('c','y')):'1/3',
        (('a','x'), 'b'):'2/3',
        (('a','x'), 'c'):'1/3',
        (('a','y'), 'b'):'1/3',
        (('a','y'), 'c'):'2/3',
        (('b','x'), 'a'):'1/3',
        (('b','x'), 'c'):'2/3',
        (('b','y'), 'a'):'2/3',
        (('b','y'), 'c'):'1/3',
        (('c','x'), 'a'):'2/3',
        (('c','x'), 'b'):'1/3',
        (('c','y'), 'a'):'1/3',
        (('c','y'), 'b'):'2/3'
    },
     font_size=8
)
plt.show()

# # Node labels:
# {
#     'a': 'a',
#     'b': 'b',
#     'c': 'c',
#     ('a', 'x'): 'x',
#     ('a', 'y'): 'y',
#     ('b', 'x'): 'x',
#     ('b', 'y'): 'y',
#     ('c', 'x'): 'x',
#     ('c', 'y'): 'y'
# }