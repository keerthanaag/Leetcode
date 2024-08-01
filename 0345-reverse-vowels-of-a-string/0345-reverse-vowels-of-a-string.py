class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=[]
        temp=''
        for x in s:
            if x=="e" or x=="o" or x=="i" or x=="u" or x=="a"or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
                vowel.append(x)
        if len(vowel)==0:
            return s
        i=-1
        for x in s:
            if x=="e" or x=="o" or x=="i" or x=="u" or x=="a"or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
                x=vowel[i]
                i-=1
            temp+=x
        return temp
        