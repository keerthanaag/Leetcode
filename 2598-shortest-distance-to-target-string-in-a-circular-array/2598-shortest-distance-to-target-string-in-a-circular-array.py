class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        c = 0
        lst = []
        i = startIndex
        flag = 1
        while i != startIndex or flag == 1:
            flag = 0
            if words[i] == target:
                lst.append(c)
            c += 1
            i += 1
            if i == len(words):
                i = 0
        c = 0
        i = startIndex
        flag = 1
        while i != startIndex or flag == 1:
            flag = 0
            if words[i] == target:
                lst.append(c)
            c += 1
            i -= 1
            if i == -1:
                i = len(words)-1
        return min(lst)
        