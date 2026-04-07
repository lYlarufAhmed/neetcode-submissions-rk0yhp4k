class Solution:
    def countBits(self, n: int) -> List[int]:
        def pop_count(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                
                n = n >> 1
            
            return count
        
        ans = [0]

        for i in range(1, n+1):
            ans.append(pop_count(i))
        
        return ans