class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_positive=0
        no_negative=0
        for i in nums:
            if i>0:
                no_positive +=1
            elif i <0:
                no_negative +=1
        return max(no_positive,no_negative)
        