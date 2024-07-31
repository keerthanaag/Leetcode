class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            if x not in d:
                d.update({x:1})
            else:
                return x