class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
        nums.sort()
        for i,x in enumerate(nums):
            if x == original:
                original*=2
        return original