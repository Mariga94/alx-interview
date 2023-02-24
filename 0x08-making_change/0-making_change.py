#!/usr/bin/python3
"""Coin Change Module"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to 
    return a total
    Arguments:
        coins (int): collection of selected coins
        total (int): total number of coins
    Returns: fewest number of coins require to meet total
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total +1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    if dp[total] != total + 1:
        return dp[total]
    return -1

