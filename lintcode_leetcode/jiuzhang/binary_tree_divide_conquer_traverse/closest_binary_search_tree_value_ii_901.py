"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # write your code here

        if not root or not root.val:
            return []

        self.nums = []
        # 中序遍历
        self.get_nums(root)

        # 二分法找到与target最接近的位置
        indx = self.find_target(target)
        # 设置左右两个index
        left, right = indx - 1, indx + 1

        result = [self.nums[indx]]
        for _ in range(k - 1):
            # 先考虑一边越界的情况
            if left < 0:
                result.append(self.nums[right])
                right += 1
                continue
            elif right >= len(self.nums):
                result.append(self.nums[left])
                left -= 1
                continue

            # 不越界则考虑最接近的数
            if abs(self.nums[left] - target) >= abs(self.nums[right] - target):

                result.append(self.nums[right])
                right += 1
                continue

            else:
                result.append(self.nums[left])
                left -= 1
                continue

        return result

    def find_target(self, target):
        start, end = 0, len(self.nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.nums[mid] > target:
                end = mid
            elif self.nums[mid] < target:
                start = mid
            else:
                return mid

        if abs(self.nums[start] - target) > abs(self.nums[end] - target):
            return end
        return start

    # def get_nums(self, root):
    #     if root is None:
    #         return []

    #     self.get_nums(root.left)
    #     self.nums.append(root.val)
    #     self.get_nums(root.right)

    def get_nums(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                self.nums.append(stack[-1].val)


