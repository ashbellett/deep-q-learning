import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam

class Model():
    """ Returns a fully-connected feed-forward neural network. """
    def __init__(self, action_space, state_space, hidden_nodes, layers, learning_rate):
        self.action_space = action_space
        self.state_space = state_space
        self.nodes = hidden_nodes
        self.layers = layers
        self.learning_rate = learning_rate

    def build(self):
        """ Builds the neural network model. """
        model = Sequential()
        # Input layer
        model.add(Dense(self.nodes, input_dim=self.state_space, activation=relu))
        # Hidden layers
        for _ in range(self.layers):
            model.add(Dense(self.nodes, activation=relu))
        # Output layer
        model.add(Dense(self.action_space, activation=linear))
        model.compile(
            optimizer=Adam(lr=self.learning_rate),
            loss='mse',
            metrics=['accuracy']
        )
        return model