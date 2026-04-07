class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        ROW, COL = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if min(r,c) < 0 or (r, c) in visited or r == ROW or c == COL or grid[r][c] == '0':
                return 0
            visited.add((r,c))
            dfs(r+1 ,c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in visited or grid[r][c] == '0': continue
                elif grid[r][c] == '1':
                    count += 1
                    dfs(r,c)


        return count 