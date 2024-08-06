class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={str(i)+'#':chr(96+i) for i in range(10,27)}
        d.update({str(i): chr(96+i) for i in range(1,10)})
        s=s[::-1]
        i=0
        word=''
        while i<len(s):
            if s[i]=='#':
                print(s[i:i+3])
                t=s[i:i+3]
                word+=d.get(t[::-1])
                print(t[::-1])
                i=i+3
            else:
                word+=d.get(s[i])
                i+=1
        return word[::-1]
        