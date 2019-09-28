from lib.config import *
from lib.agent import Agent
from lib.episode import Episode
from lib.graph import Graph

# Print expected rewards and transition probabilities
agent = Agent(states, actions, rewards, HORIZON, discount_factor, policy, transitions)
expected_return_under_policy = agent.expected_return_under_policy()
expected_rewards = {}
for state in states:
    expected_rewards[state] = round(expected_return_under_policy[state, HORIZON-1])
print('Expected rewards:', expected_rewards)

actual_rewards = {}
for state in states:
    episode = Episode(actions, states, rewards, HORIZON, policy, transitions, state)
    actual_rewards[state] = 0
    for _ in range(EPISODES):
        actual_rewards[state] += episode.play()
    actual_rewards[state] /= EPISODES

print('Actual rewards:  ', actual_rewards)

# Draw state-action diagram
#graph = Graph(states, actions, probabilities)
#graph.draw()
