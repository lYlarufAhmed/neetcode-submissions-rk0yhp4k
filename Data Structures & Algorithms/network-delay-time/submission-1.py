class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        print(dist)
        dist[k-1] = 0

        for _ in range(n-1):
            for u, v, w in times:
                if dist[v-1] > dist[u-1] + w: # relxation
                    dist[v-1] = dist[u-1] + w
        
        max_dist = max(dist)

        return -1 if max_dist == float("inf") else max_dist
             