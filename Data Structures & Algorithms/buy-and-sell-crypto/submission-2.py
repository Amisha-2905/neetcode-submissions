class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < min_value:
                min_value = prices[i]
            if prices[i] - min_value > profit:
                profit = prices[i] - min_value
        return profit