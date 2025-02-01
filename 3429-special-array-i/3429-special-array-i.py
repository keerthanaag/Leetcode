class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(len(nums)-1):
            print(nums[i:i+2])
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        return True