import gym

from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os


environment_name = "BreakoutNoFrameskip-v4"
env = gym.make(environment_name, render_mode='human')
episodes = 1
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()

env.action_space.sample()
env.observation_space.sample()

env = make_atari_env('BreakoutNoFrameskip-v4', n_envs=16) # utiliza 4 ambiente de treino
env = VecFrameStack(env, n_stack=4)
log_path = os.path.join('logs')
agent = A2C("CnnPolicy", env, verbose=1, tensorboard_log=log_path)
agent.learn(total_timesteps= int(5e6))  # duração de treino


obs = env.reset()
#Salvar agente 
a2c_path = os.path.join('modelos', 'AgenteTreinado16')

agent.save(a2c_path)



while True:
    action, _ = agent.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()

# env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
# env = VecFrameStack(env, n_stack=4)
# model = A2C.load('D:\Projetos\AgentBreakout\modelos\AgenteTreinado.zip', env)


#evaluate_policy(model, env, n_eval_episodes=10, render=True)
# obs = env.reset()
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, info = env.step(action)
#     print(env.n_stack)
#     env.render()
    
# env.close()


