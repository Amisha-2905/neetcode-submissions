class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_yet = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_yet:
                min_yet = prices[i]
            else:
                profit = max(profit, prices[i] - min_yet)
        return profit
        