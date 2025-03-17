class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        for x in nums:
            #print(x)
            if x not in d:
                d.update({x:1})
                #print("not in nums")
            else:
                #print(x,"entered in d")
                val=d.get(x)
                val+=1
                d.update({x:val})
        print(d)
        count=0
        left=0
        n=len(nums)
        no_of_pairs=n//2
        for x in d:
            count+=d[x]//2
            left+=d[x]%2
            if left>=1:
                return False
        if count == no_of_pairs:
            return True
        else:
            return False
        