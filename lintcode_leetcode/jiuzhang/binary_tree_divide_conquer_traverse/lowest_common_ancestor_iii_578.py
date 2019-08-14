"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

'''
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

Example
Example1

Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

Example2

Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
Notice
node A or node B may not exist in tree.
Each node has a different value


'''

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not root:
            return None

        a, b, father = self.LCA(root, A, B)
        return father

    def LCA(self, root, A, B):
        if root is None:
            return False, False, None

        l_a, l_b, l_father = self.LCA(root.left, A, B)
        if l_a and l_b:
            return l_a, l_b, l_father

        r_a, r_b, r_father = self.LCA(root.right, A, B)
        if r_a and r_b:
            return r_a, r_b, r_father

        a = l_a or r_a
        b = l_b or r_b

        if a and b:
            return True, True, root

        if root == A:
            a = True
        elif root == B:
            b = True
        if a and b:
            return True, True, root

        return a, b, None