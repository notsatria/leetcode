class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # define char to count all letters
        char = {}
        # l and r for defining the sliding window
        l = 0
        # to count the most repeated letter
        mostFreq = 0
        
        for r in range(len(s)):
            # add every same letter by 1
            char[s[r]] = 1 + char.get(s[r], 0)
            # compare current letter count and before
            mostFreq = max(mostFreq, char[s[r]])
            
            # if the length of current window minus
            # the number of most frequent letter
            # is greater than the number of operation
            # move the left pointer to right by 1
            # and decrease char[l] by 1
            if r - l + 1 - mostFreq > k:
                char[s[l]] -= 1
                l += 1
            
            print(mostFreq)
            
        print(char)
        
        return r - l + 1
            