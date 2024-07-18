class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            potentialProfit = prices[i] - minPrice
            
            if potentialProfit > maxProfit:
                maxProfit = potentialProfit
        
        return maxProfit