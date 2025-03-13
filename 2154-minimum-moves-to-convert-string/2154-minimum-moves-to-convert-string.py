class Solution(object):
    def minimumMoves(self, s):
        i = 0
        cnt = 0
        if len(s) <= 3:
            if 'X' not in s:
                return 0
            return 1
        while i < len(s):
            if s[i] == 'O':
                i += 1
                continue
            temp = s[i:i+3]
            print(i,temp)
            if 'x' in temp.lower():
                cnt += 1
            i += 3
        return cnt
