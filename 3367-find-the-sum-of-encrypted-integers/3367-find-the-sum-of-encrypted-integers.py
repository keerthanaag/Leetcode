class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            bal=0
            count=0
            while x!=0:
                bal=max(bal,x%10)
                x=x//10
                count+=1
            ans+=int(str(bal)*count)
        return ans

        