class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_yet = prices[0]
        for i, price in enumerate(prices):
            if price < min_yet:
                min_yet = price
            else:
                temp = price - min_yet
                profit = max(profit, temp)
        return profit