# Bikin hasmap dengan key = closing bracket dan value open bracket
# Make a list
# loop trough s, on each char, push to the list, 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for char in s:
            if char not in dic:
                stack.append(char)
                continue
            if not stack or stack[-1] != dic[char]:
                return False
            stack.pop()
        
        return len(stack) == 0

        