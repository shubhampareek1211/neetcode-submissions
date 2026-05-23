class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprofit = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    maxprofit = max(profit,maxprofit)
        return maxprofit

