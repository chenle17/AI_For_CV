'''
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"
Notice
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

'''


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    '''
    分层BFS
    '''

    def ladderLength(self, start, end, dict):
        # 目标单词加入字典
        dict.add(end)
        distance = 0
        # 起始单词作为根节点，为第一层，也是第一步
        dq = collections.deque([start])
        # 存放已经走过的单词
        visited = set()

        while dq:
            distance += 1

            # 遍历当前相同距离的单词
            for _ in range(len(dq)):
                word = dq.popleft()
                if word == end:
                    return distance

                words = self.get_next_word(word)
                for next_word in words:
                    if next_word in dict and next_word not in visited:
                        dq.append(next_word)
                        # 加入已走列表
                        visited.add(next_word)
        return 0

    def get_next_word(self, word):
        next_words = []

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                if word[i] == char:
                    continue
                next_words.append(left + char + right)
        return next_words