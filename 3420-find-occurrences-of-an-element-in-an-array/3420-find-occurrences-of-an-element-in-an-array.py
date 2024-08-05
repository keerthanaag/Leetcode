class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        d={}
        count=0
        for i,val in enumerate(nums):
            if x==val:
                count+=1
                d.update({count:i})
        ans=[]
        for i in queries:
            if i in d:
                ans.append(d[i])
            else:
                ans.append(-1)
        return ans
        