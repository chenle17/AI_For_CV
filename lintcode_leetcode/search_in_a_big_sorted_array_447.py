'''
447. Search in a Big Sorted Array
中文English
Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
Challenge
O(logn) time, n is the first index of the given target number.

Notice
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.
'''

"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    # 二分法
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader or target == None:
            return -1

        start = 0
        end = 1
        # 确定二分法范围
        while reader.get(end) < target:
            end *= 2

        # 开始二分
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 任务是目标第一次出现的位置，当=时应当赋值给end，否则可能丢失第一次出现的位置
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end

        return -1

    # 倍增法
    def searchBigSortedArray_1(self, reader, target):
        # write your code here
        if not reader or target == None:
            return -1

        first_nums = reader.get(0)
        if first_nums == target:
            return 0

        if first_nums > target:
            return -1

        start, jump = 0, 1
        while jump:
            # jump之后小于则jump到当前位置，然后jump值翻倍，继续跳
            # jump之后大于等于则jump值折半，继续判断
            # 当jump值为0时，不再跳
            # 注：0翻倍还是0
            while jump and reader.get(start + jump) >= target:
                jump >>= 1
            start += jump
            jump <<= 1

        # 最终当前位置为小于target的最大数，判断下一个的数是否为target
        if reader.get(start + 1) == target:
            return start + 1
        return -1