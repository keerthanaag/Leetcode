class Solution(object):
    def closetTarget(self, words, target, startIndex):
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
            print(i, words[i], c, lst)
            c += 1
            i += 1
            if i == len(words):
                i = 0
        print("\n")
        #words = ["hello", "i", "am", "leetcode", "hello"]
        c = 0
        i = startIndex
        flag = 1
        while i != startIndex or flag == 1:
            flag = 0
            if words[i] == target:
                lst.append(c)
            print(i, words[i], c, lst)
            c += 1
            i -= 1
            if i == -1:
                i = len(words)-1
        return min(lst)
                