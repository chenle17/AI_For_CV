class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    '''
    全排列
中文English
给定一个数字列表，返回其所有可能的排列。

Example
样例 1：

输入：[1]
输出：
[
  [1]
]
样例 2：

输入：[1,2,3]
输出：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
使用递归和非递归分别解决。

Notice
你可以假设没有重复数字。


    '''

    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]

        result = []
        self.find_permulations(nums, result, [])

        return result

    def find_permulations(self, nums, result, sub_p):
        if not nums:
            result.append(sub_p[:])
            return

        for i in range(len(nums)):
            sub_p.append(nums[i])
            self.find_permulations(nums[:i] + nums[i + 1:], result, sub_p)
            sub_p.pop()

    # 非递归
    def _permute(self, nums):
        # write your code here

        if not nums:
            return [[]]

        stack = [[i] for i in nums]
        result = []

        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue
            for n in nums:
                if n not in last:
                    # last += [n]
                    stack.append(last + [n])

        return result