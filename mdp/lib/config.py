states = {'a', 'b', 'c'}            # state space
actions = {'x', 'y'}                # action space
rewards = {'a': 0, 'b': 1, 'c': -1} # reward function
policy = {}
transition = {}
edge_labels = {}

# Set action probabilities (policy)
# policy[state, action]
policy['a', 'x'] = 2/3
policy['a', 'y'] = 1/2
policy['b', 'x'] = 2/3
policy['b', 'y'] = 1/3
policy['c', 'x'] = 2/3
policy['c', 'y'] = 1/3

# Set state transition probabilities
# transition[(state, next_state), action]
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

edge_labels['a', ('a','x')] = '2/3'
edge_labels['a', ('a','y')] = '1/3'
edge_labels['b', ('b','x')] = '2/3'
edge_labels['b', ('b','x')] = '2/3'
edge_labels['b', ('b','y')] = '1/3'
edge_labels['c', ('c','x')] = '2/3'
edge_labels['c', ('c','y')] = '1/3'
edge_labels[('a','x'), 'b'] = '2/3'
edge_labels[('a','x'), 'c'] = '1/3'
edge_labels[('a','y'), 'b'] = '1/3'
edge_labels[('a','y'), 'c'] = '2/3'
edge_labels[('b','x'), 'a'] = '1/3'
edge_labels[('b','x'), 'c'] = '2/3'
edge_labels[('b','y'), 'a'] = '2/3'
edge_labels[('b','y'), 'c'] = '1/3'
edge_labels[('c','x'), 'a'] = '2/3'
edge_labels[('c','x'), 'b'] = '1/3'
edge_labels[('c','y'), 'a'] = '1/3'
edge_labels[('c','y'), 'b'] = '2/3'

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