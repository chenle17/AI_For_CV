'''
Calculate the an % b where a, b and n are all 32bit positive integers.

Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

Challenge
O(logn)
'''


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here

        ans = 1
        """
        循环中的% b 为防止stackoverflow，保留或去掉不影响结果
        """
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b
            a = a * a % b
            n = n // 2

        return ans % b