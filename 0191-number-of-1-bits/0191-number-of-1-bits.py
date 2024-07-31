class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        s=str(bin(n))
        for x in s:
            if x=='1':
                count+=1
        return count
        