import gym

from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os

a2c_path = 'D:\Projetos\AgentBreakout\modelos.zip'

env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
env = VecFrameStack(env, n_stack=4)
agent = A2C.load(a2c_path, env)


evaluate_policy(agent, env, n_eval_episodes=10, render=True)
obs = env.reset()
score = 0
while True:
    action, _states = agent.predict(obs)
    obs, rewards, dones, info = env.step(action)
    episode = agent._episode_num
    score+= rewards
    env.render()
    print('Episode:{} Score:{}'.format(episode, score))
    
env.close()
