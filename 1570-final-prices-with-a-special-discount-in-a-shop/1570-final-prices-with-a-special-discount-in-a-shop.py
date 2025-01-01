class Solution(object):
    def finalPrices(self, prices):
        for i in range(len(prices)-1):
            j=i+1
            while j < len(prices):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
                else:
                    j+=1
        return prices
        