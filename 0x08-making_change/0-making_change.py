#!/usr/bin/python3
"""
module that handles changes
"""


def makeChange(coins, total):
    """
    makechange function
    :param coins: list of coins
    :param total: amount to make change for
    :return: fewest number of coins needed to meet total
    if total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination
    of coin in the list
    Your solution's runtime will be evaluated in this task
    """
    if total <= 0:
        return 0
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
