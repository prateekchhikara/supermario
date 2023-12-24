# Mario RL Game
This repository contains a Reinforcement Learning (RL) project focused on training an AI agent to play the 'Super Mario Bros' game. The project uses the Proximal Policy Optimization (PPO) algorithm and is built on the gym_super_mario_bros environment from OpenAI.

## Features
- **Environment Setup**: Custom environment setup for the Super Mario Bros game.
- **Preprocessing**: Includes grayscale observation and frame stacking to optimize the learning process.
- **Training**: Training the RL model using the PPO algorithm with custom callbacks for model saving.
- **Testing**: Code to test and visualize the performance of the trained model.

## Prerequisites

Before running the project, ensure you have Python installed on your system. Python 3.7 or later is recommended.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/prateekchhikara/supermario
   cd supermario
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
3. **Training the Model**
    ```bash
    python train_rl_model.py
4. **Testing the Model**
    ```bash
    python test_model.py
## Project Structure

mario_env_setup.py: Setup of the Mario game environment.
preprocess_environment.py: Preprocessing steps for the environment.
train_rl_model.py: Script for training the RL model using PPO.
test_model.py: Script to test and demonstrate the trained model.
callbacks.py: Custom callback definitions for training.
requirements.txt: List of dependencies for the project.
README.md: This file, containing project information and instructions.