class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        '''
        1，递归：函数接受什么样的参数，返回什么样的值，代表什么意思
        2， 递归的拆解
        3， 递归的出口
        '''
        if not n:
            return 0

        if n <= 2:
            return n - 1

        # return self.fibonacci(n - 1) + self.fibonacci(n - 2)

        a = 0
        f_sum = 1
        for i in range(n - 2):
            a, f_sum = f_sum, f_sum + a
        return f_sum