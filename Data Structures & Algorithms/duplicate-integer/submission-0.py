class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # key : val
        found = False
        for i in range(len(nums)):
            if nums[i] in seen:
                found = True
            else:
                seen.add(nums[i])
        return found