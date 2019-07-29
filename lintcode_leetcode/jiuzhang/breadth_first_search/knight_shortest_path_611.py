"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

'''
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Notice
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
'''
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    '''
    DFS版本，矩阵大时会超时
    '''

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1

        self._h = len(grid)
        self._w = len(grid[0])
        self._min_counter = 0
        counter = 0
        visited = set((source.x, source.y))
        self.find_path(grid, source, destination, counter, visited)

        if self._min_counter:
            return self._min_counter
        return -1

    def find_path(self, grid, source, destination, counter, visited):
        if source.x == destination.x and source.y == destination.y:
            if self._min_counter == 0 or self._min_counter > counter > 0:
                self._min_counter = counter
                return

        move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        # 一条路走到黑，再不断溯回，时间复杂度太高
        for move_x, move_y in move:
            new_x = source.x + move_x
            new_y = source.y + move_y
            if 0 <= new_x < self._h and 0 <= new_y < self._w and not grid[new_x][new_y] and (
            new_x, new_y) not in visited:
                counter += 1
                source.x = new_x
                source.y = new_y
                visited.add((new_x, new_y))

                self.find_path(grid, source, destination, counter, visited)

                counter -= 1
                source.x -= move_x
                source.y -= move_y
                visited.remove((new_x, new_y))

'''
BFS版本，使用distance hash记录距离
'''

from collections import deque

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1

        h = len(grid)
        w = len(grid[0])

        # distance hash 记录距离
        min_counter = {(source.x, source.y): 0}
        dq = deque([(source.x, source.y)])

        while dq:
            x, y = dq.popleft()
            if (x, y) == (destination.x, destination.y):
                return min_counter[(x, y)]
            # 当前位置可以走的所有点加入队列
            # 排除走过的点和非0点
            # 利用队列先进后出的特点保证第一个到终点的店距离其最近
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) in min_counter:
                    continue

                # 可走点加入队列，并记录其步数
                if 0 <= new_x < h and 0 <= new_y < w and not grid[new_x][new_y]:
                    dq.append((new_x, new_y))
                    min_counter[(new_x, new_y)] = min_counter[(x, y)] + 1

        return -1