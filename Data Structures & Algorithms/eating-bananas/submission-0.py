class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        res = right

        
        def timeTaken(k):
            time = 0
            for i in range(len(piles)):
                time += math.ceil(float(piles[i]) / k)
            return time

        while left <= right:
            middle = (left + right) // 2

            time = timeTaken(middle)

            if time <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return res

        
