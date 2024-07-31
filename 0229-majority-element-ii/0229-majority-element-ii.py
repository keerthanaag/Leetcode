class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst=[]
        n=len(nums)
        dup=set(nums)
        for x in dup:
            if nums.count(x) > n/3:
                lst.append(x)
        return lst

        