class Solution:
    def strStr(self, haystack: str, needle: str) -> int:       
        if not needle in haystack:
            return -1
        
        if haystack == needle:
            return 0
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
            
        return -1