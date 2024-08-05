class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        lst=[]
        for x in nums:
            if x not in d:
                d.update({x:1})
            else:
                lst.append(x)
        return lst

        