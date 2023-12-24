from preprocess_environment import preprocess_env
from stable_baselines3 import PPO

model = PPO.load('./train/best_model_1000000')
env = preprocess_env()
state = env.reset()

while True:
    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()
