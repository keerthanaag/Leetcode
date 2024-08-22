class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=0
        for i,x in enumerate(num):
            ans+=x*(10**(len(num)-i-1))
        ans+=k
        print(ans)
        lst=[]
        for x in str(ans):
            lst.append(int(x))
        return lst
        carry=0
        for i in range(-1,-len(num)-1,-1):
            if k >0:
                base=k%10
                k=k//10
            else:
                base=0
            #print(carry)
            num[i]=num[i]+base+carry
            carry=0
            if num[i]>9:
                carry=num[i]//10
                num[i]=num[i]%10
        while k!=0:
            base=k%10
            k=k//10
            val=base+carry
            num.insert(0,val)
            carry=0
            if val>9:
                carry=val//10
                num[0]=val%10
        if carry>0:
            num.insert(0,carry)
        return num
        
        