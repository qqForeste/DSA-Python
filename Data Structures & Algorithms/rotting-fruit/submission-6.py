class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]


        def BFS(q, fresh):
            
            length = 0

            while q and fresh >= 1:

                for i in range(len(q)):
                    r, c = q.popleft()
                    changed = False
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                            continue

                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
                length += 1
            
            return length if fresh < 1 else -1


        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        return BFS(q, fresh)

                    





