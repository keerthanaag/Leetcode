class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s = arr[1] - arr[0]
        for i in range(len(arr)-1):
            val = arr[i+1] - arr[i]
            if s != val:
                return False
        return True
        