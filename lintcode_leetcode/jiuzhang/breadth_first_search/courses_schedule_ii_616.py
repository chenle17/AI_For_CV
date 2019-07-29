from collections import deque

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]

'''

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if prerequisites is None:
            return []

        indegree = [0 for _ in range(numCourses)]
        courses_order = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            courses_order[j].append(i)
            indegree[i] += 1

        dq = deque(maxlen=1)
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)

        whole_order = []
        while dq:
            course = dq.popleft()
            whole_order.append(course)
            for x in courses_order[course]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    dq.append(x)

        # 判断条件是上完所有课，可能会存在剩余课程没有入度为0的，
        # 无法继续上课
        if len(whole_order) == numCourses:
            return whole_order
        return []
