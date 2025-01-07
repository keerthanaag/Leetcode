class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst=set({})
        for i,x in enumerate(words):
            for y in words:
                if x in y and x!=y:
                    lst.add(x)
        return list(lst)
        