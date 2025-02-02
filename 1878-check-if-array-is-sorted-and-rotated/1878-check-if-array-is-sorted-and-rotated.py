from collections import deque
class Solution(object):
    def check(self, nums):
        d = deque(nums)
        sorted_nums = sorted(nums)
        for _ in range(len(nums)):
            if list(d) == sorted_nums:
                return True
            d.rotate(-1)  
        return False
        