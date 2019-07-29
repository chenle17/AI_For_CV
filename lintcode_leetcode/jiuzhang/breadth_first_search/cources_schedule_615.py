from collections import deque

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: true
Example 2:

Input: n = 2, prerequisites = [[1,0],[0,1]]
Output: false

'''


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        # 判断为空则返回true
        if not prerequisites or not prerequisites[0]:
            return True

        # 入度
        indegree = [0 for _ in range(numCourses)]
        # key：前序课程， value：后续课程
        # 方便去除0入度课程时找到对应后续课程，并且后续课程入度-1
        edges = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            indegree[c1] += 1
            # 前序为key，指向后续
            edges[c2].append(c1)

        # 入度为0加入队列
        dq = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)

        # 记录上课节数
        counter = 0
        while dq:
            # pop一次记上课一次
            counter += 1
            c = dq.popleft()
            for j in edges[c]:
                indegree[j] -= 1
                # 判断是否出现满足上课要求的课程（入度为0）
                if indegree[j] == 0:
                    dq.append(j)

        return counter == numCourses