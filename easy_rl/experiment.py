"""
Author: MingChen
Date: 2025-03-11 14:04:42
LastEditors: MingChen
LastEditTime: 2025-03-28 15:31:26
"""

import gym  # 导入 Gym 的 Python 接口环境包
import marimo  # 导入 Marimo 的 Python 接口环境包

env = gym.make("CartPole-v0", render_mode="rgb_array")  # 构建实验环境
env.reset()  # 重置一个回合
for _ in range(10):
    env.render()
    action = env.action_space.sample()  # 从动作空间中随机选取一个动作
    observation, reward, done, info = env.step(
        action
    )  # 用于提交动作，括号内是具体的动作
    print(observation)  # 输出当前观测值
env.close()  # 关闭环境


