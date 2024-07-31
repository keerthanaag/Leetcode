class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #time limit exceeded
        # n=len(nums)
        # count=nums.count(0)
        # for j in range(0,count):
        #     for i in range(0,n-1):
        #         if nums[i]==0:
        #             temp=nums[i]
        #             nums[i]=nums[i+1]
        #             nums[i+1]=temp
        # return nums
        n1=len(nums)
        count=nums.count(0)
        for i in range(0,count):
            nums.remove(0)
        n2=len(nums)
        for i in range(n2,n1):
            nums.append(0)
        return nums
