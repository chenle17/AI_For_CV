class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here

        if not numbers or target is None:
            return []

        hash_nums = {}
        index = 0
        # hash中value为index，key为index对应与target的差值，
        # 循环找当前值的差值是否在hash中存在
        while index < len(numbers):
            if numbers[index] in hash_nums:
                return [hash_nums[numbers[index]], index]

            hash_nums[target - numbers[index]] = index
            index += 1

        return []