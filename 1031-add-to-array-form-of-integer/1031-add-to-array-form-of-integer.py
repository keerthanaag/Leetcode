class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
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
        