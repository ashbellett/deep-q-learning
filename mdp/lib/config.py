states = {'a', 'b', 'c'}            # state space
actions = {'x', 'y'}                # action space
rewards = {'a': 0, 'b': 1, 'c': -1} # reward function

policy = {}
transitions = {}
probabilities = {}

# Set action probabilities (policy)
# policy[state, action]
policy['a', 'x'] = 2/3
policy['a', 'y'] = 1/2
policy['b', 'x'] = 2/3
policy['b', 'y'] = 1/3
policy['c', 'x'] = 2/3
policy['c', 'y'] = 1/3

# Set state transition probabilities
# transitions[(state, next_state), action]
transitions[('a', 'a'), 'x'] = 0
transitions[('a', 'a'), 'y'] = 0
transitions[('b', 'b'), 'x'] = 0
transitions[('b', 'b'), 'y'] = 0
transitions[('c', 'c'), 'x'] = 0
transitions[('c', 'c'), 'y'] = 0
transitions[('a', 'b'), 'x'] = 2/3
transitions[('a', 'b'), 'y'] = 1/3
transitions[('a', 'c'), 'x'] = 1/3
transitions[('a', 'c'), 'y'] = 2/3
transitions[('b', 'a'), 'x'] = 1/3
transitions[('b', 'a'), 'y'] = 2/3
transitions[('b', 'c'), 'x'] = 2/3
transitions[('b', 'c'), 'y'] = 1/3
transitions[('c', 'a'), 'x'] = 2/3
transitions[('c', 'a'), 'y'] = 1/3
transitions[('c', 'b'), 'x'] = 1/3
transitions[('c', 'b'), 'y'] = 2/3

# probabilities[state, state-action]
# probabilities[state-action, state]
probabilities['a', ('a','x')] = '2/3'
probabilities['a', ('a','y')] = '1/3'
probabilities['b', ('b','x')] = '2/3'
probabilities['b', ('b','x')] = '2/3'
probabilities['b', ('b','y')] = '1/3'
probabilities['c', ('c','x')] = '2/3'
probabilities['c', ('c','y')] = '1/3'
probabilities[('a','x'), 'b'] = '2/3'
probabilities[('a','x'), 'c'] = '1/3'
probabilities[('a','y'), 'b'] = '1/3'
probabilities[('a','y'), 'c'] = '2/3'
probabilities[('b','x'), 'a'] = '1/3'
probabilities[('b','x'), 'c'] = '2/3'
probabilities[('b','y'), 'a'] = '2/3'
probabilities[('b','y'), 'c'] = '1/3'
probabilities[('c','x'), 'a'] = '2/3'
probabilities[('c','x'), 'b'] = '1/3'
probabilities[('c','y'), 'a'] = '1/3'
probabilities[('c','y'), 'b'] = '2/3'

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