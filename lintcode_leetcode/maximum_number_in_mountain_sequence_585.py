'''
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7],
Output: 10

'''

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here


        if not nums:
            return -1

        l = len(nums)
        start = 0
        end = l - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1]:
                start = mid
            else:
                end = mid

        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]