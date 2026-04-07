class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        self.stones.sort(reverse=True)
        
        while len(self.stones) > 1:
            y, x, *rem = self.stones
            self.stones = rem + [y-x]
            self.stones.sort(reverse=True)
        return self.stones[0] 