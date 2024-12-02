class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l=sentence.find(searchWord)
        if l==-1:
            return l
        s=0
        n=len(searchWord)
        for i,x in enumerate(sentence):
            if x==' ':
                s+=1
            elif x==searchWord[0]:
                if searchWord == sentence[i:i+n] and (sentence[i-1]==' ' or i==0):
                    return s+1
        return -1
        
        