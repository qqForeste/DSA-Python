class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

       left = 1
       right = max(piles) 

       while left < right:
        middle = (left + right) // 2

        time = 0

        for i in range(len(piles)):
            time += math.ceil(piles[i] / middle)
        
        if time <= h:
            right = middle
        else:
            left = middle + 1
    
       return left