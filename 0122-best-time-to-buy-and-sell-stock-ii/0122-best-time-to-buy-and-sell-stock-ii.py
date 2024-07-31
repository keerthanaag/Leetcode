class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i, x in enumerate(prices):
            if x < buy:
                buy = x
            else:
                profit += x - buy
                buy = prices[i]
        return profit
