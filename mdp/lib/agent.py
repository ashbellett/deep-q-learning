from itertools import permutations

# TODO convert for loops into dictionary comprehensions

class Agent:
    def __init__(self, states, actions, rewards, horizon, discount_factor, policy, transitions):
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.horizon = horizon
        self.discount_factor = discount_factor
        self.policy = policy
        self.transitions = transitions

    def state_pairs(self):
        ''' Return state transition pairs '''
        return list(permutations(self.states, 2))

    def expected_rewards(self):
        ''' expected_rewards[state, action] '''
        expected_rewards = {}
        # Initialise expected rewards
        for action in self.actions:
            for state_pair in self.state_pairs():
                expected_rewards[state_pair[0], action] = 0
        # Calculate expected rewards
        for action in self.actions:
            for state_pair in self.state_pairs():
                expected_rewards[state_pair[0], action] += self.rewards[state_pair[1]]*self.transitions[state_pair, action]
        return expected_rewards

    def transitions_under_policy(self):
        ''' transitions_under_policy[state, next_state] '''
        transitions_under_policy = {}
        # Calculate state transitions probabilities while following policy
        for state_pair in self.state_pairs():
            transitions_under_policy[state_pair] = 0
            for action in self.actions:
                transitions_under_policy[state_pair] += self.policy[state_pair[0], action]*self.transitions[state_pair, action]
        return transitions_under_policy

    def expected_rewards_under_policy(self):
        ''' expected_rewards_under_policy[state] '''
        expected_rewards_under_policy = {}
        # Calculate expected rewards while following policy
        for state in self.states:
            expected_rewards_under_policy[state] = 0
            for action in self.actions:
                expected_rewards_under_policy[state] += self.policy[state, action]*self.expected_rewards()[state, action]
        return expected_rewards_under_policy

    def expected_return_under_policy(self):
        ''' state_value_function[state, step] '''
        expected_return_under_policy = {}
        for step in range(self.horizon):
            for state in self.states:
                expected_return_under_policy[state, step] = 0
        for step in range(self.horizon)[1:]:
            for state in self.states:
                for action in self.actions:
                    inner_sum = 0
                    for state_pair in [state_pair for state_pair in self.state_pairs() if state_pair[0] == state]:
                        inner_sum += self.transitions[state_pair, action]*expected_return_under_policy[state, step-1]
                    expected_return_under_policy[state, step] += inner_sum*self.policy[state, action]
                expected_return_under_policy[state,step] = self.expected_rewards_under_policy()[state] + self.discount_factor*expected_return_under_policy[state, step]
        return expected_return_under_policy
