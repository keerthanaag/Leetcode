class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while(1):
            temp=3**i
            if n == temp:
                return True
            elif n < temp:
                return False
            i+=1