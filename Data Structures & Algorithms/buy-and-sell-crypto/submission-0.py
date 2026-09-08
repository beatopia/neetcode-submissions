class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            #check the profit of every combination of numbers to the right, not including i
            for j in range(i+1, len(prices)):
                profit = prices[j]-prices[i]
                if profit > max_profit:
                    max_profit = profit
        return(max_profit)
