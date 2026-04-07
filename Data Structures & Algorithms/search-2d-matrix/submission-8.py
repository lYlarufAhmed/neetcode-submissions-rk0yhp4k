class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix) , len(matrix[0])

        if not (row or col): return False

        left = 0
        right = (max(row, 1) * max(col, 1) )-1

        # if left == 0 and right == 0:
        #     return matrix[0][0] == target

        get_cord = lambda i: (
            i // col,
             i % col
            )

        while left <= right:
            mid = (left + right) // 2
            r,c = get_cord(mid)
            print(r,c, mid, )
            
            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr < target:
                left = mid+1
            else:
                right = mid - 1
        return False