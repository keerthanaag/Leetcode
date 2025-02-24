class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        print(s)
        if len(s) == 0:
            return -1
        s = list(s)
        s.sort()
        print(s)
        print(s[0])
        return s[0]
                