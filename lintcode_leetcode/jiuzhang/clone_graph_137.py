"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

Notice
You need return the node with the same label as the input node.
'''
import collections
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node
        root = node

        nodes = self.getNones(node)

        # 2. 深度复制所有的点（不包括相邻点信息）
        # 并与原始点生成映射
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # 3. 找到所有边，复制所有边
        # 便利所有原始点
        for node in nodes:
            # 新点
            new_node = mapping[node]
            # 遍历原始点的相邻点
            for neighbor in node.neighbors:
                # 复制原始点的边
                # 根据映射关系，把原始点的相邻点对应的新节点连接当前新节点（边）
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    # 1. 找到所有点
    def getNones(self, node):
        # 把输入点放入双向队列
        q = collections.deque([node])
        # 使用set存放所有点
        result = set([node])
        while q:
            # 取出队列第一个点
            head = q.popleft()
            # 遍历第一个的每一个相邻点
            for neighbor in head.neighbors:
                # 新找到的点放入set，并加入队列，继续循环队列，知道队列为空
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result