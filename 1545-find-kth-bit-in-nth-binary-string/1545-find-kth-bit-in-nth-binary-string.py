class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0",]
        for i in range(1,n):
            t = ''
            for x in s[i-1]:
                if x == '1':
                    t+= '0'
                else:
                    t+= '1'
            st = "".join(t) 
            temp = s[i-1] + "1" + st[::-1]
            s.append(temp)
        return s[-1][k-1]