import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from itertools import permutations
import networkx as nx
import matplotlib.pyplot as plt

states = {'a', 'b', 'c'}            # state space
actions = {'x', 'y'}                # action space
rewards = {'a': 0, 'b': 1, 'c': -1} # reward function
state_pairs = list(permutations(states, 2)) # (state, next_state)

# Initialise multi, directed graph
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

policy = {} # policy[state, action]
transition = {} # transition[(state, next_state), action]
transition_under_policy = {} # transition_under_policy[state, next_state]
expected_reward = {} # expected_reward[state, action]
expected_reward_under_policy = {} # expected_reward_under_policy[state]

# TODO convert for loops into dictionary comprehensions

# Set action probabilities (policy)
policy['a', 'x'] = 2/3
policy['a', 'y'] = 1/2
policy['b', 'x'] = 2/3
policy['b', 'y'] = 1/3
policy['c', 'x'] = 2/3
policy['c', 'y'] = 1/3

# Set state transition probabilities
transition[('a', 'a'), 'x'] = 0
transition[('a', 'a'), 'y'] = 0
transition[('b', 'b'), 'x'] = 0
transition[('b', 'b'), 'y'] = 0
transition[('c', 'c'), 'x'] = 0
transition[('c', 'c'), 'y'] = 0
transition[('a', 'b'), 'x'] = 2/3
transition[('a', 'b'), 'y'] = 1/3
transition[('a', 'c'), 'x'] = 1/3
transition[('a', 'c'), 'y'] = 2/3
transition[('b', 'a'), 'x'] = 1/3
transition[('b', 'a'), 'y'] = 2/3
transition[('b', 'c'), 'x'] = 2/3
transition[('b', 'c'), 'y'] = 1/3
transition[('c', 'a'), 'x'] = 2/3
transition[('c', 'a'), 'y'] = 1/3
transition[('c', 'b'), 'x'] = 1/3
transition[('c', 'b'), 'y'] = 2/3

# Calculate state transition probabilities while following policy
for state_pair in state_pairs:
    transition_under_policy[state_pair] = 0
    for action in actions:
        transition_under_policy[state_pair] += policy[state_pair[0], action]*transition[state_pair, action]

# Initialise expected rewards
for action in actions:
    for state_pair in state_pairs:
        expected_reward[state_pair[0], action] = 0

# Calculate expected rewards
for action in actions:
    for state_pair in state_pairs:
        expected_reward[state_pair[0], action] += rewards[state_pair[1]]*transition[state_pair, action]

# Calculate expected rewards while following policy
for state in states:
    expected_reward_under_policy[state] = 0
    for action in actions:
        expected_reward_under_policy[state] += policy[state, action]*expected_reward[state, action]

print('Expected reward while following policy:')
print(expected_reward_under_policy)
