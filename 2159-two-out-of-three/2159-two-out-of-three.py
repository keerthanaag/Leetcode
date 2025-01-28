class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums3) & set(nums1))
        temp = set(nums1).intersection(nums2)
        temp2 = set(nums2).intersection(nums3)
        temp3 = set(nums3).intersection(nums1)
        return list(temp.union(temp2).union(temp3))

        