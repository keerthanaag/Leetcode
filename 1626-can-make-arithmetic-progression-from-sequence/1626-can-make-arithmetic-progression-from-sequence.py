class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s= set({})
        for i in range(len(arr)-1):
            val = arr[i+1] - arr[i]
            s.add(val)
        if len(s) > 1:
            return False
        return True
        