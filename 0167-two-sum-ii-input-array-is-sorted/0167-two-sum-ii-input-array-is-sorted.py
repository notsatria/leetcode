class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}
        
        for i, num in enumerate(numbers):
            pointer = target - num
            
            if pointer in pairs:
                return [pairs[pointer], i+1] 
            pairs[num] = i + 1
        
        # print(pairs)
        