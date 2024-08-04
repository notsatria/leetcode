class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sumValues = 0
        
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    sumValues += 1
        
        return sumValues