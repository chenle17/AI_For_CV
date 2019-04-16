'''
458. Last Position of Target
中文English
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here
        # if not nums or not target:
        #     return -1

        # l = len(nums)
        # for i in range(len(nums)):
        #     if nums[-i-1] == target:
        #         return l-i-1
        # return -1

        if not nums or not target:
            return -1

        l = len(nums)
        start = 0
        end = l - 1
        # 取mid，中间隔一个
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        # 防止第一个end就是target的情况
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1