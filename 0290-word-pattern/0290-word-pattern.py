class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t=s.split()
        if len(t)!=len(pattern):
            return False
        d={}
        for i in range(len(pattern)):
            d.update({pattern[i]:t[i]})
            print(d)
        sentence=''
        for x in pattern:
            sentence+=d[x]+' '
        print(sentence,s)
        if sentence.strip()==s:
            first= True
        else:
            first= False
        d2={}
        sen=''
        for i in range(len(pattern)):
            d2.update({t[i]:pattern[i]})
            print(d2)
        sen=''
        for x in t:
            sen+=d2[x]
        print(sen,pattern)
        if sen.strip()==pattern:
            scnd= True
        else:
            scnd= False
        print(first,scnd)
        if scnd == True and first == True:
            return True
        else:
            return False



        