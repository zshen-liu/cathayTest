import numpy as np


def calculate(invest_money: int, reward: list):
    """

    :param invest_money: invest per month
    :param reward: the records for year
    :return: total reward, avg_reward, reward std
    """
    #change reward to percent
    reward_percent = [i / 100 for i in reward]
    # record the reward per month
    reward_month = [i * invest_money for i in reward_percent]

    total_reward = round(sum(reward_month))

    reward_avg = round(sum(reward) / len(reward))

    std = round(np.std(reward, ddof=0))

    return total_reward, reward_avg, std


invest_money = 1000
reward = [-12, 5, 7, 25, 11, 3, -9, -5, -17, -22, -15, 0]

total_gain, avg_return, std_return = calculate(invest_money, reward)

print(f"總收益: {total_gain} 元")
print(f"投報率平均值: {avg_return}%")
print(f"投報率標準差: {std_return}%")
