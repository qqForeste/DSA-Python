class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 5 = matrix[1][1]
        #matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        #           ^     ^       ^                 
        # r = middle // COLS
        # r 5 // 4 = 1
        # c = middle % COLS
        # c = 5 % 4 = 1

        while left <= right:
            middle = (left + right) // 2
            r = middle // COLS
            c = middle % COLS

            current = matrix[r][c]
            print(middle)
            print(current)
            print(r,c)

            if current == target:
                return True

            else:
                if current < target:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return False
            

