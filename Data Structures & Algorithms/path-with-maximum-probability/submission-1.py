class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # we need multiple [star, end] possible value and return the max poss
        # [0: 0, 1: 0, 2: 0]
        
        adj = defaultdict(list)

        for i, [start, end] in enumerate(edges):
            adj[start].append((end, succProb[i]))
            adj[end].append((start, succProb[i]))

        pq = [(-1, start_node)]

        visited = set()

        while pq:
            prob, nei = heapq.heappop(pq)

            if nei in visited:
                continue

            if nei == end_node:
                return prob * -1

            visited.add(nei)
            
            for node, p in adj[nei]:
                heapq.heappush(pq, (p*prob, node))

        return 0
