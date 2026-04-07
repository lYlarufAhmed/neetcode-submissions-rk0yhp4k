class Solution:
    def climbStairs(self, n: int) -> int:
        
        #base case
        if n < 4:
            return n
        
        #memoization and dp

        mem = [i if i < 4 else 0 for i in range(n+1)]

        def dp(i):
            if mem[i] == 0:
                mem[i] = dp(i-1) + dp(i-2)
            return mem[i]

        dp(n)
        #general case
        return mem[n]