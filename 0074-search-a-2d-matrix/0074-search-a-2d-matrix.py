class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for element in matrix:
            if self.binarySearch(element, target) != -1:
                return True
        return False
           
