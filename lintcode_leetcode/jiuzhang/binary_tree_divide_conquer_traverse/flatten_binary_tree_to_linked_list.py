"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
'''
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
         1
Challenge
Do it in-place without any extra memory.

Notice
Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.


'''

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    last_node = None

    def flatten(self, root):
        # write your code here
        if root is None:
            return None

        # 当前节点移到最后节点的右边，左边置None
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root

        # 当前节点为最后节点，取下右节点
        # 先序排列先根节点 再左节点 后右节点
        # 按照先序顺序把节点更新到最后节点
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
