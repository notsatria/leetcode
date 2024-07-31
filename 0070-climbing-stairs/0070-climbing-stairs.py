class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.fib(n + 1, memo)
        
        
    def fib(self, x: int, memo: dict) -> int:
        if x in memo:
            return memo[x]
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        memo[x] = self.fib(x - 2, memo) + self.fib(x - 1, memo)
        return memo[x]