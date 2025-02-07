class Solution(object):
    def fib(self, n):
        for i in range(n+1):
            if i == 0:
                prev1 = 0
                val = 0
            elif i == 1:
                prev2 = 1
                val = 1
            else:
                val = prev1+prev2
                prev1 = prev2
                prev2 = val
                print(prev1,prev2,val)      
        return val
        