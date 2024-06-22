/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = prices[0]
    let maxProfit = 0
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i]
        }
        
        let potentialProfit = prices[i] - minPrice
        
        if (potentialProfit > maxProfit) {
            maxProfit = potentialProfit
        }
    }
    
    return maxProfit
};