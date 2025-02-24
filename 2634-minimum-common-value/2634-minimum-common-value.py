class Solution(object):
    def getCommon(self, nums1, nums2):
        s = set(nums1).intersection(set(nums2))
        if len(s) == 0:
            return -1
        s = list(s)
        s.sort()
        return s[0]
        