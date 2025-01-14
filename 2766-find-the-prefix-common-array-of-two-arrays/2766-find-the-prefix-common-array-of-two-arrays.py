class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        lst = []
        for i in range(1,len(A)+1):
            s = set(A[:i]).intersection(set(B[:i]))
            lst.append(len(s))
            print(A[:i],B[:i])
        return lst

        