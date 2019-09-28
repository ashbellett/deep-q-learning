FIGURE_DIRECTORY = './mdp/output/graph.png'
EPISODES = 1000
HORIZON = 100

STATES = ['a', 'b', 'c']            # state space
ACTIONS = ['x', 'y']                # action space
REWARDS = {'a': 0, 'b': 1, 'c': -1} # reward function
DISCOUNT_FACTOR = 1

POLICY = {}
TRANSITIONS = {}
LABELS = {}

# Set action probabilities (policy)
# POLICY[state, action]
POLICY['a', 'x'] = 2/3
POLICY['a', 'y'] = 1/3
POLICY['b', 'x'] = 2/3
POLICY['b', 'y'] = 1/3
POLICY['c', 'x'] = 2/3
POLICY['c', 'y'] = 1/3

# Set state transition probabilities
# TRANSITIONS[(state, next_state), action]
TRANSITIONS[('a', 'a'), 'x'] = 0
TRANSITIONS[('a', 'a'), 'y'] = 0
TRANSITIONS[('b', 'b'), 'x'] = 0
TRANSITIONS[('b', 'b'), 'y'] = 0
TRANSITIONS[('c', 'c'), 'x'] = 0
TRANSITIONS[('c', 'c'), 'y'] = 0
TRANSITIONS[('a', 'b'), 'x'] = 2/3
TRANSITIONS[('a', 'b'), 'y'] = 1/3
TRANSITIONS[('a', 'c'), 'x'] = 1/3
TRANSITIONS[('a', 'c'), 'y'] = 2/3
TRANSITIONS[('b', 'a'), 'x'] = 1/3
TRANSITIONS[('b', 'a'), 'y'] = 2/3
TRANSITIONS[('b', 'c'), 'x'] = 2/3
TRANSITIONS[('b', 'c'), 'y'] = 1/3
TRANSITIONS[('c', 'a'), 'x'] = 2/3
TRANSITIONS[('c', 'a'), 'y'] = 1/3
TRANSITIONS[('c', 'b'), 'x'] = 1/3
TRANSITIONS[('c', 'b'), 'y'] = 2/3

# LABELS[state, state-action]
# LABELS[state-action, state]
LABELS['a', ('a','x')] = '2/3'
LABELS['a', ('a','y')] = '1/3'
LABELS['b', ('b','x')] = '2/3'
LABELS['b', ('b','x')] = '2/3'
LABELS['b', ('b','y')] = '1/3'
LABELS['c', ('c','x')] = '2/3'
LABELS['c', ('c','y')] = '1/3'
LABELS[('a','x'), 'b'] = '2/3'
LABELS[('a','x'), 'c'] = '1/3'
LABELS[('a','y'), 'b'] = '1/3'
LABELS[('a','y'), 'c'] = '2/3'
LABELS[('b','x'), 'a'] = '1/3'
LABELS[('b','x'), 'c'] = '2/3'
LABELS[('b','y'), 'a'] = '2/3'
LABELS[('b','y'), 'c'] = '1/3'
LABELS[('c','x'), 'a'] = '2/3'
LABELS[('c','x'), 'b'] = '1/3'
LABELS[('c','y'), 'a'] = '1/3'
LABELS[('c','y'), 'b'] = '2/3'

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