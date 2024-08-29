class Solution:
    def sumZero(self, n: int) -> List[int]:
        i=0
        lst=[]
        num=1
        flag=0
        length=n
        if n%2!=0:
            length=n-1
            flag=1
        while i < length:
            lst.append(num)
            lst.append(-num)
            num+=1
            i+=2
            print(i,lst)
        if flag == 1:
            lst.append(0)
        return sorted(lst)



        