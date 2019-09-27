import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, states, actions, probabilities):
        self.graph = nx.MultiDiGraph()
        self.states = states
        self.actions = actions
        self.probabilities = probabilities
        self.build()

    def build(self):
        ''' Add nodes and edges to graph '''
        self.graph.add_nodes_from(self.states)
        for state in self.states:
            for action in self.actions:
                # Add state-action nodes
                self.graph.add_node((state, action))
                # Add edges from states to state-actions
                self.graph.add_edge(state, (state, action))
                # Add edges from state-actions to next states
                for next_state in self.states - set(state):
                    self.graph.add_edge((state, action), next_state)
    
    def draw(self):
        ''' Draw graph '''
        pos = nx.kamada_kawai_layout(self.graph)
        nx.draw(
            self.graph,
            pos,
            node_color='white',
            edge_color='black',
            width=1,
            linewidths=1,
            node_size=500,
            with_labels=True
        )
        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=self.probabilities,
            font_size=8
        )
        plt.show()
