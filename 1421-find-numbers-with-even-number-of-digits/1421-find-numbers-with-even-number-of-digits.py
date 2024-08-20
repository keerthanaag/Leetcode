class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            length=0
            while num!=0:
                num=num//10
                length+=1
            if length %2==0:
                count+=1
        return count
        # count=0
        # for x in nums:
        #     if len(str(x)) % 2==0:
        #         count+=1
        # return count
        