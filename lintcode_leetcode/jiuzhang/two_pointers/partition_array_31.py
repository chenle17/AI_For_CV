class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    '''
    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
Challenge
Can you partition the array in-place and in O(n)?

Notice
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length


    
    '''
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while end >= start and nums[end] >= k:# 求第一个k的位置，start无等于号，不移动，end有等于号，移动
                end -= 1

            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return start