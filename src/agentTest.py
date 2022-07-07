import gym

from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os

a2c_path = "D:\Projetos\AgentBreakout\modelos\AgenteTreinado3.zip"


               
env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
env = VecFrameStack(env, n_stack=4)

model = A2C.load(a2c_path, env)

evaluate_policy(model, env, n_eval_episodes=10, render=True)

episodes =50

for episode in range(1, episodes+1):
    obs = env.reset()
    #state = env.reset()
    done = False
    score = 5
    
    while not done:
        #env.render()
        action,_ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
    
env.close()