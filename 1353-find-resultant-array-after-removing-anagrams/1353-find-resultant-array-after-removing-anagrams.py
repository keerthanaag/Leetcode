class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=1
        n=len(words)
        while i<n:
            print(i,words[i],words[i-1])
            if sorted(words[i])==sorted(words[i-1]):
                words.pop(i)
                n=len(words)
            else:
                i+=1
        return words
        