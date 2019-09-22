import numpy as np
import gym
from gym.wrappers import Monitor
from lib.agent import Agent
from lib.summary import summary
from lib.constants import *

def main():
    """ Orchestrates agent and environment interactions. """
    # Create environment
    environment = gym.make(ENVIRONMENT)
    if RECORD:
        environment = Monitor(
            env=environment,
            directory='./video/',
            video_callable=lambda episode_id: True,
            force=True
        )
    # Set random seeds
    environment.seed(0)
    np.random.seed(0)
    # Get action and state space sizes
    action_space = environment.action_space.n
    state_space = environment.observation_space.shape[0]
    # Instantiate agent
    agent = Agent(action_space, state_space)
    # Initialise list of all rewards
    rewards = []
    for episode in range(EPISODES):
        # Get initial state
        state = environment.reset()
        state = np.reshape(state, (1, state_space))
        # Reset score for this episode
        score = 0
        for _ in range(STEPS):
            if RENDER:
                environment.render()
            # Agent selects action from state
            action = agent.act(state)
            # Agent performs action and makes an observation of the environment
            next_state, reward, done, _ = agent.observe(environment, action)
            next_state = np.reshape(next_state, (1, state_space))
            observation = (state, action, reward, next_state, done)
            # Agent remembers parameters of this time step
            agent.remember(observation)
            state = next_state
            # Agent retrains model
            agent.learn()
            score += reward
            if done:
                print("Episode: {}/{}. Reward: {:.2f}".format(episode+1, EPISODES, score))
                break
        rewards.append(score)
        # Average reward over the last 100 episodes
        average_reward = np.mean(rewards[-100:])
        print("Average reward: {:.2f}\n".format(average_reward))
    # Terminate environment and plot rewards
    environment.close()
    summary(rewards)

if __name__ == "__main__":
    main()
