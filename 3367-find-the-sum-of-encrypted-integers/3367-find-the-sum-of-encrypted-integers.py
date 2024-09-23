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
            print(count,bal)
            val=int(str(bal)*count)
            print(val)
            ans+=val
        return ans

        