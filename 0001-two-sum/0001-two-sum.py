class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # map = {}
        # for i in range(len(nums)):
        #     if nums[i] not in map:
        #         map[target - nums[i]] = i 
        #     else:
        #         return map[nums[i]], i

        # return -1,-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i!=j and target == nums[i]+nums[j]:
                    return [i,j]
        

