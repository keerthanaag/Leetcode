class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x>-2147483648) and (x <2147483647):
            rev=0
            temp = abs(x)
            while(temp!=0):
                remainder = temp % 10
                rev = (rev*10) + remainder
                temp = int(temp / 10)
            if x<0:
                rev = -abs(rev)
            if (rev < 2**31) and (rev > -2**31):
                return rev
            else:
                return 0
        else:
             return 0