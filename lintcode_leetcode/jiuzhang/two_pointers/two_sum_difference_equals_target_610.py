"""\
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example
Example 1:

Input: nums = [2, 7, 15, 24], target = 5
Output: [1, 2]
Explanation:
(7 - 2 = 5)
Example 2:

Input: nums = [1, 1], target = 0
Output: [1, 2]
Explanation:
(1 - 1 = 0)
Notice
It's guaranteed there is only one available solution
"""


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    '''
    相似问题
G家的一个相似问题：找到一个数组中有多少对二元组，他们的平方差 < target（target 为正整数）。
我们可以用类似放的方法来解决，首先将数组的每个数进行平方，那么问题就变成了有多少对两数之差 < target。
然后走一遍上面的这个流程，当找到一对 nums[j] - nums[i] >= target 的时候，就相当于一口气发现了：

nums[i + 1] - nums[i]
nums[i + 2] - nums[i]
...
nums[j - 1] - nums[i]
一共 j - i - 1 对满足要求的二元组。累加这个计数，然后挪动 i 的位置 +1 即可。
    '''

    def twoSum7(self, nums, target):
        # write your code here

        if not nums or target is None:
            return
        if len(nums) < 2:
            return

        sum_dict = {}
        for i in range(len(nums)):
            if nums[i] in sum_dict:
                return [sum_dict[nums[i]] + 1, i + 1]
            # 数组无序，求差值时谁减谁前后有2种情况
            sum_dict[nums[i] + target] = i
            sum_dict[nums[i] - target] = i

        # dict中不存放两次相减结果，反过来再遍历一遍也可实现
        # sum_dict = {}
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] in sum_dict:
        #         return [i + 1, sum_dict[nums[i]] + 1]
        #     sum_dict[target + nums[i]] = i

        return