class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()# 统计所有点

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])# 统计所有边

        return graph

    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)# 统计入度

        queue = []# 使用list方便统计长度
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)# 找到入口

        topo_order = []
        while queue:
            if len(queue) > 1:# 路径不唯一
                # there must exist more than one topo orders
                return False

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return False