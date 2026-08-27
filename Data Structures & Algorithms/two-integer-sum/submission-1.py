class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dit = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in dit:
                return[dit[compliment], i]
            
            dit[nums[i]] = i



        return []