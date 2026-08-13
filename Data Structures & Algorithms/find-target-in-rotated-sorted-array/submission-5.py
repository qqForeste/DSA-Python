class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # left sorted
            if nums[left] <= nums[middle]:
                
                if target < nums[middle]  and target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1 
            else:

                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1
            #right sorted