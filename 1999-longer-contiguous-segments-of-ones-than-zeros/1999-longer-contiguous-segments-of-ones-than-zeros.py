class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len_one=0
        len_zero=0
        temp1 =0
        temp0=0
        for x in s:
            if x =='1':
                temp1 += 1
                len_zero=max(temp0,len_zero)
                temp0=0
            else:
                temp0 += 1
                len_one = max(temp1,len_one)
                temp1 = 0
            print(x,temp1,temp0,len_one,len_zero)
        len_zero=max(temp0,len_zero)
        len_one = max(temp1,len_one)
        return len_one > len_zero        