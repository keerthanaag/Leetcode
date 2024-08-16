class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        #(description=We want to reformat the string s such that each group contains exactly k characters.\it means that the first group can have less than K only if the other groups contains exactly K characters, int this case you mentioned, the last group are just with 3 elements...You can use module to discover how many characters can be on first group.)
        s=s.split('-')
        temp="".join(s)
        temp=temp[::-1]
        i=0
        ans=''
        while i<len(temp):
            t=temp[i:i+k]
            if len(ans)==0:
                ans+=t
            else:
                ans=ans+'-'+t
            i=i+k
        ans=ans[::-1]
        return ans.upper()

        