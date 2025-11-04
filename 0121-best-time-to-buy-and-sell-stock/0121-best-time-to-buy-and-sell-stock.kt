/*
    Simpan prices[i] ke dalam sebuah variable global x
    lalu bandingkan prices[i] dengan x
    Jika prices[i] < x maka beli.

    lalu bikin variable local currentProfit = prices[i] - x
    bikin variable bestProfit = if (currentProfit > bestProfit) replace bestProfit dengan currentProfit
 */

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var maxProfit = 0
        var x = prices[0]
        for (i in 0..prices.size - 1) {
            if (prices[i] < x) {   
                x = prices[i]
            }

            val currentProfit = prices[i] - x
            if (currentProfit > maxProfit) {
                maxProfit = currentProfit
            }
        }

        return maxProfit
    }
}