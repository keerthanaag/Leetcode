class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        lst=[]
        i=1
        while len(lst)<=k:
            if i not in arr:
                lst.append(i)
            i+=1
        return lst[k-1]
        