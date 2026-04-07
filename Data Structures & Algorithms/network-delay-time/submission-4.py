class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n)]
        dist[k-1] = 0

        for _ in range(n-1):
            for u, v, w in times:
                dist[v-1] = min(dist[v-1], dist[u-1] + w)
        

        res = max(dist)


        return res if res != float("inf") else -1