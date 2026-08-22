class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        surrounded = defaultdict()

        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def BFS(r, c):
            surround = set()
            q = deque()
            q.append((r,c))
            surround.add((r,c))


            while q: 
                for i in range(len(q)):
                    ro, co = q.popleft()

                    for dr, dc in directions:
                        nr, nc = dr + ro, dc + co
                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in surround or board[nr][nc] == 'X':
                            continue
                        
                        surround.add((nr,nc))
                        q.append((nr,nc))

                        if nr == ROWS - 1 or nc == COLS - 1 or nr == 0 or nc == 0:
                            return None

            return surround


        for r in range(ROWS):
            if r == 0 or r == ROWS - 1:
                continue
            for c in range(COLS):
                if c == 0 or c == COLS - 1:
                    continue
                
                if board[r][c] == 'O':
                    cells = BFS(r,c)
                    if cells:
                        for cell in cells:
                            board[cell[0]][cell[1]] = 'X'

                        
