class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS, COLS = len(board), len(board[0])

        rowdict = defaultdict(list)
        coldict = defaultdict(list)

        squares = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in rowdict[r] or board[r][c] in coldict[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                
                rowdict[r].append(board[r][c])
                coldict[c].append(board[r][c])
                squares[(r // 3, c // 3)].append(board[r][c])

        print(rowdict)

        return True