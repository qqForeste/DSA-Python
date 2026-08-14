class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
    
        def BFS(grid, q):
            length = 0
            while q:
                
                for i in range(len(q)):
                    
                    r, c = q.popleft()
                 
                    
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c

                        if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647:
                            continue

                        grid[nr][nc] = length + 1
                        q.append((nr,nc))

            
                length += 1
                

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        BFS(grid, q) 
            