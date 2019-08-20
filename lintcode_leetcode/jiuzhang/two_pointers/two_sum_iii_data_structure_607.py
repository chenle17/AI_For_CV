class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    '''
    Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
    '''

    _nums = {}

    # _sum = set()
    # _diff = set()

    def add(self, number):
        # write your code here
        # self._sum = self._sum | set([i + number for i in self._nums])
        # self._nums.add(number)
        self._nums[number] = self._nums.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        # 判断条件：
        # 求差值是否在nums里
        # 1. 在，两个相加数不相等
        # 2. 在，两个相加数相等且nums中个数大于1
        for i in self._nums:
            if value - i in self._nums and (value - i != i or self._nums[i] > 1):
                return True
        return False