class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        start = max(piles)
        low = 1
        high = start

        while low <= high:
            newRate = (low + high) // 2
            totalH = sum(map(lambda x: math.ceil(x/newRate), piles))
            if totalH <= h:
                start = newRate
                high = newRate - 1
            else:
                low = newRate + 1
        
        return start