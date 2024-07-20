class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = ""
        left, right = strs[0], strs[-1]
        
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return res
            res += left[i]
        
        return res