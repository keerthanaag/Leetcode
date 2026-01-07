class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left,right+1):
            if i < 10:
                lst.append(i)
            else:
                temp = i
                flag = 1
                while i != 0: 
                    rem = i%10 
                    if rem == 0 or temp%rem != 0: 
                        flag = 0
                        break
                    i = i//10 
                    print(temp,rem,i)
                if flag == 1:
                    lst.append(temp)
        return lst