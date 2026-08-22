class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        notsurrounded = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(board), len(board[0])

        def BFS(r, c, visit):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                for i in range(len(q)):
                    ro, co = q.popleft()

                    for dr, dc, in directions:
                        nr, nc = dr + ro, dc + co

                        if min (nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visit or board[nr][nc] == 'X':
                            continue
                        
                        visit.add((nr,nc))
                        q.append((nr,nc))

        
        for r in range(ROWS):
          
            if board[r][0] == 'O' and board[r][0] not in notsurrounded:
                BFS(r, 0, notsurrounded)
            if board[r][COLS - 1] == 'O' and board[r][COLS -1] not in notsurrounded:
                BFS(r, COLS - 1, notsurrounded)
        
        for c in range(COLS):
            
            if board[0][c] == 'O' and board[0][c] not in notsurrounded:
                BFS(0, c, notsurrounded)
            if board[ROWS - 1][c] == 'O' and board[ROWS - 1][c] not in notsurrounded:
                BFS(ROWS - 1, c, notsurrounded)
        
        for r in range(ROWS):
            for c in range(COLS):
            
                if board[r][c] == 'O' and not (r,c) in notsurrounded:
                    board[r][c] = 'X'


            
        
