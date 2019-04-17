'''46. Majority Element
中文English
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

Example
Example 1:

Input: [1, 1, 1, 1, 2, 2, 2]
Output: 1
Example 2:

Input: [1, 1, 1, 2, 2, 2, 2]
Output: 2
Challenge
O(n) time and O(1) extra space'''
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return ""

        storted_num = None
        counter = 1
        for num in nums:
            if num == storted_num:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    storted_num = num
                    counter = 1
        return storted_num