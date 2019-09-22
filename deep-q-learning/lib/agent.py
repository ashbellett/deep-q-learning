import random
import numpy as np
from collections import deque
from .model import Model
from .constants import *

class Agent():
    """ Observes environment, selects actions and trains model. """
    def __init__(self, action_space, state_space):
        self.action_space = action_space
        self.batch_size = BATCH_SIZE
        self.epsilon = 1.0
        self.epsilon_min = EPSILON_MIN
        self.epsilon_decay = EPSILON_DECAY
        self.gamma = GAMMA
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.model = Model(
            action_space,
            state_space,
            HIDDEN_NODES,
            HIDDEN_LAYERS,
            LEARNING_RATE
        ).build()

    def act(self, state):
        """ Selects an action from the action space. """
        # Occasionally explore the state space via a random action
        if np.random.rand() <= self.epsilon:
            actions = range(self.action_space-1)
            action = np.random.choice(actions)
        # Normally choose predicted optimal action
        else:
            policy = self.model.predict(state)
            action = np.argmax(policy[0])
        return action

    def observe(self, environment, action):
        """ Gets new state and reward from environment. """
        return environment.step(action)

    def remember(self, observation):
        """ Stores observation in memory. """
        self.memory.append(observation)

    def learn(self):
        """ Retrains model using new observations. """
        if len(self.memory) > self.batch_size:
            # Get a batch of observations
            batch = random.sample(self.memory, self.batch_size)
            # Retrieve signals from batch
            states = np.array([i[0] for i in batch])
            actions = np.array([i[1] for i in batch])
            rewards = np.array([i[2] for i in batch])
            next_states = np.array([i[3] for i in batch])
            dones = np.array([i[4] for i in batch])
            # Remove single-dimensional entries from array shape
            states = np.squeeze(states)
            next_states = np.squeeze(next_states)
            # Predict action-state value function (Q-function) for current state
            action_state_value = self.model.predict_on_batch(states)
            # Predict optimal action-state value function for next state (Bellman equation)
            next_action_state_value = rewards + self.gamma*np.amax(self.model.predict_on_batch(next_states), axis=1)*(1-dones)
            # Create index from batch size
            indices = np.array([i for i in range(self.batch_size)])
            # Map actions to optimal action-state value function
            action_state_value[[indices], [actions]] = next_action_state_value
            # Train model with states and predicted action-state value function
            self.model.fit(states, action_state_value, epochs=1, verbose=0)
            # Decrease likelihood of exploratory action
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay
