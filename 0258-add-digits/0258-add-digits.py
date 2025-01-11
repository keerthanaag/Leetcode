class Solution:
    def addDigits(self, num: int) -> int:
        def fn(num):
            temp=0
            while num!=0:
                temp+=num%10
                num=num//10
            return temp
        while num >9:
            num=fn(num)
        return num