"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
Notice
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    '''
    非递归
    '''
    def closestValue(self, root, target):
        # write your code here
        if not root or target is None:
            return

        # 从根节点开始，也包括了只有一个节点的BST
        lower = root
        upper = root
        while root:
            # 根比目标大，设定上界，向左找下届或更小的上届
            if root.val > target:
                upper = root
                root = root.left
            # 根比目标小，设定下届，向右找上届或更大的下届
            elif root.val < target:
                lower = root
                root = root.right
            # 相等则返回
            else:
                return root.val

        # 根据上下界
        if abs(upper.val - target) >= abs(target - lower.val):
            return lower.val
        return upper.val

    '''
    递归：找上下边界
    '''

    def closestValue(self, root, target):
        # write your code here
        if not root or target is None:
            return

        # 上下界没有初始值，可能会出现None的情况
        upper = self.get_upper(root, target)
        lower = self.get_lower(root, target)
        if upper is None:
            return lower.val
        if lower is None:
            return upper.val
        if (upper.val - target) >= (target - lower.val):
            return lower.val
        return upper.val

    def get_lower(self, root, target):
        if not root:
            return None

        # 找下界，根大则向左走
        if root.val >= target:
            return self.get_lower(root.left, target)

        # 根小则向右走
        lower = self.get_lower(root.right, target)
        # 没有后路返回的None，则当前root为边界
        return root if lower is None else lower

    def get_upper(self, root, target):
        if not root:
            return None

        if root.val <= target:
            return self.get_upper(root.right, target)

        upper = self.get_upper(root.left, target)
        return root if upper is None else upper