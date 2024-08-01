class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        if len(nums1)<len(nums2):
            for x in nums1:
                if x in nums2:
                    lst.append(x)
                    nums2.remove(x)
        else:
            for x in nums2:
                if x in nums1:
                    lst.append(x)
                    nums1.remove(x)
        return lst