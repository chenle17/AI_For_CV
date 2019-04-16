'''
460. Find K Closest Elements
中文English
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time

Notice
The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^410
​4
​​
Absolute value of elements in the array will not exceed 10^410
​4
​​
'''


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here

        if not A or k < 0 or not str(target).isdigit():
            return []

        l = len(A)
        if k > l:
            return []

        start = 0
        end = l - 1
        # 二分法找到两个点，start点小于target，end点大于等于target
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        out_array = []
        # 双指针向两边展开
        while k > 0:
            # 一个指针超出index范围后直接添加另一指针所指元素
            if end == l:
                out_array.append(A[start])
                start -= 1
                k -= 1
                continue
            elif start == -1:
                out_array.append(A[end])
                end += 1
                k -= 1
                continue

            # 取两指针对应元素与target更近的那个
            start_sub = target - A[start]
            end_sub = A[end] - target
            if start_sub > end_sub:
                out_array.append(A[end])
                end += 1
            else:
                out_array.append(A[start])
                start -= 1

            k -= 1

        return out_array