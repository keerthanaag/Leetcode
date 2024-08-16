class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # def dec_to_bin(n):
        #     binary =" "
        #     x = 0
        #     if n==0:
        #         return "000000000"
        #     while n > 0 and x<=8: 
        #         s1 = str(int(n%2)) 
        #         binary += s1 
        #         n /= 2
        #         x = x + 1
        #         result = binary[::-1] 
        #     return result
        # binx=dec_to_bin(x)
        # biny=dec_to_bin(y)
        # count=0
        # n=len(binx)
        # for i in range(n):
        #     if binx[i]!=biny[i]:
        #         count+=1
        # return count
        value = str(bin(x^y))
        return value.count('1')


        