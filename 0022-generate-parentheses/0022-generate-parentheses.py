class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(openN, closeN, s):
            if len(s) == n*2:
                res.append(s)
                return
            
            if openN < n:
                backtracking(openN + 1, closeN, s + "(")
            if closeN < openN:
                backtracking(openN, closeN + 1, s + ")")
        
        backtracking(0, 0, "")
        
        return res
