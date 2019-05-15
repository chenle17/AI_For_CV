'''
Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example
Example 1:

Input：[4, 5, 1, 2, 3]
Output：3
Explanation:
After sorting，[1,2,3,4,5]，the middle number is 3
Example 2:

Input：[7, 9, 4, 5]
Output：5
Explanation:
After sorting，[4,5,7,9]，the second(4/2) number is 5
Challenge
O(n) time.

Notice
The size of array is not exceed 10000

'''


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here

        if not nums:
            return None

        start, end = 0, len(nums) - 1
        k = (end + 2) // 2# 与找第k个数问题相同
        return self.quick_sort(nums, start, end, k)

    def quick_sort(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quick_sort(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quick_sort(nums, left, end, k - left + start)
        return nums[right + 1]