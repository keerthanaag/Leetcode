class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find the length of the list to know the no of iterations then use count function to find the element which appeared only once
        n=len(nums)
        for i in range(0,n):
            j=nums[i]
            target=nums.count(j)
            if target == 1:
                return j