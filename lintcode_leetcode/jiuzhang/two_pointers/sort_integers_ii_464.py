class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    '''
    Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.
    '''

    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return None

        # quick sort
        # self.quick_sort(A, 0, len(A) - 1)
        temp = [0 for _ in range(len(A))]
        print(temp)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid + 1, end, temp)
        self.merge(nums, start, end, temp)

    def merge(self, nums, start, end, temp):
        mid = (start + end) // 2
        left = start
        right = mid + 1
        index = left

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                index += 1
                left += 1
            else:
                temp[index] = nums[right]
                index += 1
                right += 1

        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            nums[i] = temp[i]