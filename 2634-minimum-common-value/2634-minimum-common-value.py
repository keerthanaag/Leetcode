class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        if len(s) == 0:
            return -1
        s = list(s)
        s.sort()
        return s[0]
                