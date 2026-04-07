class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Do a traverse and find out the rotten tomatos
        # maintain the queue
        queue = deque()

        min_time = 0 # time to rot
        direct = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0)
        )
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
        print(queue)
        # if not queue: return 
        while queue: # infinite timer elapsing one minute per cycle
            rotten = False
            rot_count =len(queue)
            for _ in range(rot_count):
                r, c = queue.popleft()
                for dr, dc in direct:
                    nr, nc = r+dr, c+dc
                    if (
                        min(nr,nc) >= 0 and 
                        nr < ROW and 
                        nc < COL and 
                        grid[nr][nc] == 1
                        ):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        rotten = True
            # if not queue and not min_time: return -1
            if rotten: min_time +=1 # at each cycle
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1: return -1
        return min_time
        