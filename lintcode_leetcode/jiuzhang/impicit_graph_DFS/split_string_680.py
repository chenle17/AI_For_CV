class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    '''
    分割字符串
中文English
给一个字符串,你可以选择在一个字符或两个相邻字符之后拆分字符串,使字符串由仅一个字符或两个字符组成,输出所有可能的结果

Example
样例1

输入： "123"
输出： [["1","2","3"],["12","3"],["1","23"]]
样例2

输入： "12345"
输出： [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
    '''

    def splitString(self, s):
        # write your code here
        if not s:
            return [[]]

        result = []

        self.sub_str(s, result, [])

        return result

    def sub_str(self, s, result, path):
        if not s:
            # path[:] to clone path
            result.append(path[:])
            return

        for i in range(1, 3):
            if len(s) >= i:
                path.append(s[:i])
                # 每次删除一到两个字符
                self.sub_str(s[i:], result, path)
                path.pop()