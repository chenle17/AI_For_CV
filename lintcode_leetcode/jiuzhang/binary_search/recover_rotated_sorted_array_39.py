class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    '''
    39. Recover Rotated Sorted Array
    中文English
    Given a rotated sorted array, recover it to sorted array in-place.
    
    Example
    Example1:
    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
    Example2:
    [6,8,9,1,2] -> [1,2,6,8,9]
    
    Challenge
    In-place, O(1) extra space and O(n) time.
    
    Clarification
    What is rotated array?
    
    For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
    '''

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return

        l = len(nums) - 1
        for index in range(l):
            if nums[index] > nums[index + 1]:
                self.reverse_array(nums, 0, index)
                self.reverse_array(nums, index + 1, l)
                self.reverse_array(nums, 0, l)
                return

    def reverse_array(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1