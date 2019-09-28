from lib.config import *
from lib.agent import Agent
from lib.episode import Episode
from lib.graph import Graph

# Predict expected return for each time step
agent = Agent(STATES, ACTIONS, REWARDS, HORIZON, DISCOUNT_FACTOR, POLICY, TRANSITIONS)
expected_return_under_policy = agent.expected_return_under_policy()

# Get expected rewards at end of episode
expected_rewards = {}
for state in STATES:
    expected_rewards[state] = round(expected_return_under_policy[state, HORIZON-1])

# Simulate an episode to get actual rewards
actual_rewards = {}
for state in STATES:
    episode = Episode(ACTIONS, STATES, REWARDS, HORIZON, POLICY, TRANSITIONS, state)
    actual_rewards[state] = 0
    for _ in range(EPISODES):
        actual_rewards[state] += episode.play()
    actual_rewards[state] /= EPISODES

# Compare predicted vs. actual rewards
print('Expected rewards:', expected_rewards)
print('Actual rewards:  ', actual_rewards)

# Draw state-action diagram
graph = Graph(STATES, ACTIONS, LABELS)
graph.draw()
