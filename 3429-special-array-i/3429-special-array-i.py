class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            print(nums[i:i+2])
            if sum(nums[i:i+2]) % 2 == 0:
                return False
        return True