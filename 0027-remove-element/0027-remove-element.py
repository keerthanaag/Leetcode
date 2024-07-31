class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #count the number of element in the list then iterate it the no of times using remove function thn return the length of the list
        n=nums.count(val)
        for i in range(0,n):
            nums.remove(val)
        k=len(nums)
        return k

