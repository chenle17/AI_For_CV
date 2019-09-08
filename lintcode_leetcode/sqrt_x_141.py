class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    '''
    
    Implement int sqrt(int x).

Compute and return the square root of x.

Example
Example 1:
	Input:  0
	Output: 0


Example 2:
	Input:  3
	Output: 1
	
	Explanation:
	return the largest integer y that y*y <= x. 
	
Example 3:
	Input:  4
	Output: 2
	

Challenge
O(log(x))


    
    '''
    def sqrt(self, x):
        # write your code here
        if not x:
            return 0

        start, end = 0, x
        while int(start) != int(end):
            mid = start + (end - start) / 2
            if mid ** 2 > x:
                end = mid
            elif mid ** 2 < x:
                start = mid
            else:
                return int(mid)

        return int(start)