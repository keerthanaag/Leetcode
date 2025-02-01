class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            print(nums[i:i+2])
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        return True