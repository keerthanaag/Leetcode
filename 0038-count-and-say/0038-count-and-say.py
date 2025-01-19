class Solution:
    def countAndSay(self, n: int) -> str:
        for i in range(1,n+1):
            if i == 1:
                st ="1"
            else:
                temp = st
                st = ""
                j = 0
                while j < len(temp):
                    if j == 0:
                        word = temp[j]
                        count = 1
                    elif word == temp[j]:
                        count += 1
                    else:
                        st += (str(count)+word)
                        word = temp[j]
                        count = 1
                    j+=1
                st += (str(count)+word)
        return st


        