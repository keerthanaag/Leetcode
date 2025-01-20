import numpy as np
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for x in nums:
            p *= x
        print(p)
        if p == 0:
            return 0
        elif p > 0:
            return 1
        else:
            return -1