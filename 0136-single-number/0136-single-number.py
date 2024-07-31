class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find the length of the list to know the no of iterations then use count function to find the element which appeared only once
        # n=len(nums)
        # for i in range(0,n):
        #     j=nums[i]
        #     target=nums.count(j)
        #     if target == 1:
        #         return j
        d={}
        for x in nums:
            if x in d:
                val=d[x]
                val+=1
            else:
                val=1
            d.update({x:val})
        for x in d.keys():
            if d[x]==1:
                return x