class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #convert to num thn add 1 to the num
        # import math
        # n=len(digits)
        # temp=0
        # for i in range(n):
        #     temp=temp+(digits[i]*math.pow(10,n-i-1))
        # temp=int(temp)+1
        # num = temp
        # count = 0
        # while num != 0:
        #     num //= 10
        #     count += 1
        # res= [1] * count
        # for i in range(count):
        #     res[i]=int(temp/(math.pow(10,count-i-1)))
        #     temp=temp%(math.pow(10,count-i-1))
        # return res
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]
