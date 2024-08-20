class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for num in nums:
            length=0
            while num!=0:
                num=num//10
                length+=1
            if length %2==0:
                count+=1
        return count
            
        