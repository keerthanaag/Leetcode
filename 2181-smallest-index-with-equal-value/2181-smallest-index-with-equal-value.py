class Solution(object):
    def smallestEqual(self, nums):
        for i,x in enumerate(nums):
            if i % 10 == x:
                return i
        return -1