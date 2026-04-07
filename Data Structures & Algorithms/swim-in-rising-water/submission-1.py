class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        maxH = max(max(r) for r in grid)

        minH = min(min(r) for r in grid)

        def canReach(node, t):
            r, c = node

            if min(r, c) < 0 or max(r,c) >= n or visited[r][c] or grid[r][c] > t:
                return False
            
            if r == n-1 and c == n-1: return True
            visited[r][c] = True

            return canReach((r, c+1), t) or \
            canReach((r, c-1), t) or \
            canReach((r+1, c), t) or \
            canReach((r-1, c), t)
        
        for t in range(minH, maxH):
            if canReach((0, 0), t):
                return t
            # reset the visited map
            visited = [[False] * n for _ in range(n)]

        return maxH





        