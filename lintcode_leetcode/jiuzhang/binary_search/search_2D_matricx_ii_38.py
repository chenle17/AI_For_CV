class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    '''
    Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

        This matrix has the following properties:
        
        Integers in each row are sorted from left to right.
        Integers in each column are sorted from up to bottom.
        No duplicate integers in each row or column.
        Example
        Example 1:
        
        Input:
            [[3,4]]
            target=3
        Output:1
        Example 2:
        
        Input:
            [
              [1, 3, 5, 7],
              [2, 4, 7, 8],
              [3, 5, 9, 10]
            ]
            target = 3
        Output:2
        Challenge
        O(m+n) time and O(1) extra space
    '''

    def searchMatrix(self, matrix, target):
        # write your code here\
        if not matrix:
            return ""

        row_max = len(matrix) - 1
        col_max = len(matrix[0]) - 1
        # 从右上角走，
        row = 0
        col = col_max

        out_num = 0
        while row <= row_max and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                out_num += 1
                col -= 1
                row += 1

        return out_num
