class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #sol:replace the 0's in nums1 with elements in nums2 ,then sort the list
        j=0
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j=j+1
        nums1=nums1.sort()