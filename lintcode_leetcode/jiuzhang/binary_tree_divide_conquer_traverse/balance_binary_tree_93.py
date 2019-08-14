"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Example  1:
	Input: tree = {1,2,3}
	Output: true
	
	Explanation:
	This is a balanced binary tree.
		  1  
		 / \                
		2  3

	
Example  2:
	Input: tree = {3,9,20,#,#,15,7}
	Output: true
	
	Explanation:
	This is a balanced binary tree.
		  3  
		 / \                
		9  20                
		  /  \                
		 15   7 

	
Example  3:
	Input: tree = {1,#,2,3,4}
	Output: false
	
	Explanation:
	This is not a balanced tree. 
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1  
		   \                
		   2                
		  /  \                
		 3   4
	
'''

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        # 空树也是平衡二叉树
        if root is None or root.val is None:
            return True

        balance, _ = self.is_balance(root)

        return balance

    def is_balance(self, root):
        # 终止条件：到达最底层返回高度0
        if root is None:
            return True, 0

        # 每一个子树都应该是平衡二叉树，否则返回False
        balance, left_depth = self.is_balance(root.left)
        if not balance:
            return False, 0
        balance, right_depth = self.is_balance(root.right)
        if not balance:
            return False, 0

        # max高度不断增加，左右高度差小于2
        return abs(left_depth - right_depth) < 2, max(left_depth, right_depth) + 1



