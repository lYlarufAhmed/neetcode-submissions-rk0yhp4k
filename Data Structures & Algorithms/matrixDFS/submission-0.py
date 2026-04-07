class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if (r,c) in visit or min(r,c) < 0 or r == ROW or c == COL or grid[r][c]:
                return 0
            if r == ROW-1 and c == COL-1:
                return 1
            visit.add((r,c)) # for backtracking
            count = 0

            count += dfs(r-1, c)
            count += dfs(r+1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            visit.remove((r,c)) # for backtracking
            return count
        return dfs(0, 0)