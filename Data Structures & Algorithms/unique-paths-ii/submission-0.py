class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        prevRow = [0] * cols

        for r in range(rows-1, -1, -1):
            currRow = [0] * cols

            if r == rows-1:

                currRow[cols-1] = 0 if obstacleGrid[r][cols-1] else 1
            else:
                currRow[cols-1] = 0 if obstacleGrid[r][cols-1] else prevRow[cols-1]
            
            for c in range(cols-2, -1, -1):
                currRow[c] = 0 if obstacleGrid[r][c] else currRow[c+1] + prevRow[c]
            
            prevRow = currRow
        
        return prevRow[0]