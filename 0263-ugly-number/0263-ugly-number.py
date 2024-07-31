class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        lst=[2,3,5]
        i=0
        temp=[]
        for x in lst:
            while(1):
                print(n,x,n%x)
                if n%x==0:
                    n=n//x
                    if n==1:
                        return True
                else:
                    break

        if n==1:
            return True
        else:
            return False


