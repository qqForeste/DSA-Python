class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def DFS(r, c, visit, prevHeight):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))

            DFS(r + 1, c, visit, heights[r][c])
            DFS(r - 1, c, visit, heights[r][c])
            DFS(r , c + 1, visit, heights[r][c])
            DFS(r, c - 1, visit, heights[r][c])

        
        for r in range(ROWS):
            DFS(r, 0, pac, heights[r][0])
            DFS(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            DFS(0, c, pac, heights[0][c])
            DFS(ROWS - 1, c, atl, heights[ROWS - 1][c])

        print(atl)
        print(pac)
        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res



