class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<3:#if length less than  return max of nums
            return max(nums)
        else:
            nums=set(nums)#convert to set to eradicate duplicates
            ans=sorted(nums,reverse=True)#incase of only +ve elements in list
            for i in nums:
                if i<0:
                    ans=sorted(nums,reverse=False)#incase of -ve elements in list
                    if len(ans)<3:
                        return max(ans)
                    else:
                        return ans[-3]
            if len(ans)<3:
                return max(ans)
            elif len(ans)==3:
                return min(ans)
            else:
                return ans[2]