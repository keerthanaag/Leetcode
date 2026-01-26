class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        abs_diff = arr[1] - arr[0]
        result = []
        for i in range(0,len(arr)-1):
            if abs(arr[i+1]-arr[i]) == abs_diff:
                result.append([arr[i],arr[i+1]])
            elif abs(arr[i+1]-arr[i]) < abs_diff:
                abs_diff = abs(arr[i+1]-arr[i])
                result = []
                result.append([arr[i],arr[i+1]])
        return result
        