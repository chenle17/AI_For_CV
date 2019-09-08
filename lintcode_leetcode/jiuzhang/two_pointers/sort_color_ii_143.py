class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    '''
    Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Example1

Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
Example2

Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?

Notice
You are not suppose to use the library's sort function for this problem.
k <= n

    '''

    def sortColors2(self, colors=[3,2,3,3,4,3,3,2,4,4,1,2,1,1,1,3,4,3,4,2]
, k=4):
        # write your code here

        if not colors:
            return []

        self.sort(colors, 1, k, 0, len(colors) - 1)

    def sort(self, colors, color_start, color_end, start, end):
        if color_end == color_start or start >= end:
            return
        print(colors)

        color_mid = (color_end + color_start) // 2
        print(color_mid)

        left, right = start, end
        while left <= right:
            # 等于放到左边
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1

            if left <= right:
                print(left, right)
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.sort(colors, color_start, color_mid, start, right)
        self.sort(colors, color_mid + 1, color_end, left, end)
