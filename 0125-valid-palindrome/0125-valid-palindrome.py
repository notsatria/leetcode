class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        s = s.lower()
        clean_s = []
        
        for char in s:
            char_ascii = ord(char) 
            if char_ascii >= 48 and char_ascii <= 57 or char_ascii >= 97 and char_ascii <= 122:
                clean_s.append(char)
        
        l, r = 0, len(clean_s) - 1
        
        print(clean_s)
        
        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
            
        return True
                