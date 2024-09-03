class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d={chr(96+i):str(i) for i in range(1,27)}
        print(d)
        temp=''
        for x in s:
            temp+=d[x]
        temp=int(temp)
        for i in range(k):
            ans=0           
            while temp!=0:
                ans+=temp%10
                temp=temp//10
                print(i,ans,temp)
            print(ans)
            temp=ans
        return ans
            


        