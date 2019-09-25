from itertools import permutations

states = ['a', 'b', 'c'] # state space
actions = ['x', 'y'] # action space
rewards = {'a': 0, 'b': 1, 'c': -1} # reward function

state_pairs = list(permutations(states, 2)) # (state, next_state)
policy = {} # policy[state, action]
transition = {} # transition[(state, next_state), action]
transition_under_policy = {} # transition_under_policy[state, next_state]
expected_reward = {} # expected_reward[state, action]
expected_reward_under_policy = {} # expected_reward_under_policy[state]

# TODO convert for loops into dictionary comprehensions

# Every action is equally likely in each state
for state in states:
    for action in actions:
        policy[state, action] = 1/len(actions)

# Every state transition is equally likely
for state_pair in state_pairs:
    for action in actions:
        transition[(state_pair), action] = 1/(len(state_pairs)*len(actions))

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
