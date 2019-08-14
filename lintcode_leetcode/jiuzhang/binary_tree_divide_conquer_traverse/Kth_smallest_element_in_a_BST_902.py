"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Notice
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        if not root or k < 1:
            return None

        self.nums = []
        self.get_nums(root)
        # print(self.nums)

        return self.nums[k - 1]

    def get_nums(self, root):
        if root is None:
            return None

        self.get_nums(root.left)
        self.nums.append(root.val)
        self.get_nums(root.right)

    # Binary Tree Iterator连续找K个点
    def kthSmallest_1(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            # 除第一次，每次pop最小的一个，所以出循环后stack中最后一个是第k小
            node = stack.pop()
            # pop出根节点
            if node.right:
                node = node.right
                # 循环栈中节点
                while node:
                    # 当前节点加入栈
                    stack.append(node)
                    # 走向左节点
                    # 不为None就继续走，每走一步把节点加入栈
                    # 会走到最小值，然后遵循栈的后入先出原则
                    # 下一次for循环先把栈中最小的节点（最后压栈的节点）pop出
                    # 看他是否有右节点，有的话压栈循环操作
                    # 除第一次为找最小节点，下塔每次pop一个当时最小节点
                    # 所以出了for循环栈中最后一个就是第k个最小节点
                    node = node.left
            if not stack:
                break

        return stack[-1].val

