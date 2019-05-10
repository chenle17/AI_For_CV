"""
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
Example
Example 1:

Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
Explanation:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
Example 2:

Input:
nums = [1,2,3]
Output:
[1,2,3]
3
Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
Notice
You don't need to keep the original order of the integers.
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here

        if not nums:
            return 0

        # Version 1: Do it in O(n) time complexity.
        tmp = set()# 花费额外空间，使时间复杂度更小
        index = 0
        for num in nums:
            if num not in tmp:
                nums[index] = num
                index += 1
                tmp.add(num)

        return index

        # version 2: Do it in O(nlogn) time without extra space.
        nums.sort()# 花费更多的时间，但不适用额外空间
        index = 0
        for num in nums:
            if num != nums[index]:
                index += 1
                nums[index] = num

        return index + 1