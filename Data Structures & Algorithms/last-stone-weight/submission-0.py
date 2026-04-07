class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stone1 = max(stones)
            stones.remove(stone1)
            stone2 = max(stones)
            stones.remove(stone2)
            if stone1 == stone2:
                pass
            else:
                stones.append(abs(stone1)-abs(stone2))
        if not stones:
            return 0
        else:
            return max(stones) 