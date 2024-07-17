class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i, num in enumerate(nums):
            pointer = target - num
            if pointer in hashMap:
                return [i, hashMap[pointer]]
            else:
                hashMap[num] = i
            
        
