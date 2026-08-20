class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """"
        ROWS = 3 COLS = 4
        [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
                        ^

        1 // ROW = R 5 // 4 = 1 correct
        5 % ROW = C 5 % 4 = 1

        matrix[1][2]

        grid[1][1] = 1 + (r * ROWS)

        row = 1 + (r * rows) 
        1 + (r * rows) 

        """
        
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        
        ROWS, COLS = len(matrix), len(matrix[0])
        

        while left <= right:
            middle = (left + right) // 2

            r = middle // COLS
            c = middle % COLS # 1 % 2 = 1 1 // 4 = 0

            
            print(middle)

            

            print((r,c))
            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                left = middle + 1
            elif matrix[r][c] > target:
                right = middle - 1
            
        
        return False

        