'''
457. Classical Binary Search
中文English
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
Challenge
O(logn) time
'''
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 参数
        return self.binary_search(nums, start, end, target)

    def binary_search(self, nums, start, end, target):
        # 终止条件
        if start > end:
            return -1

        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # 拆解
            # return 保证返回值向上传递
            return self.binary_search(nums, start, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, end, target)
