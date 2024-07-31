class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_st=str(x)
        y=x_st[::-1]
        print(y)
        if x_st.__eq__(y):
            return True
        else:
            return False            