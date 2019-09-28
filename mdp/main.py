from lib.config import *
from lib.agent import Agent
from lib.graph import Graph

# Print expected rewards and transition probabilities
agent = Agent(states, actions, rewards, horizon, discount_factor, policy, transitions)
print('State transitions: ', agent.state_pairs())
print('Expected rewards ', agent.expected_rewards())
print('State transition probabilities under policy: ', agent.transitions_under_policy())
print('Expected rewards under policy: ', agent.expected_rewards_under_policy())
print('State-value function: ', agent.expected_return_under_policy())

# Draw state-action diagram
graph = Graph(states, actions, probabilities)
graph.draw()
