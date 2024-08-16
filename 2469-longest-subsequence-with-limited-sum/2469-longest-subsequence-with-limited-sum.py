class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        lst=[]
        nums=sorted(nums) #[1,2,4,5]
        for x in queries:
            count=0
            temp=0
            for i,data in enumerate(nums):
                temp+=data
                if temp<=x:
                    count+=1
                else:
                    break
            lst.append(count)
        return lst

