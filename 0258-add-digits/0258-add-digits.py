class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def fn(num):
            temp=0
            while num!=0:
                temp+=num%10
                num=num//10
            return temp
        while num >9:
            num=fn(num)
        return num
        