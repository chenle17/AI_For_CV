"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.
'''

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        if not root:
            return None

        self.tree_root = root
        self.min_sum = float('inf')# 无穷大，方便第一次记录
        self.tree_sum(root)

        return self.tree_root

    def tree_sum(self, root):
        # 递归终止条件，节点为None
        if root is None:
            return 0
        left_sum = self.tree_sum(root.left)
        right_sum = self.tree_sum(root.right)
        # 加上根节点的值
        sub_tree_sum = root.val + right_sum + left_sum

        if sub_tree_sum < self.min_sum:
            self.tree_root = root
            self.min_sum = sub_tree_sum

        return sub_tree_sum

