class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        islands = 0
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.land = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] and grid[r][c] == "1":
                    print("ran this")
                    if (r,c) not in self.land:
                        islands += 1
                        self.DFS(grid, r, c, set())
                        print("ran dfs")
        
        return islands


    def DFS(self, grid,r,c,visited):
        if min(r,c) < 0 or r == self.ROWS or c == self.COLS or (r,c) in visited or grid[r][c] == "0":
            return 0
        
        count = 0
        visited.add((r,c))
        self.land.add((r,c))

        count += self.DFS(grid, r + 1, c, visited)
        count += self.DFS(grid, r - 1, c, visited)
        count += self.DFS(grid, r, c + 1, visited)
        count += self.DFS(grid, r, c - 1, visited)

        
        return 1