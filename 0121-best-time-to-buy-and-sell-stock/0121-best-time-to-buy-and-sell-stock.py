class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            
            potentialProfit = price - minPrice
            
            if potentialProfit > maxProfit:
                maxProfit = potentialProfit
            print(maxProfit)
        
        return maxProfit