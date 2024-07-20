class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split(" ")
        last = -1
        
        while not splitted[last].isalnum():
            last -= 1
        
        return len(splitted[last])