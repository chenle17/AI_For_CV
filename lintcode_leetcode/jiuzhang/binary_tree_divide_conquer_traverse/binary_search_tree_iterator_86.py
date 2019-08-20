"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
'''
Binary Search Tree Iterator
中文English
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Example
Example 1

Input:  {10,1,11,#,6,#,12}
Output:  [1, 6, 10, 11, 12]
Explanation:
The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
Example 2

Input: {2,1,3}
Output: [1,2,3]
Explanation:
The BST is look like this:
  2
 / \
1   3
You can return the inorder traversal of a BST tree [1,2,3]
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
'''

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary
        self._stack = []
        while root:
            self._stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        # write your code here
        return len(self._stack) > 0

    """
    @return: return next node
    """

    def next(self, ):
        # write your code here
        next_node = self._stack.pop()

        if next_node.right:
            node = next_node.right
            while node:
                self._stack.append(node)
                node = node.left

        return next_node
