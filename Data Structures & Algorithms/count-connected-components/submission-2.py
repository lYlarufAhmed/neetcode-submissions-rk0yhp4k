class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        # DFS 

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = [False for _ in range(n)]
        count = 0

        def dfs(node):
            for adj in adjList[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dfs(adj)
        
        # print(adjList)
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
            
        return count