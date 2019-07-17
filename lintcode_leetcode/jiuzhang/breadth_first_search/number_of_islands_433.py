from collections import deque

'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1
'''
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        h = len(grid)
        w = len(grid[0])
        # 记录已走过的岛（值为1的元素）
        visited = set()
        island_num = 0

        # 双层循环遍历起点坐标
        for i in range(h):
            for j in range(w):
                if grid[i][j] and (i, j) not in visited:
                    # 记录每一个岛坐标
                    visited.add((i, j))
                    # 走遍当前岛屿（1的点）
                    self.find_island(grid, i, j, visited, (h, w))
                    # 走完岛屿个数增加1
                    island_num += 1

        return island_num

    def find_island(self, grid, x, y, visited, h_w):
        # 使用双向队列保存当前位置
        # 注意加[]
        index_deque = deque([(x, y)])
        # “探索”岛屿
        # 注：for循环中不能改变被循环队列
        while index_deque:
            # 先进先出popleft
            x, y = index_deque.popleft()
            # 上下左右四个方向
            for move_x, move_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x = x + move_x
                new_y = y + move_y
                # 走出边界 或 已走过 或 是0 则 跳过本次循环
                if not self.is_valid(grid, new_x, new_y, visited, h_w):
                    continue
                # 在矩阵内，没有走过的1点
                # 加入队列等待“探索”
                index_deque.append((new_x, new_y))
                # 并标记已被探索
                visited.add((new_x, new_y))

    def is_valid(self, grid, x, y, visited, h_w):
        return 0 <= x < h_w[0] and 0 <= y < h_w[1] and (x, y) not in visited and grid[x][y]








