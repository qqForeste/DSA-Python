class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])

        def bfs(grid, q, fresh):

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            mins = 0
            print(fresh)

            while q:
                changed = False
                for i in range(len(q)):
                    r,c = q.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        
                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                            continue
                        
                        grid[nr][nc] = 2
                        print("here")
                        fresh -= 1
                        changed = True
                        q.append((nr,nc))

                if changed:
                    mins += 1

                

            print(fresh)
            if fresh < 1:
                return mins
            else:
                return -1

        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        return bfs(grid, q, fresh)



