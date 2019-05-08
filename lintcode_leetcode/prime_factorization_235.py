'''

235. Prime Factorization
中文English
Prime factorize a given integer.

Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
Notice
You should sort the factors in ascending order.
'''
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here

        if num < 2:
            return None

        import math
        # 质因数上界设置为根号（num），减少循环次数
        max_k = math.sqrt(num)

        k = 2
        results = []
        # num为1时，提前终止循环
        while k <= max_k and num != 1:
            if num % k == 0:
                results.append(k)
                num //= k
            else:
                # 除不尽时k++
                k += 1

        # 大于k的上界质因数只可能有一个
        if num != 1:
            results.append(num)
        return results
    """
    复杂度分析
    最坏时间复杂度 
        O(\sqrt{n})。当n为质数时，取到其最坏时间复杂度。
    空间复杂度 
        O(log(n))，当n质因数很多时，需要空间大，
        但总不会多于O(log(n))O(log(n))个。
    """
