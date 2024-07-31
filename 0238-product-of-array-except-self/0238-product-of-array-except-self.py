import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst=[]
        ans=np.prod(nums)
        for i,x in enumerate(nums):
            if x==0:
                temp=np.prod(nums[:i])*np.prod(nums[i+1:])
                lst.append(int(temp))
            else:
                lst.append(ans//x)
        return lst


        