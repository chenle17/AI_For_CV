"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Example 1:

Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal
Example 2:

Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.

Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
'''

from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        # 判断None
        if root is None:
            return []

        # 创建双向队列
        dq = deque([root])
        result = []
        # 循环队列，一边pop一边append，直到队列为空
        # 每次while循环记录一层叶子节点
        while dq:
            # 暂存每一层叶子节点
            level = []

            '''
            for循环次数只在第一次时确定，循环中增加队列元素不影响循环次数
            每次for整体循环一层二叉树，循环结束当前层全部pop，
            此时队列中为下一层所有叶子节点，存下当前层叶子节点后，进行下一while循环
            '''
            for _ in range(len(dq)):
                head_dq = dq.popleft()
                level.append(head_dq.val)
                if head_dq.left:
                    dq.append(head_dq.left)
                if head_dq.right:
                    dq.append(head_dq.right)
            result.append(level)
        return result