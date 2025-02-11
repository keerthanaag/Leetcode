from typing import List
from collections import Counter

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        num = sorted(nums, reverse=True)[:k]
        num_counts = Counter(num)
        lst = []
        
        for n in nums:
            if num_counts[n] > 0:
                lst.append(n)
                num_counts[n] -= 1
            if len(lst) == k:
                break
        
        return lst
