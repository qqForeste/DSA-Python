class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(grid, ro, co):
            
            q = deque()
            q.append((ro,co))

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
       

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if min(r,c) < 0 or c >= COLS or r >= ROWS or grid[r][c] == "0":
                        continue
                    
                    grid[r][c] = "0"

                    for dr, dc in directions:
                        q.append((r + dr, c + dc))

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(grid, r, c)

        
        return islands


            
                    
