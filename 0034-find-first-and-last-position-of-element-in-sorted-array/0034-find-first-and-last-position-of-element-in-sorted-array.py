class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst=[]
        flag=0
        for i in range(0,len(nums)):
            if nums[i]==target:
                lst.append(i)
                flag=1
        if flag==0:
            return [-1,-1]
        else:
            result=[]
            result.append(min(lst))
            result.append(max(lst))
            return result
        