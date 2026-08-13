class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle

            # left half is sorted
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:   # target inside left range
                    right = middle - 1
                else:
                    left = middle + 1
            # right half is sorted
            else:
                if nums[middle] < target <= nums[right]:   # target inside right range
                    left = middle + 1
                else:
                    right = middle - 1

        return -1