class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles,reverse=True)
        you=0
        i=1
        pos=len(piles)-1
        while i<pos:
            you+=piles[i]
            print(i,piles[i],pos,piles[pos])
            pos-=1
            i+=2
        return you
        