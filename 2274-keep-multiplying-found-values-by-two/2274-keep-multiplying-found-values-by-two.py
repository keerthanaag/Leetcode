class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i,x in enumerate(nums):
            if x == original:
                original*=2
        return original