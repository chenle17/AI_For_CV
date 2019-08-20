class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    '''
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example
Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
Notice
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
    '''

    def moveZeroes(self, nums):
        # write your code here

        if not nums:
            return

        slow, fast = 0, 0
        while fast < len(nums):
            while fast < len(nums) and not nums[fast]:
                fast += 1

            if fast < len(nums):
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
