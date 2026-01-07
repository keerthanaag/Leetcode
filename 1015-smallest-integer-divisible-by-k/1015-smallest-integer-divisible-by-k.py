class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        if k%2 == 0 or k % 5 == 0:
            return -1
        else:
            rem = 0
            for i in range(0,k):
                rem = (rem*10+1)%k # rem = (10+1)%3 = 11%3 = 2*10+1 %3 = 21%3 = 0
                if rem == 0:
                    return i+1
            return -1
        