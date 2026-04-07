from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        length = 0
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        ROW, COL = len(grid), len(grid[0])
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                if r == ROW-1 and c == COL -1:
                    return length
                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc


                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nc, nr) in visited or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1