from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0))
        visited = set()
        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROW-1 and c == COL -1:
                    return length
                
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1,1)):
                    nr, nc = r+dr, c+dc

                    if min(nr, nc) < 0 or nc == COL or nr == ROW or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                
            length += 1

        return -1