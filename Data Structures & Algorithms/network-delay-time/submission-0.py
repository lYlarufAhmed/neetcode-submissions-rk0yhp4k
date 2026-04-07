class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)
        
        for u, v, w in times:
            edges[u].append((w, v))

        t = 0

        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited: continue

            visited.add(n1)
            t = w1

            for w2, n2 in edges[n1]:
                heapq.heappush(minHeap, (w1+w2, n2))
        

        return t if len(visited) == n else -1