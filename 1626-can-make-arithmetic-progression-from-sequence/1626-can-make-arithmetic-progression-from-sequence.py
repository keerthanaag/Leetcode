class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        s = arr[1] - arr[0]
        for i in range(len(arr)-1):
            val = arr[i+1] - arr[i]
            if s != val:
                return False
        return True
        