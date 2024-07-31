class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m=0
        for i in range(0,len(nums)):
            if target == nums[i]:
                m=1
                g=i
                break
            elif (target >nums[i]):
                l=i+1
            elif target < nums[0]:
                l=0
                break
        if m==1:
            return (g)
        else:
            return (l)
       
            
        

