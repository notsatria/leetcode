class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
            
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
            
        for i in range(len(nums)):
            if max(target, nums[i]) != target:
                return i
 