class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        return list(set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums3) & set(nums1))

        