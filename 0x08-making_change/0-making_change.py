#!/usr/bin/python3
"""
A module to determine the fewest number
of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    num_coins = 0
    if total == 0 or total < 0:
        return 0

    while total != 0:
        max_coin = max(coins)
        total = total - max_coin
        if total < max_coin:
            coins.remove(max_coin)
        num_coins += 1
        
        if not coins:
            return -1 
        elif total == 0:
            return num_coins
