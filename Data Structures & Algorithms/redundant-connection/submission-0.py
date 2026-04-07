class Solution:
    def _is_connected(self, src, des, visited, adj_list):
        visited[src] = True

        if src == des:
            return True

        res = False
        for node in adj_list[src]:
            if not visited[node]:
                res = res or self._is_connected(node, des, visited, adj_list)
            

        return res
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes_count = len(edges)

        adj_list = [[] for _ in range(nodes_count)]

        for edge in edges:
            visited = [False for _ in range(nodes_count)]

            if self._is_connected(edge[0]-1, edge[1]-1, visited, adj_list):
                return edge
            
            adj_list[edge[0]-1].append(edge[1]-1)
            adj_list[edge[1]-1].append(edge[0]-1)
        
        return []

