import gym

from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os


environment_name = "Breakout-v0"
env = gym.make(environment_name, render_mode='human')
episodes = 5
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

env = make_atari_env('Breakout-v0', n_envs=4, seed=0) # utiliza 4 ambiente de treino
env = VecFrameStack(env, n_stack=4)
log_path = os.path.join('logs')
agent = A2C("CnnPolicy", env, verbose=1, tensorboard_log=log_path)
agent.learn(total_timesteps= 4000000)  # duração de treino

#Salvar agente 
a2c_path = os.path.join('modelos', 'AgenteTreinado')
agent.save(a2c_path)
del agent

# env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
# env = VecFrameStack(env, n_stack=4)
# model = A2C.load(a2c_path, env)


# evaluate_policy(model, env, n_eval_episodes=10, render=True)
# obs = env.reset()
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, info = env.step(action)
#     env.render()
    
# env.close()