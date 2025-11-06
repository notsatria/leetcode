import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = math.floor((left + right) / 2)
            print(f"Mid {mid}")
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                left += 1
            else:
                right -= 1

        return -1
        