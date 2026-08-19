class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def BFS(grid, q):
            
            length = 0
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]

            while q:
                for i in range(len(q)):
                    ro,co = q.popleft()

                    if grid[ro][co] != -1 or grid[ro][co] != 0:
                        grid[ro][co] = length
                    
                    for dr, dc in dirs:
                        nr,nc = dr + ro, dc + co

                        if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1 or (nr,nc) in visit:
                            continue
                        q.append((nr,nc))
                        visit.add((nr,nc))
                
                length += 1
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))

        BFS(grid, queue)

        



