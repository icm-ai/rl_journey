import marimo

__generated_with = "0.11.30"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import gym  # 导入 Gym 的 Python 接口环境包

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
    return action, done, env, gym, info, observation, reward


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
