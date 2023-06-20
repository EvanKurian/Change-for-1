#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:47:35 2023

@author: evankurian
"""

def count_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

coins = [1, 5, 10, 25, 50]  # Different coin denominations (in cents)
amount = 100  # Amount in cents, equivalent to $1

ways = count_change(coins, amount)
print(f"The number of ways to make change for ${amount/100} is: {ways}")

