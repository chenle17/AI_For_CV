'''
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example
Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20

'''
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here

        if not nums or len(nums) < k:
            return []

        k_sum = 0
        sum_list = []
        for i in range(len(nums)):
            k_sum += nums[i]
            if i == k - 1:
                sum_list.append(k_sum)
            if i > k - 1:
                k_sum -= nums[i - k]
                sum_list.append(k_sum)

        return sum_list