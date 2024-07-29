class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                required_val = nums[i - 1] + 1
                operation += required_val - nums[i]
                nums[i] = required_val
            
        print(nums)
        return operation