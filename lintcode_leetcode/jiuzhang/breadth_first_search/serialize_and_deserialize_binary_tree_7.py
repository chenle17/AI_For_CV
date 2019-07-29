from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

Example
Example 1:

Input：{3,9,20,#,#,15,7}
Output：{3,9,20,#,#,15,7}
Explanation：
Binary tree {3,9,20,#,#,15,7},  denote the following structure:
	  3
	 / \
	9  20
	  /  \
	 15   7
it will be serialized {3,9,20,#,#,15,7}
Example 2:

Input：{1,2,3}
Output：{1,2,3}
Explanation：
Binary tree {1,2,3},  denote the following structure:
   1
  / \
 2   3
it will be serialized {1,2,3}
Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

You can use other method to do serializaiton and deserialization.

Notice
There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.
'''
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here

        # 入参检测
        if root is None or root.val is None:
            return []

        # 放入第一个node的值（val）
        data = [root.val]
        # 按照BFS，在双端队列中加入第一个根节点（root node）
        dq = deque([root])
        while dq:
            # 从队列中取出一个node，判断左右子节点加入队列
            # dq中按照bfs 顺序存放树的节点，
            # 取出一个父节点，放入其子节点
            node = dq.popleft()
            if node.left is None:
                data.append('#')
            else:
                data.append(node.left.val)
                dq.append(node.left)
            if node.right is None:
                data.append('#')
            else:
                data.append(node.right.val)
                dq.append(node.right)

        return data

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if not data:
            return

        # 根据所给的bfs 顺序的节点生成node列表
        bfs_order = [TreeNode(val) if val != '#' else None for val in data]
        # 使用快慢索引指针
        # 因为一个父节点必定对应两个子节点，即使没有子节点，对应位置也以’#‘表示
        # 注：’#‘并没有子节点
        # 慢指针在所有节点的列表遍历，从零开始（即第一个节点：根节点）
        slow_ind = 0
        # 快指针在bfs 顺序列表遍历，从根节点的子节点开始遍历（1开始）
        fast_ind = 1
        # 创建列表存放所有非None节点
        nodes = [bfs_order[0]]
        while slow_ind < len(nodes):
            # 取出慢指针对应节点，为期添加子节点
            node = nodes[slow_ind]
            node.left = bfs_order[fast_ind]
            node.right = bfs_order[fast_ind + 1]
            # 慢指针+1，快指针表示子节点则+2
            slow_ind += 1
            fast_ind += 2

            # 如果当前节点存在子节点则加入节点列表nodes
            # 注：data传过来的数据为：
            # {3, 9, 20,# ,#,15,7, #, #, #, #}
            # 所以快指针不会越界
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return nodes[0]







