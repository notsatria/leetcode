class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        if len(s) == 1:
            return False
        
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:
                if not stack or bracket != pairs[stack.pop()]:
                    return False
        
        return len(stack) == 0
            