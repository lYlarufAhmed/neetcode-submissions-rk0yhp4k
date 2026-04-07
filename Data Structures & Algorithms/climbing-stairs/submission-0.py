class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n

        def dec(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dec(i+1) + dec(i+2)
            return cache[i]
        
        return dec(0)