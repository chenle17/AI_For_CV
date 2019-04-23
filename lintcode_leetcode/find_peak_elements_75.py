'''
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example
Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6

	Explanation:
	return the index of peek.


Example 2:
	Input: [1,2,3,4,1]
	Output:  3

Challenge
Time complexity O(logN)

Notice
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
'''


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here

        if not A:
            return -1

        start, end = 0, len(A) - 1
        # 中间值与前一个值比较，单调增则移动start
        # 最后start 一定为极大值
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= A[mid - 1]:
                start = mid
            else:
                end = mid

        return start