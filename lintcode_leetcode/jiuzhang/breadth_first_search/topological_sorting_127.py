from collections import deque

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

'''

Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?

Clarification
Learn more about representation of graphs

Notice
You can assume that there is at least one topological order in the graph.
'''


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        if not graph:
            return None

        # 入度初始化
        indegree = {node: 0 for node in graph}
        # 计算所有节点入度
        for node in graph:
            for next_node in node.neighbors:
                indegree[next_node] += 1

        # 统计入度为0节点
        dq = deque()
        for k, v in indegree.items():
            if v == 0:
                dq.append(k)

        topo = []
        while dq:
            # 把走过的节点放入结果中
            node = dq.popleft()
            topo.append(node)
            # 邻居节点入度-1，并判断是否有入度为0加入循环dq
            for next_node in node.neighbors:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    dq.append(next_node)
                    
        if len(topo) == len(indegree):
            return topo
        return None

