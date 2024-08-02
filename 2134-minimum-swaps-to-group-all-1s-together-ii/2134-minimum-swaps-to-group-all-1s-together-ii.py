class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)

        if ones == 0 or ones == len(nums):
            return 0

        nums = nums + nums
        zerosInWindow = nums[:ones].count(0)
        minZeros = zerosInWindow

        print(nums)

        for i in range(ones, len(nums)):
            print(nums[i])
            if nums[i] == 0:
                zerosInWindow += 1
            print(nums[i - ones])
            if nums[i - ones] == 0:
                zerosInWindow -= 1
            minZeros = min(zerosInWindow, minZeros)

        return minZeros