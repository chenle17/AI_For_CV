'''
Find K-th largest element in an array.

Example
Example 1:

Input:
n = 1, nums = [1,3,4,2]
Output:
4
Example 2:

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4
Challenge
O(n) time, O(1) extra memory.

Notice
You can swap elements in the array

'''


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here

        if not n or not nums:
            return None

        start, end = 0, len(nums) - 1
        return self.quick_sort(nums, start, end, n)

    def quick_sort(self, nums, start, end, k):
        # 终止条件
        if start == end:
            return nums[start]

        left, right = start, end
        # 扩苏排序中，随便找一个数作为比较对象
        pivot = nums[(left + start) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1

            #　交换
            if right >= left:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # k不变，每次与right、left比较（此时right一定小于left）
        # 选择一块（part）即可，另一块舍去
        # k不是0-based，所以-1
        if k - 1 <= right:
            return self.quick_sort(nums, start, right, k)
        if k - 1 >= left:
            return self.quick_sort(nums, left, end, k)
        return nums[k - 1]