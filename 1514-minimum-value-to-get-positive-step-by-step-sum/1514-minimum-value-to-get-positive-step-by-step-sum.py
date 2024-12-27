class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start =1
        i=0
        stepsum = start
        while i< len(nums):
            print(f"start: {start} i: {i}",end=" ")
            stepsum +=nums[i]
            if stepsum <1:
                print("updating start value",end=" ")
                start+=1
                stepsum = start
                i=0
            else:
                i+=1
            print(f"stepsum: {stepsum} ")
        return start
            
        