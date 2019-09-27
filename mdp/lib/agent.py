from itertools import permutations

# TODO convert for loops into dictionary comprehensions

class Agent:
    def __init__(self, states, actions, rewards, policy, transitions):
        self.states = states
        self.actions = actions
        self.rewards = rewards
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

    def expected_reward_under_policy(self):
        ''' expected_rewards_under_policy[state] '''
        expected_rewards_under_policy = {}
        # Calculate expected rewards while following policy
        for state in self.states:
            expected_rewards_under_policy[state] = 0
            for action in self.actions:
                expected_rewards_under_policy[state] += self.policy[state, action]*self.expected_rewards()[state, action]
        return expected_rewards_under_policy
