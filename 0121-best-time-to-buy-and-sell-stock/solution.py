class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            if prices[i] > prices[sell]:
                sell = i
            profit = max(profit, prices[sell]-prices[buy])
        return profit
