"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []

        self.paths = []
        # 第一个格式不同，放在递归外面
        path = "{}".format(str(root.val))
        left = self.find_path(root.left, path)
        right = self.find_path(root.right, path)

        # 当只有根节点时
        if not left and not right:
            self.paths.append(path)

        return self.paths

    def find_path(self, root, path):
        if root is None:
            return None

        path += '->{}'.format(str(root.val))

        left = self.find_path(root.left, path)
        right = self.find_path(root.right, path)

        # 当前节点为叶子节点时
        if left is None and right is None:
            self.paths.append(path)

        return 1