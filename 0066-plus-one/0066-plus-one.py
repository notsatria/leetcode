class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitStr = ""
        
        for i in range(len(digits)):
            digitStr += str(digits[i])
            
        operation = int(digitStr) + 1
        
        resStr = str(operation)
        res = []
        
        for i in range(len(resStr)):
            res.append(int(resStr[i]))
            
        return res