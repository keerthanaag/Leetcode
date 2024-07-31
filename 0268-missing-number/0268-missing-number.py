class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set([x for x in range(len(nums)+1)])
        print(s)
        num=set(nums)
        a=s.difference(num)
        a=list(a)
        return a[0]
        