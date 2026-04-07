class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = defaultdict(set)
        boxSeen = defaultdict(set)
        colSeen = defaultdict(set)

        def get_box_index(row, col):
            if row < 3 and col < 3:
                return 0
            elif row < 6 and col < 3:
                return 3
            elif row < 9 and col < 3:
                return 6
            elif row < 3 and col < 6:
                return 1
            elif row < 6 and col < 6:
                return 4
            elif row < 9 and col < 6:
                return 7
            elif row < 3 and col < 9:
                return 2
            elif row < 6 and col < 9:
                return 5
            elif row < 9 and col < 9:
                return 8

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]

                if num.isnumeric():
                    box_i = get_box_index(i, j)
                    if (num in rowSeen[i]) or (num in boxSeen[box_i]) or (num in colSeen[j]):
                        return False
                    boxSeen[box_i].add(num)
                    rowSeen[i].add(num)
                    colSeen[j].add(num)
        print(rowSeen, colSeen, boxSeen)
        return True

        