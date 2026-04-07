class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            if (r,c) in visited or min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            area = 1

            area += bfs(r+1, c)
            area += bfs(r-1, c)
            area += bfs(r, c+1)
            area += bfs(r, c-1)
            return area


        for r in range(ROW):
            for c in range(COL):
                if (r,c) in visited or grid[r][c] == 0: continue
                elif grid[r][c] == 1:
                     max_area = max(max_area, bfs(r, c))

        return max_area

