class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return nums
        d = {}
        lst=[]
        for x in nums:
            if x in d:
                val=d[x]
                val+=1
                d.update({x:val})
            else:
                val=1
                d.update({x:val})
        for x in nums:
            if d[x] == 1:
                lst.append(x)
        return lst
        