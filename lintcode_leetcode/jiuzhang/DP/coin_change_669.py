'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example
Example1

Input:
[1, 2, 5]
11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example2

Input:
[2]
3
Output: -1
Notice
You may assume that you have an infinite number of each kind of coin.

'''

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        # write your code here
        if not coins or not amount:
            return 0

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    dp[i] = min(dp[i], dp[diff] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        return -1