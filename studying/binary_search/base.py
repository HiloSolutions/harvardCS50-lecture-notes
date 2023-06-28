class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1

        while l <= u:
            mid = int((l + u) / 2)
            
            if target < nums[mid]:
                u = mid - 1

            elif target > nums[mid]:
                l = mid + 1

            else:
                return mid
        
        return l