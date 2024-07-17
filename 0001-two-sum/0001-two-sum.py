class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i, num in enumerate(nums):
            hashMap[i] = num
            # print(hashMap)
            pointer = target - num
            for key, value in hashMap.items():
                if value == pointer and i != key:
                    return [i, key]
            
        
