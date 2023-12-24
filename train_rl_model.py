from preprocess_environment import preprocess_env
from stable_baselines3 import PPO
from callbacks import TrainAndLoggingCallback

env = preprocess_env()
CHECKPOINT_DIR = './train/'
LOG_DIR = './logs/'

callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR, learning_rate=0.000001, n_steps=512)
model.learn(total_timesteps=1000000, callback=callback)
model.save('thisisatestmodel')
