class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n=len(pref)
        for x in words:
            if x[:n] == pref:
                count +=1
        return count

        