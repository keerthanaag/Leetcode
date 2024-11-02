class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sen = sentence.split(" ")
        prev=''
        curr=''
        if sen[0][0] != sen[-1][-1]:
            return False
        for i in range(1,len(sen)):
            prev=sen[i-1][-1]
            curr=sen[i][0]
            if prev != curr:
                return False
        return True    