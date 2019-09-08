class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    '''
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
Example 1:

Input:[2,7,11,15]
Output:[]
Example 2:

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
Notice
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
    '''

    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []

        numbers.sort()

        # 转化为2 sum
        result = set()
        for i in range(len(numbers)):
            target = - numbers[i]

            sum_2 = set()
            for j in range(i + 1, len(numbers)):
                diff = target - numbers[j]
                if diff in sum_2:
                    result.add((numbers[i], diff, numbers[j]))
                sum_2.add(numbers[j])
        return list(result)