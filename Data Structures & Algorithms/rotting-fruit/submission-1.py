class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def BFS(grid, queue):
            ROWS, COLS = len(grid), len(grid[0])
            mins = 0

            while queue:
                rotted = False

                for i in range(len(queue)):
                    r, c = queue.popleft()
                    
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                            continue

                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        rotted = True

                if rotted:
                    mins += 1        
            return mins


        q = deque()
        for ro in range(len(grid)):
            for co in range(len(grid[0])):
                cell = grid[ro][co]

                if cell == 2:
                    q.append((ro,co))
                

        
        time = BFS(grid, q)
        
        fresh = False

        for ro in range(len(grid)):
            for co in range(len(grid[0])):
                cell = grid[ro][co]

                if cell == 1:
                    fresh = True

        
        if fresh:
            return -1
        else:
            return time



