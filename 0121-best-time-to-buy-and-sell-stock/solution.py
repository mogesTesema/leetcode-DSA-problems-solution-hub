class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -float("inf")
        days = len(prices)
        # for i in range(days):
        #     for j in range(i+1,days):
        #         max_profit = max(prices[j]-prices[i], max_profit)
        # return max_profit if max_profit > 0 else 0
        buy = 0
        sell = 1
        while sell < days:
            current_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit,current_profit)
            if current_profit < 0:
                buy = sell
            sell += 1
        return max_profit if max_profit > 0 else 0
            

