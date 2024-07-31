class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price=prices[0]
        profit=0
        for x in prices:
            if price>x:
                price=x
            profit=max(profit,x-price)
        return profit
        # n=len(prices)
        # val=0
        # sort_prices=sorted(prices,reverse = True)
        # for i in range(n-1):
        #     sort_prices.remove(prices[i])
        #     max_profit=sort_prices[0]
        #     temp=max_profit-prices[i]
        #     if temp>0:
        #         val=max(val,temp)
        # return val



        

        