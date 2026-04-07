class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DFS
        dist = {node: float("inf") for node in range(1, n+1)}

        # need adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        

        def dfs(node, time):
            if time > dist[node]: return


            dist[node] = time
            for v,w in adj[node]:
                dfs(v, time + w)
        
        dfs(k, 0)

        res = max(dist.values())
        return res if res != float("inf") else -1
