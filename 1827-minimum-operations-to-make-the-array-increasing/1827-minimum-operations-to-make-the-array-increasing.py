class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                val = max(nums[i - 1] + 1, nums[i])
                if nums[i] < val:
                    operation += val - nums[i]
                    nums[i] = val
                    print(operation)
            
        print(nums)
        return operation