class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def fn(n):
            temp=0
            squared=0
            while n!=0:
                temp=n%10
                squared+=(temp**2)
                n=n//10
            return squared
        n=fn(n)
        while n >9:
            n=fn(n)
        if n==1 or n==7:
            return True
        else:
            return False
        