class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        arr = sorted(set(nums))
        counter = 1
        res = 0

        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1

        print(arr)     
        
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == 1 and arr[i + 1] != arr[i]:
                counter += 1
            else:
                counter = 1
                
            res = max(res, counter)

        return res