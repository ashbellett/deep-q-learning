import numpy as np

class Episode:
    def __init__(self, actions, states, rewards, horizon, policy, transitions, initial_state):
        self.actions = actions
        self.states = states
        self.rewards = rewards
        self.horizon = horizon
        self.policy = policy
        self.transitions = transitions
        self.initial_state = initial_state
    
    def act(self, state):
        state_policy = []
        for action in self.actions:
            state_policy.append(self.policy[state, action])
        action = np.random.choice(a=self.actions, p=state_policy)
        next_states = list(set(self.states) - set(state))
        state_transitions = []
        for next_state in next_states:
            state_transitions.append(self.transitions[(state, next_state), action])
        return np.random.choice(a=next_states, p=state_transitions)

    def outcome(self, state):
        return self.rewards[state]
    
    def play(self):
        state = self.initial_state
        rewards = []
        for _ in range(self.horizon):
            next_state = self.act(state)
            rewards.append(self.outcome(next_state))
        return sum(rewards)
    