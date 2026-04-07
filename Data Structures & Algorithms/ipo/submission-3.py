class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [] # initially not profit
        
        maxHeap = [(c, p) for c,p in zip(capital, profits)]

        heapq.heapify(maxHeap)

        for _ in range(k):

            while maxHeap and maxHeap[0][0] <= w:
                c, p = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -p)

            if not minHeap:
                break
            w += -heapq.heappop(minHeap)

        return w