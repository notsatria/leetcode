class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k) -> bool:
            hours = 0
            for pile in piles:
                hours += -(-pile // k)
            
            return hours <= h

        left, right = 1, max(piles)

        while left <= right:
            hours = 0
            k = left + (right - left) // 2
       
            if canEatAll(k):
                right = k - 1
            else:
                left = k + 1
        
        return left
            