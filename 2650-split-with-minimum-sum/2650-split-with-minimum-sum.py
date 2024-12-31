class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = []
        while num != 0:
            rem = num % 10
            num = num // 10
            lst.append(rem)
        lst = sorted(lst) 
        num1 = ""
        num2 = ""
        for i in range(len(lst)):
            if i % 2 == 0:
                num1 += str(lst[i])
            else:
                num2 += str(lst[i])
        return int(num1) + int(num2)
        