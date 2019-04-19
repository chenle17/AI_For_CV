"""
428. Pow(x, n)
中文English
Implement pow(x, n). (n is an integer.)

Example
Example 1:

Input: x = 9.88023, n = 3
Output: 964.498
Example 2:

Input: x = 2.1, n = 3
Output: 9.261
Example 3:

Input: x = 1, n = 0
Output: 1
Challenge
O(logn) time

Notice
You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

"""


class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    # 循环法 时间复杂度：logn
    def myPow(self, x, n):
        # write your code here
        if not x or n == None:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        # 循环法
        # ans = 1
        # tmp = x
        #
        # while n != 0:
        #     if n % 2 == 1:
        #         ans *= tmp
        #     tmp *= tmp
        #     n = n // 2
        # return ans

        # 迭代法
        if n == 0:
            return 1

        if n % 2 == 0:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp
        else:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp * x